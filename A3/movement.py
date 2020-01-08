from A3.interaction import meet_staff, battle_round, meet_family


def check_valid_move(new_position: list):
    """
    Return boolean True if a position is in the 9x9 grid.

    :param new_position:
    :precondition new_position: must be a list of integers
    :postcondition: creates a tuple out of the position and checks
    to see if the tuple is in the list created using the range
    function function
    :return: boolean

    >>> check_valid_move([0, 1])
    True
    >>> check_valid_move([5, 5])
    False
    """
    tuple_position = tuple(new_position)
    if tuple_position in [(k, v) for k in range(9) for v in range(9)]:
        return True
    else:
        print("\nThat's out of bounds.")
        return False


def make_move(char_dict: dict, move_list: list):
    """
    Update character position if valid move.

    :param char_dict: a dictionary
    :param move_list: a list
    :precondition char_dict: must be a dictionary with 'Position' key
    :precondition move_list: must be a list containing only two integers
    :postcondition: calls helper function to determine whether move is valid, calls helper
    functions to determine what happens after a move
    """
    new_position = [char_dict['Position'][num] + move_list[num] for num in range(len(move_list))]
    if check_valid_move(new_position):
        if meet_family(char_dict):
            battle_round(char_dict)
        else:
            meet_staff(char_dict)
            gain_points(char_dict)
        char_dict['Position'] = new_position
        print("\nYou are now in square", str(new_position))


def validate_input(user_input: str):
    """
    Return Boolean True if user_input in a list of valid values, False if not.

    :param user_input: a string
    :precondition user_input: must be a string
    :postcondition: will make string lower case and check if it is in a list of valid values
    :return: a boolean value

    >>> validate_input('n')
    True
    >>> validate_input('r')
    False
    """
    if user_input.lower() in ['n', 'e', 's', 'w', 'el', 'quit']:
        return True
    else:
        return False


def process_input(move: str, user_dict: dict):
    """
    Call specific function depending on argument passed.

    :param move: str
    :param user_dict: dictionary
    :precondition move: must be a string (either 'n', 'e', 's', or 'w')
    :precondition user_dict: must be a dictionary with key 'Position' and 'Foes'
    :postcondition: calls another function
    return: a boolean value
    """
    if move in ['n', 'e', 's', 'w', 'el']:
        if move == 'n':
            make_move(user_dict, [-1, 0])
        elif move == 'e':
            make_move(user_dict, [0, -1])
        elif move == 's':
            make_move(user_dict, [1, 0])
        elif move == 'w':
            make_move(user_dict, [0, 1])
        elif move is 'el':
            print("\nYou have " + str(user_dict['Energy']) + " out of 10 energy remaining.")
        return True
    elif move == 'q':
        return False


def gain_points(char_dict: dict):
    """
    Increase user's energy level by 2 up to a maximum of 10.

    :param char_dict: a dictionary
    :precondition char_dict: must be a dictionary with 'Energy' key
    :postcondition: adds 2 to user's energy and if that makes it above 10, brings it down to 10
    """
    char_dict['Energy'] += 2
    if char_dict['Energy'] > 10:
        char_dict['Energy'] = 10


def main():
    pass


if __name__ == '__main__':
    main()