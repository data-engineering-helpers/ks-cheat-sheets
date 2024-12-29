#!/usr/bin/env bash

# SQLMesh state database parameters
SQLMESH_PG_SVR="localhost"
SQLMESH_PG_DB="sqlmesh"
SQLMESH_PG_USR="sqlmesh"
SQLMESH_PG_SCH="sqlmesh"

# Sanity checks
if [ $(command -v psql) ]
then
	PSQL_VER="$(psql --version 2> /dev/null)"
	# echo "PostgreSQL CLI tool found - Version: ${PSQL_VER}"
else
	echo "Error - the psql command (PostgreSQL CLI tool) cannot be found"
	echo "   * On MacOS, it can be installed with brew install postgresql"
	echo "   * On Linux, it can be installed with the native packager, for instance"
	echo "     * On Fedora/CentOS/RedHat/Rocky OSes: dnf -y install postgresql"
	echo "     * On Debian-/Ubuntu-based OSes: sudo apt-get install postgresql-client"
	exit 1
fi

# The credentials for the PostgreSQL database are assumed to be in the ~/.pgpass file
declare -a table_list=($(psql -h ${SQLMESH_PG_SVR} -U ${SQLMESH_PG_USR} -d ${SQLMESH_PG_DB} -t -c "select table_name from information_schema.tables where table_schema = '${SQLMESH_PG_SCH}'"))
table_list_length=${#table_list[@]}

# Reporting
if [ "${table_list_length}" == "0" ]
then
	echo "The PostgreSQL database (Server: ${SQLMESH_PG_SVR} - DB: ${SQLMESH_PG_DB} - User: ${SQLMESH_PG_USR}) has no more state-related tables"
else
	echo "List of tables in PostgreSQL to store the state: ${table_list[@]}"
fi

# Drop every single state table
for table in "${table_list[@]}"
	do echo "Dropping ${table} table..."
	echo "Command to be executed: psql -h ${SQLMESH_PG_SVR} -U ${SQLMESH_PG_USR} -d ${SQLMESH_PG_DB} -c \"drop table if exists ${SQLMESH_PG_SCH}.${table};\" "
	psql -h ${SQLMESH_PG_SVR} -U ${SQLMESH_PG_USR} -d ${SQLMESH_PG_DB} -c "drop table if exists ${SQLMESH_PG_SCH}.${table};"
	echo "... ${table} table dropped"
done

