# Parallel Computing intro 

Joelle Begin, June 2020

So, you've run into the issue we all eventually run into at some point... your code is too slow! You've done some runtime analysis, and realize that it will take two days to run once. Well, the first thing you should do is make sure you're not doing anything silly. Can you get rid of some loops? Refactor the code in some more efficient way? 

Alas, sometimes there really isn't anything you can do; some code just requires _a lot_ of computational power. And that's ok! We have ways to deal with that; namely, parallel computing. 

Most modern day CPUs have many processors; these are independent little computers that are busy all the time doing tasks for your operating system and whatever applications you're running. If you don't do anything about it, a python script will just take whatever processor isn't busy at the time. It'll always just run one processor at once. 

This is where parallel processing comes in handy; you tell your code to use all of the processors it has available, and that way you take full advantage of your computer's power! 

There are many ways of doing this: my favourite is the MPI protocol, for which there is an example script in this directory. There is also the `multiprocessing` python package which seems to be popular, but I feel like MPI really lets you see what's going on under the hood which I like. 

## "Embarrassingly" parallelizable problems

These are the class of problems you'll (hopefully) be dealing with. An embarrassingly parallelizable problem is one where every task is independent. That is, you have for example some array of numbers to do something to, but whatever `array[0]` is after the operation doesn't affect what `array[1]` is after the operation. 

The example script included is an embarrassingly parallelizable problem. 

