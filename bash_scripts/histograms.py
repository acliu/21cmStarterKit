import matplotlib.pyplot as plt 
import numpy as np 

def main():
    file_loc = input()
    data = np.loadtxt(file_loc, delimiter = ',')

    fig, ax = plt.subplots()
    ax.hist(data, density = True)

    plt.savefig(file_loc + '.png')

if __name__ == "__main__":
    main()

    