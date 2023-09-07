#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/postgresql/ipython-notebooks/confmgr.py
#
import json

k_cfg_fp: str = "config.json"

def get_conf() -> dict:
    """Retrieve the configuration as a Python ditionary
    """
    conf: dict = None
    try:
        with open(k_cfg_fp, "r") as conf_file:
            conf = json.load(conf_file)
    except Exception as error:
        print(f"Error - The '{k_cfg_fp}' configuration file cannot be found "
              f"- {error}")
        print("Hint: copy the config-sample.json file into config.json "
              "and adapt it")
    return conf

def get_db_conn_dict(verbose: bool=False) -> str:
    """Retrieve the database connection parameters, from the configuration
    file, as a Python dictionary
    """
    conf: dict = get_conf()

    #
    db_cfg: dict = conf.get("db")

    #
    return db_cfg

def get_db_conn_string(verbose: bool=False) -> str:
    """Retrieve the database connection string from the configuration file.
    * Only PostgreSQL is supported so far.
    * If the ~/.pgpass file is be used, leave the password empty in the JSON
      configuration file
    """
    pg_connstr: str = None

    #
    db_cfg: dict = get_db_conn_dict()

    #
    db_type: str = db_cfg.get("type")
    if db_type != "postgresql":
        print(f"In the '{k_cfg_fp}' configuration file, the expected database "
              f" type, namely '{db_type}', is not supported. Only 'postgresql' "
              "is supported so far")
        return pg_connstr
    
    #
    pg_host: str = db_cfg.get("host")
    pg_port: int = db_cfg.get("port")
    pg_dbname: str = db_cfg.get("dbname")
    pg_user: str = db_cfg.get("user")
    pg_passwd: str = db_cfg.get("passwd")
    if pg_passwd == "":
        if verbose:
            print(f"As the 'passwd' field is left empty in the '{k_cfg_fp}' "
                  "configuration file, the password will be read from the "
                  "~/.pgpass secret file")
        pg_connstr = f"{db_type}://{pg_user}@{pg_host}:{pg_port}/{pg_dbname}"
    else:
        pg_connstr = f"{db_type}://{pg_user}:{pg_passwd}@{pg_host}:{pg_port}/{pg_dbname}"

    #
    return pg_connstr
