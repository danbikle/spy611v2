#!/bin/bash

# git_push.bash

# This script should push data,files to gh,bit,heroku.

# I like to pull before I push.
git pull gh master
git pull bit master
git pull heroku master
git add .
git commit -am git_push.bash.commit
git push gh master
git push bit master
git push heroku master
exit
