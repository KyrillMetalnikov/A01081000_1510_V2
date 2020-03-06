"""Make a maze and let a user walk through it."""


def game():
    board = make_board(5)
    character = make_character(board)
    display_board(board, character)
    found_exit = False
    while not found_exit:  # Tell the user where they are
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(direction, character)
            found_exit = check_if_exit_reached(character, board)
            display_board(board, character)
        else:  # Tell the user they can't go in that direction
            print("You cannot go there!  Choose a different direction!")
    print("You've won!  Congratulations on walking a straightish line!")


def make_board(size):
    x_axis = (0, size - 1)
    y_axis = (0, size - 1)
    board = (x_axis, y_axis)
    return board


def make_character(current_board):
    position = [current_board[0][0], current_board[1][0]]
    return position


def get_user_choice():
    return input("Which direction do you want to go in (N, E, S, W)").upper()


def validate_move(board, character, direction):
    """
    Validate the character's move.

    :param board: A tuple representing the full board.
    :param character: A list representing the characters current position
    :param direction: A string representing a direction the user wishes to move towards.
    :precondition: The rules of the parameters are followed.
    :postcondition: The function will determine if the move is valid.
    :return: A boolean representing whether or not a move is valid.
    """
    if direction == "N":
        if character[1] > board[1][0]:
            return True
    elif direction == "S":
        if character[1] < board[1][1]:
            return True
    elif direction == "E":
        if character[0] < board[0][1]:
            return True
    elif direction == "W":
        if character[0] > board[0][0]:
            return True
    else:
        return False


def display_board(board, character):
    coordinates = tuple(character)
    for y_coordinate in range(0, board[1][1] + 1):
        for x_coordinate in range(0, board[1][1] + 1):
            if (x_coordinate, y_coordinate) == coordinates:
                print("O", end="")
            else:
                print("x", end="")
        print("")


def move_character(direction, character):
    if direction == "N":
        character[1] -= 1
    elif direction == "S":
        character[1] += 1
    elif direction == "E":
        character[0] += 1
    elif direction == "W":
        character[0] -= 1


def check_if_exit_reached(character, board):
    if character[1] == board[1][1] and character[0] == board[0][1]:
        return True
    else:
        return False


def main():
    game()


if __name__ == "__main__":
    main()
