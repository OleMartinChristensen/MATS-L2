#! /bin/bash

source ~/.bashrc

function replace_variables () {
    sed "s=NT=$1=;" ${HOME}/src/poem/scripts/mats.sh
}

replace_variables 2  | sbatch
replace_variables 4  | sbatch
replace_variables 8  | sbatch
replace_variables 12 | sbatch
replace_variables 16 | sbatch
replace_variables 20 | sbatch
replace_variables 24 | sbatch
replace_variables 28 | sbatch
replace_variables 32 | sbatch
