# rgb.py

# This script should help me build the red, green,blue visualizations.

import numpy  as np
import pandas as pd
import datetime
import matplotlib
import pdb

# I should check cmd line arg
import sys
if (len(sys.argv) < 3):
  print('Demo:')
  print('cd /tmp/ddata')
  print('python ${HOME}/spy611v2/script/rgb.py 2010 2016')
  print('...')
  sys.exit()

startyr = int(sys.argv[1])
finalyr = int(sys.argv[2])

# I should create a loop which does train and test for each yr.
for yr in range(startyr,1+finalyr):
  predf   = 'predictions'+str(yr)+'.csv'
  pred_df = pd.read_csv(predf)
  # I should get leadp which is the price 1 ahead of cp:
  cp_l    = [p_f for p_f in pred_df['cp']]
  leadp_l = cp_l[1:] + [cp_l[-1]]
  # I should get lead_l which is leadp - cp
  lead_l  = list(np.array(leadp_l)-np.array(cp_l))
  pred_df['lead']  = lead_l
  pred_df['rdelta']=pred_df['actual_dir']*pred_df['pdir_nb']*np.sign(pred_df['lead'])*pred_df['lead']
  pred_df['gdelta']=pred_df['actual_dir']*pred_df['pdir_lr']*np.sign(pred_df['lead'])*pred_df['lead']
  # I should get initial red_l, green_l
  red_l   = [cp_l[0]]
  green_l = [cp_l[0]]
  rcount  = 0
  # I should grow red_l, green_l
  for rdelta in pred_df['rdelta']:
    rcount += 1
    red_l.append(red_l[rcount-1]+rdelta)
  gcount  = 0
  for gdelta in pred_df['gdelta']:
    gcount += 1
    green_l.append(green_l[gcount-1]+gdelta)
  # I should add red_l, green_l to df:
  pred_df['red']   = red_l[:-1]
  pred_df['green'] = green_l[:-1]
  # matplotlib likes dates:
  cdate_l = [datetime.datetime.strptime(row, "%Y-%m-%d") for row in pred_df['cdate'].values]

  # I should plot
  matplotlib.use('Agg')
  # Order is important here.
  # Do not move the next import:
  import matplotlib.pyplot as plt
  plt.figure(figsize=(15,10))
  #  plt.plot(cdate_l, cp_l, 'b-', cdate_l, green_l[:-1], 'g-')# cdate_l, red_l[:-1], 'r-') #
  plt.plot(cdate_l, red_l[:-1], 'r-', cdate_l, green_l[:-1], 'g-', cdate_l, cp_l, 'b-',)

  plt.title('Red,Green,Blue Visualization (Red: Naive-Bayes, Green: Logistic-Regression, Blue: Long Only)')
  plt.grid(True)
  pngf = 'plot'+str(yr)+'.png'
  plt.savefig(pngf)
  plt.close()
  print('New png file: ')
  print(pngf)
  # I should save the red, green, blue data-points:
  pred_df.to_csv('rgb_df'+str(yr)+'.csv', float_format='%4.3f', index=False)
'bye'

