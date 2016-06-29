#!/bin/bash

# sed_pred.bash

# This script should enhance the table in ${SPY611}/public/_predictions.erb

# This script should be called by:
# ${SPY611}/script/noon.bash
# ${SPY611}/script/night.bash

# Demo:
# export SPY611=${HOME}/spy611v2
# ${SPY611}/script/sed_pred.bash

PERBF=${SPY611}/public/_predictions.erb
sed -i  1d          $PERBF
sed -i '1i <table>' $PERBF
sed -i '/cdate/s/cdate/Date/'    $PERBF
sed -i '/cp/s/cp/Closing Price/' $PERBF
sed -i '/pctlag1/s/pctlag1/Pct. Lag 1Day/'  $PERBF
sed -i '/pctlead/s/pctlead/Pct. Lead 1Day is Effectiveness 1Day(Long Only)/' $PERBF
sed -i '/actual_dir/s/actual_dir/Actual Direction/'   $PERBF
sed -i '/prob_lr/s/prob_lr/Positive Probability(LR)/' $PERBF
sed -i '/pdir_lr/s/pdir_lr/Predicted Direction(LR)/'  $PERBF
sed -i '/pdir_nb/s/pdir_nb/Predicted Direction(NB)/'  $PERBF
sed -i '/accuracy_lr/s/accuracy_lr/Accuracy(LR)/'     $PERBF
sed -i '/accuracy_nb/s/accuracy_nb/Accuracy(NB)/'     $PERBF
sed -i '/eff1d_lr/s/eff1d_lr/Effectiveness 1Day(LR)/' $PERBF
sed -i '/eff1d_nb/s/eff1d_nb/Effectiveness 1Day(NB)/' $PERBF

exit

