import doctest
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

    def get_name(self):
        """
        Return the Country's name.

        :precondition: Use this only on a properly initialized country object.
        :postcondition: The country's name will be returned.
        :return: A string representing the name of the country.

        >>> canada = Country("Canada", 12345, 1234)
        >>> canada.get_name()
        'Canada'
        >>> denmark = Country("Denmark", 123, 12)
        >>> denmark.get_name()
        'Denmark'
        """
        return self.__name

    def get_population(self):
        """
        Return the Country's population.

        :precondition: Use this only on a properly initialized country object.
        :postcondition: The country's population will be returned.
        :return: An integer representing the population of the country.

        >>> canada = Country("Canada", 12345, 1234)
        >>> canada.get_population()
        12345
        >>> denmark = Country("Denmark", 123, 12)
        >>> denmark.get_population()
        123
        """
        return self.__population

    def get_area(self):
        """
        Return the Country's area.

        :precondition: Use this only on a properly initialized country object.
        :postcondition: The country's area will be returned.
        :return: An integer representing the area of the country.

        >>> canada = Country("Canada", 12345, 1234)
        >>> canada.get_area()
        1234
        >>> denmark = Country("Denmark", 123, 12)
        >>> denmark.get_area()
        12
        """
        return self.__area

    def is_larger(self, country: object) -> bool:
        """
        Determine if the country is larger than another country.

        :param country: A country object.
        :precondition: The country param must be a properly formatted country object.
        :postcondition: The function will determine if the country is larger or not.
        :return: A boolean representing if the country is larger or not.

        >>> canada = Country("Canada", 12345, 1234)
        >>> denmark = Country("Denmark", 123, 12)
        >>> canada.is_larger(denmark)
        True
        >>> canada = Country("Canada", 12345, 1234)
        >>> denmark = Country("Denmark", 123, 12)
        >>> denmark.is_larger(canada)
        False
        >>> canada = Country("Canada", 12345, 1234)
        >>> denmark = Country("Denmark", 123, 1234)
        >>> canada.is_larger(denmark)
        False
        """
        if self.get_area() > country.get_area():
            return True
        else:
            return False

    def population_density(self) -> float:
        """
        Find the population density of the country.

        :precondition: The method is used on a properly formatted country object.
        :postcondition: The population density will be determined.
        :return: A float representing the population density in people/km^2.

        >>> canada = Country("Canada", 1234, 1234)
        >>> canada.population_density()
        1.0
        >>> canada = Country("Canada", 2468, 1234)
        >>> canada.population_density()
        2.0
        >>> canada = Country("Canada", 1500, 1000)
        >>> canada.population_density()
        1.5
        """
        return self.get_population() / self.get_area()

    def __str__(self) -> str:
        """
        Return a detailed description of the country.

        :precondition: The country object must be properly formatted.
        :postcondition: The description will be properly returned.
        :return: A string representing the description of the country.
        """
        return self.get_name() + " has a population of " + str(self.get_population()) \
            + " and is " + str(self.get_area()) + " square kilometres."

    def __repr__(self) -> str:
        """
        Return an informative line with the address of the country object.

        :precondition: The country object must be properly formatted.
        :postcondition: The information will be properly returned.
        :return: A string showing the object's address.

        >>> canada = Country("Canada", 1234, 1234)
        >>> canada
        Country("Canada", 1234, 1234)
        >>> canada = Country("Canada", 1234, 1234)
        >>> [canada]
        [Country("Canada", 1234, 1234)]
        """
        return "Country(\"" + self.get_name() + "\", " + str(self.get_population()) + ", " + str(self.get_area()) + ")"


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
