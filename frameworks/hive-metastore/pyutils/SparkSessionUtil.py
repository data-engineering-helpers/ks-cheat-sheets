#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/hive-metastore/pyutils/SparkSessionUtil.py
#
#
import os
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from delta import *
from pathlib import Path

DATABRICKS_SERVICE_PORT = "8787"


class SparkSessionUtil:
    """
    Helper class for configuring Spark session based on the spark environment being used.
    Determines whether are using local spark, databricks-connect or directly executing on a cluster and sets up config
    settings for local spark as required.
    """

    @staticmethod
    def get_configured_spark_session(cluster_id=None):
        """
        Determines the execution environment and returns a spark session configured for either local or cluster usage
        accordingly
        :param cluster_id: a cluster_id to connect to if using databricks-connect
        :return: a configured spark session. We use the spark.sql.cerespower.session.environment custom property to store
        the environment for which the session is created, being either 'databricks', 'db_connect' or 'local'
        """
        # Note: We must enable Hive support on our original Spark Session for it to work with any we recreate locally
        # from the same context configuration.
        # if SparkSession._instantiatedSession:
        #     return SparkSession._instantiatedSession
        if SparkSession.getActiveSession():
            return SparkSession.getActiveSession()
        spark = SparkSession.builder.config("spark.sql.cerespower.session.environment", "databricks").getOrCreate()
        if SparkSessionUtil.is_cluster_direct_exec(spark):
            # simply return the existing spark session
            return spark
        conf = SparkConf()
        # copy all the configuration values from the current Spark Context
        for (k, v) in spark.sparkContext.getConf().getAll():
            conf.set(k, v)
        if SparkSessionUtil.is_databricks_connect():
            # set the cluster for execution as required
            # Note: we are unable to check whether the cluster_id has changed as this setting is unset at this point
            if cluster_id:
                conf.set("spark.databricks.service.clusterId", cluster_id)
                conf.set("spark.databricks.service.port", DATABRICKS_SERVICE_PORT)
                # stop the spark session context in order to create a new one with the required cluster_id, else we
                # will still use the current cluster_id for execution
            spark.stop()
            con = SparkContext(conf=conf)
            sess = SparkSession(con)
            return sess.builder.config("spark.sql.cerespower.session.environment", "db_connect",
                                       conf=conf).getOrCreate()
        else:
            # Set up for local spark installation
            # Note: metastore connection and configuration details are taken from <SPARK_HOME>\conf\hive-site.xml
            conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
            conf.set("spark.broadcast.compress", "false")
            conf.set("spark.shuffle.compress", "false")
            conf.set("spark.shuffle.spill.compress", "false")
            conf.set("spark.master", "local[*]")
            conf.set("spark.driver.host", "localhost")
            conf.set("spark.sql.debug.maxToStringFields", 1000)
            conf.set("spark.sql.hive.metastore.version", "2.3.7")
            conf.set("spark.sql.hive.metastore.schema.verification", "false")
            conf.set("spark.sql.hive.metastore.jars", "builtin")
            conf.set("spark.sql.hive.metastore.uris", "thrift://localhost:9083")
            conf.set("spark.sql.catalogImplementation", "hive")
            conf.set("spark.sql.cerespower.session.environment", "local")
            spark.stop()
            con = SparkContext(conf=conf)
            sess = SparkSession(con)
            builder = sess.builder.config(conf=conf)

            return configure_spark_with_delta_pip(builder).getOrCreate()

    @staticmethod
    def is_databricks_connect():
        """
        Determines whether the spark session is using databricks-connect, based on the existence of a 'databricks'
        directory within the SPARK_HOME directory
        :param spark: the spark session
        :return: True if using databricks-connect to connect to a cluster, else False
        """
        return Path(os.environ.get('SPARK_HOME'), 'databricks').exists()

    @staticmethod
    def is_cluster_direct_exec(spark):
        """
        Determines whether executing directly on cluster, based on the existence of the clusterName configuration
        setting
        :param spark: the spark session
        :return: True if executing directly on a cluster, else False
        """
        # Note: using spark.conf.get(...) will cause the cluster to start, whereas spark.sparkContext.getConf().get does
        # not. As we may want to change the clusterid when using databricks-connect we don't want to start the wrong
        # cluster prematurely.
        return spark.sparkContext.getConf().get("spark.databricks.clusterUsageTags.clusterName", None) is not None

