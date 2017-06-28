"""
~/spy611/script/dedupGSPC2csv.py

This script should use prices_df.groupby(['cdate']).cp.mean() to dedup GSPC2.csv
"""

import pdb
import pandas as pd

prices_df = pd.read_csv('GSPC2.csv')
gb_df     = prices_df.groupby(['cdate']).cp.mean()

gb_df.to_csv('/tmp/gb.csv', float_format='%4.3f',index_label='cdate',header=True)

'bye'
