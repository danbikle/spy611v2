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

# I should generate training data from features.

# I should generate test     data from features.

# I should learn then test

# I should visualize the predictions:

exit
