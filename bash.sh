#!/bin/bash

while true
do

wget https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-recent.json.gz

gunzip -f nvdcve-1.0-recent.json.gz

jq -r '.CVE_data_timestamp' nvdcve-1.0-recent.json > actual_time.txt

jq -r '.CVE_Items[].cve.CVE_data_meta.ID' nvdcve-1.0-recent.json > lines_of_cve.txt

jq -r '.CVE_Items[].publishedDate' nvdcve-1.0-recent.json > lines_of_dates.txt

jq -r '.CVE_Items[].cve.description.description_data[].value' nvdcve-1.0-recent.json > lines_of_desc.txt


sleep 600
done
