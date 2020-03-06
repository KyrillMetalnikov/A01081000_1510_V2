import doctest
"""Make a maze and let a user walk through it."""


def game():
    board = make_board(8)
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
    """
    Create a square board for play.

    :param size: A positive non-zero integer representing the width/height of the board.
    :precondition: The rules of the parameters must be followed.
    :postcondition: A square board will be created.
    :return: A tuple representing the min/max values allowed for the x and y coordinates.

    >>> make_board(1)
    ((0, 0), (0, 0))
    >>> make_board(5)
    ((0, 4), (0, 4))
    >>> make_board(100)
    ((0, 99), (0, 99))
    """
    x_axis = (0, size - 1)
    y_axis = (0, size - 1)
    board = (x_axis, y_axis)
    return board


def make_character(current_board):
    """
    Create a character by setting their position to the starting location.

    :param current_board: A tuple of two tuples representing the board.
    :precondition: Both tuples in current_board must have 0 as index 0 and at least 0 in index 1.
    :postcondition: The characters position will be set to coordinates (0, 0)
    :return: A list containing the characters current position.

    >>> make_character(((0, 4), (0, 4)))
    [0, 0]
    """
    position = [current_board[0][0], current_board[1][0]]
    return position


def get_user_choice():
    """
    Take a user input and convert it to uppercase.
    :precondition: The user inputs a string.
    :postcondition: The string will be set to uppercase.
    :return: A string in uppercase.
    """
    return input("Which direction do you want to go in (N, E, S, W)").upper()


def validate_move(board, character, direction):
    """
    Validate the character's move.

    :param board: A tuple representing the full board.
    :param character: A list representing the characters current position.
    :param direction: A string representing a direction the user wishes to move towards.
    :precondition: The rules of the parameters are followed.
    :postcondition: The function will determine if the move is valid.
    :return: A boolean representing whether or not a move is valid.

    >>> validate_move(((0, 5), (0, 5)), [0, 0], "N")
    False
    >>> validate_move(((0, 5), (0, 5)), [0, 0], "S")
    True
    >>> validate_move(((0, 5), (0, 5)), [0, 0], "W")
    False
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
    return False


def display_board(board, character):
    """
    Display the board with the character on it.

    :param board: A tuple of two tuples representing the playing area.
    :param character: A list representing the players current position.
    :precondition: The rules of the parameters must be followed.
    :postcondition: The board and the character will be displayed on screen.
    """
    coordinates = tuple(character)
    for y_coordinate in range(0, board[1][1] + 1):
        for x_coordinate in range(0, board[1][1] + 1):
            if (x_coordinate, y_coordinate) == coordinates:
                print("O", end=" ")
            else:
                print("x", end=" ")
        print("")


def move_character(direction, character):
    """
    Move a character one unit in a certain direction.

    :param direction: A string either "N", "S", "E", "W" representing the direction the character is moving.
    :param character: A list of two integers representing the characters current position.
    :precondition: The rules of the parameters must be followed.
    :postcondition: The characters position will be properly updated.
    """
    if direction == "N":
        character[1] -= 1
    elif direction == "S":
        character[1] += 1
    elif direction == "E":
        character[0] += 1
    elif direction == "W":
        character[0] -= 1


def check_if_exit_reached(character, board):
    """
    Check if the character reached the exit.

    :param character: A list of two integers representing the characters current position.
    :param board: A tuple of two tuples representing the playing area.
    :precondition: The rules of the parameters must be followed.
    :postcondition: The function will check if the character reached the exit.
    :return: A boolean value representing if the character reached the exit or not.

    >>> check_if_exit_reached([0, 0], ((0, 4), (0, 4)))
    False
    >>> check_if_exit_reached([4, 4], ((0, 4), (0, 4)))
    True
    """
    if character[1] == board[1][1] and character[0] == board[0][1]:
        return True
    else:
        return False


def main():
    game()


if __name__ == "__main__":
    main()
