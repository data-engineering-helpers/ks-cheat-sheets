#!/usr/bin/env python
#
# File: https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/minio/python/minio-browse.ipynb
#
import os
from cloudpathlib import CloudPath

geo_dir = CloudPath("s3://bronze/geonames")
for f in geo_dir.glob("**/*.parquet"):
    print(f)

