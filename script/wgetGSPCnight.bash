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

wget --output-document=${TKR}2.csv http://tkrapi2.herokuapp.com/static/tkrs/gspc.csv
#ichart.finance.yahoo.com/table.csv?s=${TKRH}

exit
