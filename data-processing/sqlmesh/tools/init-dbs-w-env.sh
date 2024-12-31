#!/usr/bin/env bash

# Sanity checks
if [ -z "${DBS_SVR_HST}" ]
then
	echo "Error - The DBS_SVR_HST environment variable should be set, but does not appear to be"
	echo "        It should point to the DataBricks workspace URL (e.g., <some-workspace>.cloud.databricks.com)"
	exit 1
else
	echo "DataBricks server host: ${DBS_SVR_HST}"
fi
if [ -z "${DBS_HTTP_PATH}" ]
then
	echo "Error - The DBS_HTTP_PATH environment variable should be set, but does not appear to be"
	echo "        It should point to the DataBricks HTTP path of the cluster (e.g., sql/protocolv1/o/<wksp-id>/<cluster-id>)"
	exit 1
else
	echo "DataBricks server host: ${DBS_HTTP_PATH}"
fi
if [ -z "${DBS_PAT}" ]
then
	echo "Error - The DBS_PAT environment variable should be set, but does not appear to be"
	echo "        It should point to the DataBricks Personal Access Token (PAT)"
	exit 1
else
	echo "DataBricks Personal Access Token specified, that is fine"
fi
if [ -z "${DBS_SCH}" ]
then
	echo "Error - The DBS_SCH environment variable should be set, but does not appear to be"
	echo "        It should point to the DataBricks schema (e.g., schema_example)"
	exit 1
else
	echo "DataBricks schema: ${DBS_SCH}"
fi

#
declare -a file_list=($(ls *.in */*.in))
file_list_length=${#file_list[@]}

# Reporting
if [ "${file_list_length}" == "0" ]
then
	echo "There is no file where environment variables should be substituted"
else
	echo "List of files where environment variables should be substituted: ${file_list[@]}"
fi

# Drop every single state table
for myfile in "${file_list[@]}"
do
	myfile_dir="$(dirname ${myfile})"
	myfile_tgt_fn="$(basename ${myfile} .in)"
	myfile_tgt="${myfile_dir}/${myfile_tgt_fn}"
	echo "Substituting environment variables in ${myfile} => ${myfile_tgt}..."
	echo "Command to be executed: envsubst < ${myfile} > ${myfile_tgt}"
	envsubst < ${myfile} > ${myfile_tgt}
	echo "... env vars substituting in ${myfile} => ${myfile_tgt}"
done


