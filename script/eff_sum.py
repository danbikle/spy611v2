# eff_sum.py

# This script computes a sum of effectiveness from allpredictions.csv

import pandas as pd
import numpy  as np
import pdb

eff_df = pd.read_csv('../public/csv/allpredictions.csv')
# print(eff_df.head())
# print(eff_df.tail())

pctlead_sum  = np.sum(eff_df['pctlead'])
eff1d_lr_sum = np.sum(eff_df['eff1d_lr'])
eff1d_nb_sum = np.sum(eff_df['eff1d_nb'])

print('pctlead_sum:')
print( pctlead_sum)

# if eff1d_lr_sum > pctlead_sum
# then Logistic Regression is effective:
print('eff1d_lr_sum:')
print( eff1d_lr_sum)

# if eff1d_nb_sum > pctlead_sum
# then Naive Bayes is effective:
print('eff1d_nb_sum:')
print( eff1d_nb_sum)
