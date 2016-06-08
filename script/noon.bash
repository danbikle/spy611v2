#!/bin/bash

# ~/spy611v2/script/noon.bash

# I should run this at 12:50 Calif time.

# Demo:
# ${HOME}/spy611v2/script/dan.bash ./noon.bash

export     SPY611=${HOME}/spy611v2
mkdir -p ${SPY611}/public/csv/
cd       ${SPY611}/public/csv/

# I should get prices
${SPY611}/script/wgetGSPC.bash

# I should generate features from prices:
${HOME}/anaconda3/bin/python ${SPY611}/script/genf.py GSPC2.csv

# I should generate training and test data from features.

# Next I generate training data CSV files:
rm -rf   /tmp/ddata/
mkdir -p /tmp/ddata/
cd       /tmp/ddata/
cp ${SPY611}/public/csv/ftrGSPC2.csv /tmp/ddata/
STARTYR=2016
ENDYR=2016
${HOME}/anaconda3/bin/python ${SPY611}/script/gentrain_test.py ftrGSPC2.csv 30 $STARTYR $ENDYR

# I should learn then test
${HOME}/anaconda3/bin/python ${SPY611}/script/train_test.py $STARTYR $ENDYR
# Now I should have CSV files with predictions mixed with actual results.

# I should now have an erb file in /tmp/ddata/
cp /tmp/ddata/_predictions.erb ${SPY611}/public/
# I should enhance the table-element:
${SPY611}/script/sed_pred.bash

# I should (not) copy new data,files to heroku,gh,bit
cd $SPY611
# script/git_push.bash

exit
