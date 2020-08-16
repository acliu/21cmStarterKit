"""
Simple example of use emcee to fit a linear data set with gaussian error bars.

By Emma Klemets, modified from Adrian Liu's code and extensively commented, which is from https://emcee.readthedocs.io/en/stable/tutorials/line/. 
July 2020
"""

#imports
import numpy as np
import corner #to make triangle plots
import emcee
import matplotlib.pyplot as plt

#first we need to set up the function that we are fitting
#theta is the parameter vector, so theta = [a, b]

#we are fitting for 2 parameters: a, b
def log_likelihood(theta, x, y, yerr):
    a, b = theta
    model = a * x + b
    sigma2 = yerr ** 2
    return -0.5 * np.sum((y - model) ** 2 / sigma2 + np.log(sigma2))

#removes any values outside of set bounds for a and b
def log_prior(theta):
    a, b = theta
    if -1.0 < a < 5. and -5. < b < 5.:
        return 0.0 # the constant doesn't matter since MCMCs only care about *ratios* of probabilities
    return -np.inf # log(0) = -inf

#log posterior
def log_post(theta, x, y, yerr):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, x, y, yerr)


#data to fit
x_vals = np.linspace(-10, 10, 15)
y_vals = 2*x_vals + 3 + np.random.normal(0.7, 2, len(x_vals))
#errs = np.random.normal(0.1, 1, len(x_vals))
errs = np.ones_like(x_vals)


num_iter = 3000 # number of iterations, or steps that the walkers take
ndim = 2 # number of parameters we are fitting
nwalkers = 32 # number of walkers

#set a guess for each parameter, here a = 1, b = 4
guess = np.array((1, 4)) 

#initial position of walkers, taken as a small perturbation from the intial guess
initial_pos = guess + 0.01 * np.random.randn(nwalkers, ndim) 

# create type of MCMC that uses a whole ensemble of walkers
# passing it: number of walkers, number of parameters, log probability function and data to fit
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_post, args=(x_vals, y_vals, errs))

# run the MCMC!
sampler.run_mcmc(initial_pos, num_iter, progress=True)


#### Look at results ####

#get the chain the MCMC created
samples = sampler.get_chain()

#make a trace plot for each parameter
f, axes = plt.subplots(2, figsize=(10, 7), sharex=True)
samples = sampler.get_chain()
labels = ["a", "b"]
for i in range(ndim):
    ax = axes[i]
    ax.plot(samples[:, :, i], alpha=0.3)
    ax.set_xlim(0, len(samples))
    ax.set_ylabel(labels[i])

axes[-1].set_xlabel("Step number")
f.suptitle('Trace Plots')
plt.show()

#Combine the chains from all the walkers into one chain while discarding the first 
#100 steps as burn-in steps, and thinning the chain by taking only one out of every 15 steps:
flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)

#make a triangle plot
fig = corner.corner(flat_samples, labels=labels, quantiles=[0.16, 0.5, 0.84])
fig.suptitle('Triangle Plot')
plt.show()

#plot a sample of the function the parameter values result in and compare to the data
inds = np.random.randint(len(flat_samples), size=100)
x0 = np.linspace(-10, 10., 50)
f, ax = plt.subplots(figsize=(6,4))

for ind in inds:
    sample = flat_samples[ind]
    ax.plot(x0, sample[0] * x0 + sample[1], alpha=0.05, color='red')
    
ax.errorbar(x_vals, y_vals, yerr=errs, linestyle = 'None',capsize=4, marker ='o', color='black', ms=8, label="data")
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.legend()
ax.set_title("Data and sample parameters fits")
plt.show()

# to look at the acceptance fraction for each walker - for this code it is quite high as the data is pretty nice
# print(sampler.acceptance_fraction)
# overall average acceptance fraction
# print(np.mean(sampler.acceptance_fraction))