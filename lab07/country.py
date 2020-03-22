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
        self.name = name.title()
        if population < 0:
            print("A population cannot be negative!")
        else:
            self.population = population
        if area < 1:
            print("An area cannot be negative!")
        else:
            self.area = area

    def is_larger(self, country: object) -> bool:
        """
        Determine if the country is larger than another country.

        :param country: A country object.
        :precondition: The country param must be a properly formatted country object.
        :postcondition: The function will determine if the country is larger or not.
        :return: A boolean representing if the country is larger or not.
        """
        if self.area > country.area:
            return True
        else:
            return False

    def population_density(self) -> float:
        """
        Find the population density of the country.

        :precondition: The method is used on a properly formatted country object.
        :postcondition: The population density will be determined.
        :return: A float representing the population density in people/km^2
        """
        return self.population / self.area

    def __str__(self) -> str:
        """
        Return a detailed description of the country.

        :precondition: The country object must be properly formatted.
        :postcondition: The description will be properly returned.
        :return: A string representing the description of the country.
        """
        return self.name + " has a population of " + str(self.population) \
            + " and is " + str(self.area) + " square kilometres."

    def __repr__(self) -> str:
        """
        Return an informative line with the address of the country object.

        :precondition: The country object must be properly formatted.
        :postcondition: The information will be properly returned.
        :return: A string showing the object's address.
        """
        return "Country(\"" + self.name + "\", " + str(self.population) + ", " + str(self.area) + ")"
