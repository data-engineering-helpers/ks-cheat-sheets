#!/usr/bin/env bash
#
# https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/frameworks/egeria/README.md

cd $HOME/dev/metadata/egeria/open-metadata-distribution/omag-server-platform/build/unpacked/egeria*gz/assembly/platform
java -Dloader.path=lib,extra -jar omag-server-platform*.jar

