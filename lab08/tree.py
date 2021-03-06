class Tree:

    def __init__(self, species: str, age: int, circumference: float):
        """
        Initialize a new tree.

        :param species: A string representing the species of the tree.
        :param age: An integer of the tree's age in years.
        :param circumference: A float of the circumference of the tree's trunk in centimetres.
        :precondition: Species cannot be empty or white space, and age and circumference must be positive.
        :postcondition: A new tree object will properly be initialized.
        :raise ValueError: If preconditions aren't met.
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

    def get_species(self) -> str:
        """
        Return the trees species.

        :precondition: Only use this with a properly formatted tree object.
        :postcondition: The trees species will be correctly returned.
        :return: A string representing the tree's species.

        >>> tree1 = Tree("Oak", 2, 2.0)
        >>> tree1.get_species()
        'Oak'
        """
        return self.__species

    def get_age(self) -> int:
        """
        Return the trees age.

        :precondition: Only use this with a properly formatted tree object.
        :postcondition: The trees age will be correctly returned.
        :return: An integer representing the tree's age in years.

        >>> tree1 = Tree("Oak", 2, 2.0)
        >>> tree1.get_age()
        2
        """
        return self.__age

    def get_circumference(self) -> float:
        """
        Return the trees circumference.

        :precondition: Only use this with a properly formatted tree object.
        :postcondition: The trees circumference will be correctly returned.
        :return: A float representing the tree's circumference in centimetres.

        >>> tree1 = Tree("Oak", 2, 2.0)
        >>> tree1.get_circumference()
        2.0
        """
        return self.__circumference

    def set_age(self, age):
        """
        Set the age of a tree.

        :param age: An integer representing the tree's age in years.
        :precondition: Age must be a positive integer.
        :postcondition: The tree's age will be properly set.
        >>> tree1 = Tree("Oak", 2, 2.0)
        >>> tree1.set_age(4)
        >>> tree1.get_age()
        4
        """
        if age < 0:
            print("Error: age cannot be a negative number.")
        else:
            self.__age = age

    def set_circumference(self, circumference: float):
        """
        Set the circumference of a tree.

        :param circumference: A float representing the circumference of the tree in centimetres.
        :precondition: Circumference must be a positive float.
        :postcondition: The tree's age will be properly set.

        >>> tree1 = Tree("Oak", 2, 2.0)
        >>> tree1.set_circumference(4.0)
        >>> tree1.get_circumference()
        4.0
        """
        if circumference < 0:
            print("Error: circumference cannot be a negative number.")
        else:
            self.__circumference = circumference

    def __str__(self) -> str:
        """
        Display the object with all attributes.

        :precondition: Only use this with a properly formatted tree object.
        :postcondition: The trees attributes will be properly displayed.
        :return: A string with all the tree's attributes.

        >>> tree1 = Tree("Oak", 2, 2.0)
        >>> print(tree1)
        Tree('species = Oak', age = 2, circumference = 2.0)
        """
        return f"Tree('species = {self.__species}', age = {self.__age}, circumference = {self.__circumference})"

    def __repr__(self) -> str:
        """
        Return a descriptive version of the object.

        :precondition: Only use this with a properly formatted tree object.
        :postcondition: The trees attributes will be properly displayed.
        :return: A string with all the tree's attributes.
        >>> tree1 = Tree("Oak", 2, 2.0)
        >>> tree1.__repr__()
        "Tree('species = Oak', age = 2, circumference = 2.0)"
        """
        return f"Tree('species = {self.__species}', age = {self.__age}, circumference = {self.__circumference})"
