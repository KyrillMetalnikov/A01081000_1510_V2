def get_user_input() -> str:
    return input("What is the name of the file you wish top open?")


def print_entry_message():
    print("Welcome to Kyrill's word ranker!  You bank 'em we rank 'em!")


def rank_words(filename: str):
    word_dict = {}
    with open(filename) as file_object:
        for line in file_object:
            contents = file_object.readline()
            word_list = contents.split()
            for word in word_list:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1


def main():
    print_entry_message()
    rank_words(get_user_input())
