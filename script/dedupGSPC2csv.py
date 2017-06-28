"""
~/spy611/script/dedupGSPC2csv.py

This script should use groupby-mean to dedup GSPC2.csv
"""

import pdb
import pandas as pd

pdb.set_trace()
prices_df = pd.read_csv('GSPC2.csv')

gb_df = prices_df.groupby(['cdate']).cp.mean()

gb_df.to_csv('/tmp/gb.csv')

'bye'
