#!/bin/bash

# ~/spy611/script/noon_dan.bash

# I should run this at 12:50 Calif time.

# Demo:
# ${HOME}/spy611/script/dan.bash ./noon.bash

export     SPY611=${HOME}/spy611

cd $SPY611
script/git_pull.bash

mkdir -p ${SPY611}/public/csv/
cd       ${SPY611}/public/csv/

# I should get prices
${SPY611}/script/wgetGSPC.bash
exit

# I should generate features from prices:
${HOME}/anaconda3/bin/python ${SPY611}/script/genf.py GSPC2.csv

# I should generate training and test data from features.

# Next I generate training data CSV files:
rm -rf   /tmp/ddata/
mkdir -p /tmp/ddata/
cd       /tmp/ddata/
cp ${SPY611}/public/csv/ftrGSPC2.csv /tmp/ddata/
STARTYR=2017
ENDYR=2017
${HOME}/anaconda3/bin/python ${SPY611}/script/gentrain_test.py ftrGSPC2.csv 30 $STARTYR $ENDYR

# I should learn then test
${HOME}/anaconda3/bin/python ${SPY611}/script/train_test.py $STARTYR $ENDYR
# Now I should have CSV files with predictions mixed with actual results.

# I should now have an erb file in /tmp/ddata/
cp /tmp/ddata/_predictions.erb ${SPY611}/public/
# I should enhance the table-element:
${SPY611}/script/sed_pred.bash


cd $SPY611
script/git_push.bash

exit
