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
