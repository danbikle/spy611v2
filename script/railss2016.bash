#!/bin/bash

# ~/spy611v2/script/railss2016.bash

# This script should start rails webserver on all interfaces which then listen on port 2016.

cd $HOME
cd spy611v2
bin/rails s -p 2016 -b 0.0.0.0
exit
