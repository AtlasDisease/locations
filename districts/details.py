class Population:
    def __init__(self, population: int = 0):

        self.population = population

    def __str__(self):
        return f"{self.population: ,}"
