import doctest
"""Display the 10 most common words in a text file."""


def get_user_input() -> str:
    """
    Get user input.

    :precondition: User will enter an input
    :postcondition: The function will return the input
    :return: A string that the user inputted
    """
    return input("What is the name of the file you wish to open?").strip()


def print_entry_message():
    """
    Display welcome message.

    :precondition: No precondition
    :postcondition: The function will display the entry message
    """
    print("Welcome to Kyrill's word ranker!  You bank 'em we rank 'em!")


def count_words(filename: str) -> dict:
    """
    Count how many times every word comes up in a text file.

    :param filename: A string representing the relative address of a text file.
    :precondition: The file address must be a text file.
    :postcondition: The function will count how many times each word is written.
    :return: A dictionary of the words in the text file as keys and the amount of times written as values.
    """
    word_dict = {}
    try:
        with open(filename) as file_object:
            for _ in file_object:
                contents = file_object.read()
                char_list = list(contents)
                punctuation = "!@#$%^&*()-_+=<>?,./;':\"[]{}\\|"
                for i in range(0, len(char_list)):
                    if char_list[i] in punctuation:
                        char_list[i] = " "
                word_list = "".join(char_list)
                word_list = word_list.split()
                for word in word_list:
                    if word.lower() in word_dict:
                        word_dict[word.lower().strip()] += 1
                    elif word.lower().strip() == "\\n":
                        pass
                    else:
                        word_dict[word.lower().strip()] = 1
        return word_dict
    except FileNotFoundError:
        print("Error: File not found.")
        return {}
    except PermissionError:
        print("Error: Please set the directory for a file.")
        return {}
    except UnicodeDecodeError:
        print("Error: Please set the directory for a text file.")
        return {}


def sort_dict(word_dict):
    """
    Display the top 10 key value pairs in descending order of their values.

    :param word_dict: A dictionary of key value pairs
    :precondition: The values in word_dict must be numbers.
    :postcondition: The dictionary will be sorted and the 10 highest values will be displayed
    """
    rank_list = sorted(word_dict, key=word_dict.get, reverse=True)
    for i in range(0, 10):
        try:
            print(rank_list[i], word_dict[rank_list[i]])
        except IndexError:
            pass


def main():
    print_entry_message()
    sort_dict(count_words(get_user_input()))
    doctest.testmod()


if __name__ == "__main__":
    main()
