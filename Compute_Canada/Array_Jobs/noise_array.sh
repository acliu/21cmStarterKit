#!/bin/bash

#SBATCH --time=00:25:00
#SBATCH --nodes=3
#SBATCH --mem=0
#SBATCH --array=1-200

f=$1 #reading filename

echo tcf_noise_$f_$SLURM_ARRAY_TASK_ID.txt | mpiexec -n 70 python triangleCorrelation.py