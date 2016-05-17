#!/bin/bash

# ~/spy611v2/script/wgetGSPC.bash

# This script should get prices at 12:50 Calif time.

mkdir -p ${HOME}/spy611v2/public/csv/
cd       ${HOME}/spy611v2/public/csv/

TKRH='%5EGSPC'
TKR='GSPC'
rm -f ${TKR}.csv ${TKR}.html

# I should get CSV data:
${HOME}/spy611v2/script/wgetGSPCnight.bash

# I should extract recent prices from html
wget --output-document=${TKR}.html http://finance.yahoo.com/q?s=$TKRH
${HOME}/anaconda3/bin/python ${HOME}/spy611v2/script/extprice.py
# I should cat prices together
echo 'cdate,cp'                                > ${TKR}3.csv
cat ${TKR}recent.csv ${TKR}2.csv|grep -v date >> ${TKR}3.csv
mv  ${TKR}3.csv                                  ${TKR}2.csv 
mv  ${TKR}.html /tmp/
exit
