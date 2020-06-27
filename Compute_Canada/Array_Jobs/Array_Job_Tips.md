# Array Jobs

Joelle Begin, June 2020

Sometimes, you need to run the same code many times, but tweaking some parameters each time. 

## Basic array job

The flag for an array job in your script will be

```bash
#SBATCH --array=1-10
```

Basically, once you do 

```
$ sbatch array_job.sh
```

where `array_job.sh` contains the above flag, 10 jobs will be run on the same script. For example, if `array_job.sh` is the following: 

```bash
#!/bin/bash
#SBATCH --time=00:00:01
#SBATCH --nodes=1
#SBATCH --mem=0=1G
#SBATCH --array=1-5

echo $SLURM_ARRAY_TASK_ID
```

Here the variable `$SLURM_ARRAY_TASK_ID` is what differentiates one job from the other. Once you `sbatch` this script, five jobs will be submitted. You can check in the `slurm` files for the output. `slurm-ID_1.out` will contain `1`, since our job prints the array ID. `slurm-ID_2.out` will contain `2`, and etc.

So say I want to run a python script for a bunch of different inputs. I would format my directory like 

```
project
|
|   script.py
|   array_job.sh
|   input_1.txt
|   input_2.txt 
|   input_3.txt
|   input_4.txt
|   input_5.txt
|
```

and now my job script would look like


```bash
#!/bin/bash
#SBATCH --time=00:00:01
#SBATCH --nodes=1
#SBATCH --mem=0=1G
#SBATCH --array=1-5

echo input_$SLURM_ARRAY_TASK_ID.txt | python script.py
```

And so when you `sbatch` this job, you'll run the script on all the input files you need!

# A more involved example

I've included some scripts that execute a more complicated operation, so only read this if you want to learn some cool tricks. All you need to know to run a basic array job is above!

## run.sh 

This happened to be a bit of a complicated thing I was running (I was doing some noise Monte Carlo), where for every file in the directory `3dboxes` I had to submit a _separate_ array job. The file structure was like this:

```
project
|
│   run.sh
|   noise_array.sh
│   triangleCorrelation.py    
│
└───3dboxes
│   │   z006.00_nf0.004340.txt
│   │   z006.50_nf0.096743.txt
│   │   ...
```

where the files in `3dboxes` are 21cmfast simulations. 

So, in run.sh, first we we loop through every file in 3dboxes.

```
3 for f in 3dboxes/*;
```

Then, if we were to `echo $f`, it would print `3dboxes/z006.00_nf0.004340.txt` for example. So `${f:8:7}` is in this case `z006.00`. This is useful to keep track of which file we're doing the operation on! 

In line 6, we generate 200 noise iterations based on this specific box. 

In lines 7-8 is a cool trick I learned in case you want to be able to name your job. Doing `$ sbatch -J $var ./job.sh` makes it so that in the squeue, the job you just submitted will be called `$var`! 


## noise_array.sh 

I've stripped this down to the bare minimum for clarity. This script will read the filename (line 8), and run the 200 different noise realizations through the relevant script. 

So, with just two bash scripts, we've run 200 different jobs for every single file in `3dboxes`! 

# Final thoughts 

With array jobs, what I've found the most important is _organization_. Make sure you format the input and output properly, such that the results of one of the array jobs won't delete the results of the others. 

Array jobs are extremely useful when used properly, and can save a _lot_ of time. As with a lot of things, I learned this by googling around so if anyone finds a better way to do things, please add it to this directory!