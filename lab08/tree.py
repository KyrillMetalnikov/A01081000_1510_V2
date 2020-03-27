class Tree:

    def __init__(self, species: str, age: int, circumference: float):
        """
        Initialize a new tree.

        :param species: A string representing the species of the tree.
        :param age: An integer of the tree's age in years.
        :param circumference: A float of the circumference of the tree's trunk in centimetres.
        """
        if species.strip() == "":
            raise ValueError("Please input a proper species name")
        else:
            self.__species = species.strip().title()
        if age < 0:
            raise ValueError("Trees cannot have negative ages.")
        else:
            self.__age = age
        if circumference < 0:
            raise ValueError("With the current laws of physics, tree's cannot have a negative circumference.")
        else:
            self.__circumference = circumference

    def get_species(self):
        return self.__species

    def __str__(self):
        return f"Tree('{self.species}', {self.age}, {self.__circumference}