#!/bin/bash

# wgetGSPCnight.bash

# Demo:
# ${HOME}/spy611/script/wgetGSPCnight.bash

# This script should be called by night.bash
# This script should get prices at night.

mkdir -p ${HOME}/spy611/public/csv/
cd       ${HOME}/spy611/public/csv/

TKR='GSPC'
rm -f ${TKR}2.csv

# curl 'http://tkrprice.herokuapp.com/static/gspc.csv'|sort -r > ${TKR}2.csv
curl 'http://tkrprice.herokuapp.com/static/gspc.csv'|\
    grep -v null|\
    awk -F, '{print $1","$5}' > ${TKR}2.csv

exit
