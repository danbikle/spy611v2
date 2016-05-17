#!/bin/bash

# ~/spy611v2/script/night.bash

# I should run this at night after daily closing price has been published.

# Demo:
# ${HOME}/spy611v2/script/dan.bash ./night.bash

export     SPY611=${HOME}/spy611v2
mkdir -p ${SPY611}/public/csv/
cd       ${SPY611}/public/csv/

# I should get prices
${SPY611}/script/wgetGSPCnight.bash

# I should generate features from prices:
${HOME}/anaconda3/bin/python ${SPY611}/script/genf.py GSPC2.csv

# I should generate training and test data from features.

# Next I generate training data CSV files:
rm -rf   /tmp/ddata/
mkdir -p /tmp/ddata/
cd       /tmp/ddata/
cp ${SPY611}/public/csv/ftrGSPC2.csv /tmp/ddata/
STARTYR=1981
ENDYR=2016
${HOME}/anaconda3/bin/python ${SPY611}/script/gentrain_test.py ftrGSPC2.csv 30 $STARTYR $ENDYR

# I should learn then test
${HOME}/anaconda3/bin/python ${SPY611}/script/train_test.py $STARTYR $ENDYR
# Now I should have CSV files with predictions mixed with actual results.

# I should report accuracy and effectiveness from CSV files in /tmp/ddata/
${HOME}/anaconda3/bin/python   ${SPY611}/script/acc_eff.py $STARTYR $ENDYR
mkdir -p                       ${SPY611}/public/acc_eff/
cp -p /tmp/ddata/_acc_eff*.erb ${SPY611}/public/acc_eff/

# I should visualize the predictions:
${HOME}/anaconda3/bin/python ${SPY611}/script/rgb.py $STARTYR $ENDYR
exit
