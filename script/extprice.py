# ~/spy611/script/extprice.py

# This script should extract recent date and prices from html

# Demo:
# TKRH='%5EGSPC'
# TKR='GSPC'
# wget --output-document=${TKR}.html http://finance.yahoo.com/q?s=$TKRH
# ${HOME}/anaconda3/bin/python ${HOME}/spy611/script/extprice.py

import bs4
import datetime
import pdb

soup       = bs4.BeautifulSoup(open("GSPC.html"), "lxml")
div_qhi    = soup.find(id="quote-header-info")
# gspc_price = div_qhi.find('section').find('span').string.replace(',','')
# Bug fix 2016-12-01:
gspc_price = div_qhi.findAll('span')[4].string.replace(',','')

# div_qmn = soup.find(id="quote-market-notice")
# div_qmn_span_s = div_qmn.find('span').string
# date_s = div_qmn_span_s.replace('As of ','').replace('.','')
# date_s_l = date_s.split()
# mydt_s = date_s_l[0]+' '+date_s_l[1]+' '+date_s_l[2]

mydt   = datetime.datetime.now()
mydt_s = mydt.strftime('%Y-%m-%d')
gspc_s = mydt_s+','+gspc_price+"\n"
gspcf  = open('GSPCrecent.csv','w')
gspcf.write(gspc_s)
gspcf.close()

'bye'
