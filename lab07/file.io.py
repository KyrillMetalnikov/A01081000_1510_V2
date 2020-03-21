def get_user_input() -> str:
    """
    Get user input.

    :precondition: User will enter an input
    :postcondition: The function will return the input
    :return: A string that the user inputted
    """
    return input("What is the name of the file you wish top open?")


def print_entry_message():
    print("Welcome to Kyrill's word ranker!  You bank 'em we rank 'em!")


def count_words(filename: str):
    word_dict = {}
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


def rank_words(word_dict):
    rank_list = sorted(word_dict, key=word_dict.get, reverse=True)
    for i in range(0, 10):
        print(rank_list[i], word_dict[rank_list[i]])


def main():
    print_entry_message()
    rank_words(count_words(get_user_input()))


if __name__ == "__main__":
    main()
