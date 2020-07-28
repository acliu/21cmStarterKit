Hi friends! 

The purpose of this repo is for us to have a place where we can put instructive resources. Hopefully, this way whenever someone is starting to delve into a new challenge (Compute Canada, parallel programming, bash scripts, etc) they have many helpful documents available! 

-Joelle

# Submission instructions 

- **Organization**: 
    * If you're submitting a new tutorial or document, first check if there are any existing subdirectories where it can go. Else, create a new subdirectory!
    * Please make sure not to do `git add .` or something similar; we don't wan't random files like `__pycache__` or `.DS_store` floating around.
- **Author statement**: Don't forget to put your name and date at the top of the document.
- **Table of Contents**: Once you're done, add a section to the table of contents briefly explaining your document.
- **Closing issues**: If your document resolves an issue, include something like "closes #10" in your pull request, which will automatically resolve the issue when it's merged. 

# **Table of contents** 

- [Bash](#bash)
- [Compute Canada](#compute-canada)
    * [Slurm Tips](#ComputeCanada_Slurm_tips.txt)
    * [Template script](#template_job_script.sh)
    * [GPUs](#GPUs_on_Compute_Canada.pdf)
    * [Array Jobs](#array_jobs)
- [Parallel Computing](#parallel-computing)
- [MCMCs with emcee](#MCMCs-with-emcee)

## Bash

Here you'll find a basic intro to bash, as well as some sample bash scripts in the subdirectory 
`bash_scripts`

## Compute Canada

Resources for getting started with the Compute Canada supercomputers!

### ComputeCanada_Slurm_tips.txt

- An introduction to everything Compute Canada, from setting up your .bashrc and python environment, to submitting your first job.

### template_job_script.sh

- A template job script that contains most of the flags you need to include when you `sbatch` a job. 

### GPUs_on_Compute_Canada.pdf

- A guide to using GPUs on Compute Canada. 

### Array_Jobs

- Guide and sample scripts for running array jobs. 

## Parallel Computing

An introduction to parallel computing, and a template for parallelizing jobs with the MPI protocol. 

## Using Gumdrop

A guide for accessing and using Gumdrop. 


## MCMCs with emcee

An introduction to running MCMCs with emcee, basic code for fitting and tips on how to look at results.
