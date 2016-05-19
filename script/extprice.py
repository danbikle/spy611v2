# ~/spy611v2/script/extprice.py

# This script should extract recent date and prices from html

# Demo:
# TKRH='%5EGSPC'
# TKR='GSPC'
# wget --output-document=${TKR}.html http://finance.yahoo.com/q?s=$TKRH
# ${HOME}/anaconda3/bin/python ${HOME}/spy611v2/script/extprice.py

import bs4
import datetime
import pdb

soup   = bs4.BeautifulSoup(open("GSPC.html"), "lxml")
span0  = soup.find(id="yfs_market_time")
date_l = span0.string.split(",")[:3]
date_s = date_l[1]+date_l[2]
mydt   = datetime.datetime.strptime(date_s, " %b %d %Y")
mydt_s = mydt.strftime('%Y-%m-%d')

span1      = soup.find(id="yfs_l10_^gspc")
gspc_price = span1.string.replace(',','')
gspc_s     = mydt_s+','+gspc_price+"\n"
gspcf      = open('GSPCrecent.csv','w')
gspcf.write(gspc_s)
gspcf.close()

'bye'
