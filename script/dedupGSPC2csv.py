"""
~/spy611/script/dedupGSPC2csv.py

This script should use prices_df.groupby(['cdate']).cp.mean() to dedup GSPC2.csv
"""

import pdb
import pandas as pd

prices_df = pd.read_csv('GSPC2.csv')
gb_df     = prices_df.groupby(['cdate']).cp.mean()
# I should now have dedupped data but last price might be wrong.

# I should get a very last price I trust:
lastprice_f = prices_df.cp.iloc[-1]

# I should update gb_df with better last price:
gb_df.iloc[-1] = lastprice_f

# I should write the dedupped data to csv:
gb_df.to_csv('/tmp/gb.csv', float_format='%4.3f',index_label='cdate',header=True)

'bye'
