"""Represent a country."""


class Country:

    def __init__(self, name: str, population: int, area: int):
        """
        Initialize a new country.

        :param name: A string representing the country's name.
        :param population: An int representing the country's population.
        :param area: An int representing the country's area in square kilometres.
        :precondition: The data-types of the params are followed and area/population are > 0.
        :postcondition: A country object will be initialized.
        """
        self.name = name
        if population < 0:
            print("A population cannot be negative!")
        else:
            self.population = population
        if area < 0:
            print("An area cannot be negative!")
        else:
            self.area = area

    def is_larger(self, country):
        if self.area > country.area:
            return True
        else:
            return False

    def population_density(self):
        return self.population / self.area

    def __str__(self):
        return self.name + " has a population of " + str(self.population) \
               + " and is " + str(self.area) + "square kilometres."

    def __repr__(self):
        return "<lab07_country.Country object at " + str(self.id())
