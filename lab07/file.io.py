def get_user_input() -> str:
    return input("What is the name of the file you wish top open?")


def print_entry_message():
    print("Welcome to Kyrill's word ranker!  You bank 'em we rank 'em!")


def count_words(filename: str):
    word_dict = {}
    with open(filename) as file_object:
        for _ in file_object:
            contents = file_object.readline()
            char_list = list(contents)
            punctuation = "!@#$%^&*()_+-=<>?,./;:\"[]{}\\|"
            for i in range(0, len(char_list)):
                if char_list[i] in punctuation:
                    char_list[i] = ""
            word_list = "".join(char_list)
            word_list = word_list.split()
            for word in word_list:
                if word.lower() in word_dict:
                    word_dict[word.lower()] += 1
                elif word.lower() == "\\n":
                    pass
                else:
                    word_dict[word.lower()] = 1
    return word_dict


def main():
    print_entry_message()
    rank_words(get_user_input())


if __name__ == "__main__":
    main()