#!/bin/bash

python distributions.py

for f in *.txt
do 
    echo ${f%%_*} #cuts filename to str before _
    mkdir ${f%%_*}_data #makes dirs
    mv $f ${f%%_*}_data
done

#you can do other fun things with strings in bash, like slicing.
#${f:0:15} would return the string $f from the first char to the 15th.
#useful if you have to make directories depending on file names!

mkdir plots 

for d in *_data 
do 
    for f in ${d}/*.txt 
    do 
        echo ${f} | python histograms.py
    done

    mv ${d}/*.png plots 
done

