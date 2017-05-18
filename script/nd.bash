#!/bin/bash

# ~/spy611/script/night_dan.bash

# I should run this at night after daily closing price has been published.

# Demo:
# ${HOME}/spy611/script/dan.bash ./night.bash

export     SPY611=${HOME}/spy611

cd $SPY611
script/git_pull.bash

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
ENDYR=2017
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
cp /tmp/ddata/plot*.png ${SPY611}/public/img/

# I should now have an erb file in /tmp/ddata/
cp /tmp/ddata/_predictions.erb ${SPY611}/public/
# I should enhance the table-element:
${SPY611}/script/sed_pred.bash

# I should capture all the predictions:
head -1 rgb_df2017.csv                 > allrgb.csv
cat rgb_df*csv | sort | grep -v cdate >> allrgb.csv
cp allrgb.csv ${SPY611}/public/csv/

# I should (not) copy new data,files to heroku,gh,bit
cd $SPY611
script/git_push.bash

exit

