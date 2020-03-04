"""Make a maze and let a user walk through it."""


def game():
    board = make_board()
    character = make_character(board)
    found_exit = False
    while not found_exit:  # Tell the user where they are
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character()
            found_exit = check_if_exit_reached()
        else:  # Tell the user they can't go in that direction
            print("You cannot go there!  Choose a different direction!")
    print("You've won!  Congratulations on walking a straightish line!")


def make_board():
    x_axis = (0, 1, 2, 3, 4)
    y_axis = (0, 1, 2, 3, 4)
    board = (x_axis, y_axis)
    return board


def make_character(current_board):
    position = [current_board[0][0], current_board[0][1]]
    return position


def get_user_choice():
    return input("Which direction do you want to go in (N, E, S, W")


def main():
    game()


if __name__ == "__main__":
    main()