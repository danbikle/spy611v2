# acc_eff.py

# This script should report accuracy and effectiveness from CSV files in /tmp/ddata/

import numpy  as np
import pandas as pd
import pdb

# I should check cmd line arg
import sys
if (len(sys.argv) < 3):
  print('Demo:')
  print('cd /tmp/ddata')
  print('python ${HOME}/spy611/script/acc_eff.py 2013 2016')
  print('...')
  sys.exit()

startyr = int(sys.argv[1])
finalyr = int(sys.argv[2])

# I should create a loop which does train and test for each yr.
for yr in range(startyr,1+finalyr):
  predf   = 'predictions'+str(yr)+'.csv'
  pred_df = pd.read_csv(predf)
  # I should count
  tp_pred = (pred_df['accuracy_nb'] == 'True Positive')
  tn_pred = (pred_df['accuracy_nb'] == 'True Negative')
  fp_pred = (pred_df['accuracy_nb'] == 'False Positive')
  fn_pred = (pred_df['accuracy_nb'] == 'False Negative')
  tp_df   =  pred_df[tp_pred]
  tn_df   =  pred_df[tn_pred]
  fp_df   =  pred_df[fp_pred]
  fn_df   =  pred_df[fn_pred]
  tp_i = len(tp_df)
  tn_i = len(tn_df)
  fp_i = len(fp_df)
  fn_i = len(fn_df)
  rpt_s = 'For '+str(yr)+':'+'\n'
  rpt_s += 'Naive-Bayes: Positive, Up,   Prediction Count is '+str(tp_i+fp_i)+'\n'
  rpt_s += 'Naive-Bayes: Negative, Down, Prediciton Count is '+str(tn_i+fn_i)+'\n'
  #pdb.set_trace()
  # bug below: divide by 0 for 2017 because nb has no pos-predictions (yet).
  #rpt_s += 'Naive-Bayes: Positive Accuracy is '+str(np.round(100*tp_i / (tp_i+fp_i)))+'%\n'
  #rpt_s += 'Naive-Bayes: Negative Accuracy is '+str(np.round(100*tn_i / (tn_i+fn_i)))+'%\n'
  rpt_s += 'Naive-Bayes: Total Accuracy is '+str(np.round(100*(tp_i+tn_i)/(tp_i+fp_i+tn_i+fn_i)))+'%\n'
  # I should compute effectiveness
  pred_up_pred   = (pred_df['pdir_nb'] ==  1)
  pred_down_pred = (pred_df['pdir_nb'] == -1)
  pred_up_df     = pred_df[pred_up_pred]
  pred_down_df   = pred_df[pred_down_pred]
  eff_up         = np.mean(pred_up_df['pctlead'])
  eff_down       = np.mean(pred_down_df['pctlead'])
  rpt_s += 'Naive-Bayes: Positive, Up,   effectiveness is '+str(eff_up)+'%\n'
  rpt_s += 'Naive-Bayes: Long-only effectiveness is '+str(np.mean(pred_df['pctlead']))+'%\n'
  rpt_s += 'Naive-Bayes: Negative, Down, effectiveness is '+str(eff_down)+'%\n'
  # I should report logistic regression (lr) now:
  # I should count
  tp_pred = (pred_df['accuracy_lr'] == 'True Positive')
  tn_pred = (pred_df['accuracy_lr'] == 'True Negative')
  fp_pred = (pred_df['accuracy_lr'] == 'False Positive')
  fn_pred = (pred_df['accuracy_lr'] == 'False Negative')
  tp_df   =  pred_df[tp_pred]
  tn_df   =  pred_df[tn_pred]
  fp_df   =  pred_df[fp_pred]
  fn_df   =  pred_df[fn_pred]
  tp_i = len(tp_df)
  tn_i = len(tn_df)
  fp_i = len(fp_df)
  fn_i = len(fn_df)
  rpt_s += 'For '+str(yr)+':\n'
  rpt_s += 'Logistic-Regression: Positive, Up,   Prediction Count is '+str(tp_i+fp_i)+'\n'
  rpt_s += 'Logistic-Regression: Negative, Down, Prediciton Count is '+str(tn_i+fn_i)+'\n'
  rpt_s += 'Logistic-Regression: Positive Accuracy is '+str(np.round(100*tp_i / (tp_i+fp_i)))+'%\n'
  rpt_s += 'Logistic-Regression: Negative Accuracy is '+str(np.round(100*tn_i / (tn_i+fn_i)))+'%\n'
  rpt_s += 'Logistic-Regression: Total Accuracy is '+str(np.round(100*(tp_i+tn_i)/(tp_i+fp_i+tn_i+fn_i)))+'%\n'
  # I should compute effectiveness
  pred_up_pred   = (pred_df['pdir_lr'] ==  1)
  pred_down_pred = (pred_df['pdir_lr'] == -1)
  pred_up_df     = pred_df[pred_up_pred]
  pred_down_df   = pred_df[pred_down_pred]
  eff_up         = np.mean(pred_up_df['pctlead'])
  eff_down       = np.mean(pred_down_df['pctlead'])
  rpt_s += 'Logistic-Regression: Positive, Up,   effectiveness is '+str(eff_up)+'%\n'
  rpt_s += 'Logistic-Regression: Long-only effectiveness is '+str(np.mean(pred_df['pctlead']))+'%\n'
  rpt_s += 'Logistic-Regression: Negative, Down, effectiveness is '+str(eff_down)+'%\n'
  myf_s = '_acc_eff'+str(yr)+'.erb'
  with open(myf_s, 'w') as myf:
    myf.write(rpt_s)
'bye'
