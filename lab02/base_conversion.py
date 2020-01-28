"""
Convert various numbers from base 10 to another base
"""


def base_conversion():
    """
      Convert a base 10 number to another base up to 4 digits.

      A user inputs a base between 2-9 then the program converts the input into an integer and displays the max number
      possible for the conversion.  The user then inputs a number within allowed parameters which gets converted then
      the resulting conversion is displayed to the user.
    """
    base = int(input("What base (2-9) do you want to convert to?"))  # inputted base converts to int and is then stored
    print("The max value allowed is ", max_value(base))
    number_base_10 = int(input("Please input the base 10 integer you wish to convert"))  # inputted num is stored as int
    print(base_converter(number_base_10, base))


def max_value(base):
    """
    Find the max possible value in a base conversion.

    Function uses an algorithm find the maximum value the conversion can hold when moving from base 10 using 4 digits

    :param base: the base being converted to: type integer
    :return: returns the max value the base can be converted to assuming there's 4 digits
    """
    return base ** 4 - 1


def base_converter(number_base_10, base):
    """
    Convert a number from base 10 to target base.

    Function uses an algorithm to convert a number from base 10 to a target base up to 4 digits

    :param number_base_10: the number in base 10 being converted: type integer
    :param base: the target base being converted to: type base
    :return: returns the 4 digits the base 10 number was converted to
    """

    num0 = number_base_10 // base
    digit0 = str(number_base_10 % base)

    num1 = num0 // base
    digit1 = str(num0 % base)

    num2 = num1 // base
    digit2 = str(num1 % base)

    digit3 = str(num2 % base)
    return digit3 + digit2 + digit1 + digit0


if __name__ == "__main__":
    base_conversion()
