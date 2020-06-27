#!/bin/bash
#SBATCH --account=def-acliu
#SBATCH --time=0-1:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=24
#SBATCH --mail-user=<henri.lamarre@mail.mcgill.ca>
#SBATCH --mail-type=ALL
#SBATCH --mem=0

mpirun -np 48 python file.py
