## Intro to Running an MCMC with emcee.  
Emma Klemets, July 2020  

emcee is a Python package built for running MCMCs.  
Note, these instructions and the example Running_a_MCMC.py are made to be run on emcee 3.0.2, and there are some commands that do not function on versions < 3.  
https://emcee.readthedocs.io/en/stable/  

#### Basic Theory  

MCMCs are used to sample a probability distribution and obtain it's shape without requiring the computational power to calculate every value in in the distribution. As we are often fitting for more than more parameter, and each parameter has it's own probability distribution, the total parameter space can very quickly become very large with muliple parameters.
The main algorithm is to use 'walkers' that move around the parameter space from a starting point and take a sample at each step, and these positions in parameter space corresponding probability values get recorded in a chain for each walker. Then a method is used to decide if the next randonly selected step should be taken, usually based on it's probability compared to the current position and the data being fitted.  

#### Metropolis–Hastings algorithm  
A common way of deciding what the next step for a walker is uses the Metropolis–Hastings algorithm.  
After drawing a new proposed new step randomly out of a proposal distribution, an acceptance ratio is calculated. This ratio is the proposed step's probability divided by the current position's probability. If the ratio is greater than 1, the proposed step is taken, if it's less than 1, a number is drawn from a uniform distribution between (0, 1) and if the ratio is greater than that it is taken. If the step is rejected, then the process is repeated until a new step is taken.  

The acceptance fraction is the fraction of proposed steps that are taken. If this fraction is too high, the steps are too careful and small; if it's too low, the steps are too big. The rule of thumb is a acceptance fraction ~0.25-0.5.  
