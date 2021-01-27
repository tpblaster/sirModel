from model import SIRModel
import matplotlib.pyplot as plt

if __name__ == '__main__':
    run = SIRModel(base_susceptible_pop=763, base_infected_pop=1, simulation_length=14, removal_rate=0.476, infectivity_rate=0.00234)
    plt.figure()
    run.data.plot()
    plt.legend(loc='best')
    plt.show()