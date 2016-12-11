# ~/spy611/script/genf.py

# This script should generate features from prices

# Demo:
# cd     ~/spy611/public/csv/
# python ~/spy611/script/genf.py GSPC2.csv

import pandas as pd
import numpy  as np
import pdb

# I should check cmd line arg
import sys

if len(sys.argv) == 1:
  print('Demo:')
  print('cd     ~/spy611/public/csv/')
  print('python ~/spy611/script/genf.py GSPC2.csv')
  print('...')
  sys.exit()

infile = sys.argv[1]
print('I am building features from this file:')
print(infile)
print('Busy...')

df1  = pd.read_csv(infile)
df1.columns = ['cdate','cp']

cp_a = df1[['cp']].values
# cp should be a list sorted by date-ascending:
cp   = [elm[0] for elm in reversed(cp_a)]

cplead_l  = cp + [cp[-1]]
cplag1_l  = [cp[0]] + cp
cplag2_l  = [cp[0],cp[0]]             + cp
cplag4_l  = [cp[0],cp[0],cp[0],cp[0]] + cp
cplag8_l  = [cp[0],cp[0],cp[0],cp[0]] + cplag4_l
cplag16_l = [cp[0]]*16 + cp


# I should snip off ends so new columns as long as cp:
cplead_l  = cplead_l[1:]
cplag1_l  = cplag1_l[:-1]
cplag2_l  = cplag2_l[:-2]
cplag4_l  = cplag4_l[:-4]
cplag8_l  = cplag8_l[:-8]
cplag16_l = cplag16_l[:-16]

# NumPy allows me to do arithmetic on its Arrays.
# I should convert my lists to Arrays:
cp_a      = np.array(cp)
cplead_a  = np.array(cplead_l)
cplag1_a  = np.array(cplag1_l)
cplag2_a  = np.array(cplag2_l)
cplag4_a  = np.array(cplag4_l)
cplag8_a  = np.array(cplag8_l)
cplag16_a = np.array(cplag16_l)

# I should calculate pct-deltas:
pctlead_a  = 100.0 * (cplead_a - cp_a)/cp_a
pctlag1_a  = 100.0 * (cp_a - cplag1_a)/cplag1_a
pctlag2_a  = 100.0 * (cp_a - cplag2_a)/cplag2_a
pctlag4_a  = 100.0 * (cp_a - cplag4_a)/cplag4_a
pctlag8_a  = 100.0 * (cp_a - cplag8_a)/cplag8_a
pctlag16_a = 100.0 * (cp_a - cplag16_a)/cplag16_a

# I am done doing calculations.
# I should put my columns into a DataFrame.
# I should order by cdate ascending not descending because descending is ... wrong.
cdate_l = list(reversed(df1['cdate'].values))
df2         = pd.DataFrame(cdate_l)
df2.columns = ['cdate']
df2['cp']   = cp

df2['pctlead']  = pctlead_a
df2['pctlag1']  = pctlag1_a
df2['pctlag2']  = pctlag2_a
df2['pctlag4']  = pctlag4_a
df2['pctlag8']  = pctlag8_a
df2['pctlag16'] = pctlag16_a

# I should save my work into a CSV file.
# My input file should look something like this:
# GSPC2.csv
# I should save my work as something like this:
# ftrGSPC2.csv
df2.to_csv('ftr'+infile, float_format='%4.3f', index=False)
print('Done...')

# done
