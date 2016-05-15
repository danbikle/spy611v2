#!/bin/bash

# dan.bash

# This script should help me pass env variables to cron scripts.

# cron Demo:
# 59 03 * * tue,wed,thu,fri,sat /home/r5/spy611v2/script/dan.bash night.bash > /tmp/night_bash.txt 2>&1

if [ -e ${HOME}/.rbenv ]; then
  export PATH="${HOME}/.rbenv/bin:$PATH"
  eval "$(rbenv init -)"
fi

if [ -e ${HOME}/jdk/bin ]; then
  export JAVA_HOME=${HOME}/jdk
  export PATH="${JAVA_HOME}/bin:${PATH}"
fi

if [ -e ${HOME}/heroku-client/bin ]; then
  export PATH="${HOME}/heroku-client/bin:${PATH}"
fi

if [ -e ${HOME}/anaconda3/bin ]; then
  export PATH="${HOME}/anaconda3/bin:$PATH"
fi

export SPY611=${HOME}/spy611v2
cd   ${SPY611}/script/

env|sort

$@

exit


