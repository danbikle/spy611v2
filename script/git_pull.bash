#!/bin/bash

# git_pull.bash

# This script should do a simple git pull from github, bit, heroku.
# I intend for this to run from cron twice a day.
export  SPY611=${HOME}/spy611
cd     $SPY611
git pull gh     master
git pull bit    master
git pull heroku master
exit
