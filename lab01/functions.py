"""

"""


def format_name(first_name, last_name):
    """
    Format a full name.

    User inputs a fullname and the function removes white space, sets to title case, and strings the two together
    """
    return first_name.strip().title() + " " + last_name.strip().title()



def tripler(parameter):
    """
    Triples whatever parameter is entered.
    """
    return str(parameter) * 3


def this_year():
    """
    No parameter function: just returns 2020.
    """
    jenny = 8675309  # call jenny
    sound_of_music = 16  # sixteen going on seventeen
    summer = 69  # bryan adams
    minutes_to_save_world = 4  # madonna
    project = 56  # deadmau5
    year = jenny / (sound_of_music * summer * minutes_to_save_world) + project
    return int(year)



def base_conversion():
    """
      Convert a base 10 number to another base up to 4 digits.

      A user inputs a base between 2-9 then the program converts the input into an integer and displays the max number
      possible for the conversion.  The user then inputs a number within allowed parameters which gets converted then
      the resulting conversion is displayed to the user.
    """
    base = int(input("What base (2-9) do you want to convert to?"))  # inputted base converts to int and is then stored
    max_number = base ** 4 - 1
    print("The max value allowed is " + str(max_number))
    number_base_10 = int(input("Please input the base 10 integer you wish to convert"))  # inputted num is stored as int

    num0 = number_base_10 // base
    digit0 = str(number_base_10 % base)

    num1 = num0 // base
    digit1 = str(num0 % base)

    num2 = num1 // base
    digit2 = str(num1 % base)

    digit3 = str(num2 % base)

    return digit3 + digit2 + digit1 + digit0


def main():
    """
    Main function used to test other functions.
    """
    print(format_name("KyrILl", "   MetalnIKoV   "))
    print(tripler("aced"))
    print(this_year())
    print(base_conversion())


if __name__ == "__main__":
    main()
