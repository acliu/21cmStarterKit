#!/bin/bash

for f in 3dboxes/*;
do
    mkdir tcf_${f:8:7} #making a new directory for the results
    
    #generating 200 noise realizations 
    #will be formated, for example:
    #   noisy_boxes_z006.00_1.txt
    #   noisy_boxes_z006.00_2.txt
    #   ...
    python noisy_boxes.py $f 
    
    var="${f:8:7}" #job name
    sbatch -J $var ./noise_array.sh $f #submitting job
done
