#!/bin/bash

# ~/spy611/script/wgetGSPC.bash

# This script should get prices at 12:50 Calif time.

mkdir -p ${HOME}/spy611/public/csv/
cd       ${HOME}/spy611/public/csv/

TKRH='%5EGSPC'
TKR='GSPC'
rm -f ${TKR}.csv ${TKR}.html

# I should get CSV data:
${HOME}/spy611/script/wgetGSPCnight.bash

# I should extract recent prices from html
wget --output-document=${TKR}.html http://finance.yahoo.com/q?s=$TKRH

${HOME}/anaconda3/bin/python ${HOME}/spy611/script/extprice.py
exit
# I should cat prices together
echo 'cdate,cp'                                 > ${TKR}3.csv
cat ${TKR}2.csv ${TKR}recent.csv|grep -iv date >> ${TKR}3.csv
mv  ${TKR}3.csv                                   ${TKR}2.csv 
mv  ${TKR}.html /tmp/spy611_${TKR}.html

${HOME}/anaconda3/bin/python ${HOME}/spy611/script/dedupGSPC2csv.py
cp /tmp/gb.csv ${TKR}2.csv 
exit
