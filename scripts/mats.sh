#!/usr/bin/env bash
#SBATCH -A C3SE2019-1-15 -p vera
#SBATCH -n NT
#SBATCH -c 2
#SBATCH -J MATS
#SBATCH -t 0-1:00:00

cd ${HOME}/src/poem/test
source ..ops/setup_vera.sh
export OMP_NUM_THREADS=NT

python mats.py
