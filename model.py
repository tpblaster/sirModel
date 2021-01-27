from pandas import DataFrame


class SIRModel:
    removal_rate: float
    infectivity_rate: float
    data: DataFrame

    def __init__(self, base_susceptible_pop: int, base_infected_pop: int, simulation_length: int, removal_rate: float, infectivity_rate: float):
        self.removal_rate = removal_rate
        self.infectivity_rate = infectivity_rate
        self.data = DataFrame.from_dict({
            "Susceptible Population": [float(base_susceptible_pop)],
            "Infected Population": [float(base_infected_pop)],
            "Recovered Population": [0.0]
        })
        for x in range(0, simulation_length):
            self.data.loc[x+1] = [
                (self.data.at[x, "Susceptible Population"] - (self.infectivity_rate * self.data.at[x, "Infected Population"] * self.data.at[x, "Susceptible Population"])),
                (self.data.at[x, "Infected Population"] + (self.infectivity_rate * self.data.at[x, "Infected Population"] * self.data.at[x,"Susceptible Population"]) - (self.removal_rate * self.data.at[x, "Infected Population"])),
                (self.data.at[x, "Recovered Population"] + (self.removal_rate * self.data.at[x, "Infected Population"]))
            ]
