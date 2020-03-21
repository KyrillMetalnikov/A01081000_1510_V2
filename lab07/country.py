"""Represent a country."""


class Country:

    def __init__(self, name, population, area):
        self.name = name
        if population < 0:
            print("A population cannot be negative!")
        else:
            self.population = population
        if area < 0:
            print("An area cannot be negative!")
        else:
            self.area = area

    def population_density(self):
        return self.population / self.area

    def __str__(self):
        return self.name + " has a population of " + str(self.population) \
               + " and is " + str(self.area) + "square kilometres."

