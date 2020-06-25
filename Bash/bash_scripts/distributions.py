import numpy as np 

def main():
    '''generates a bunch of .txt files with different distributions'''
    poisson = np.random.poisson(size = 2000)
    gaussian = np.random.normal(size = 2000)
    pareto = np.random.pareto(3, size = 2000)

    np.savetxt('poisson_distribution_2000_datapoints.txt', poisson, delimiter=',')
    np.savetxt('gaussian_distribution_2000_datapoints.txt', gaussian, delimiter=',')
    np.savetxt('pareto_distribution_2000_datapoints.txt', pareto, delimiter=',')

if __name__ == "__main__":
    main()

