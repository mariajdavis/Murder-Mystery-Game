from A3.messages import welcome, instructions, mystery_solved
from A3.movement import validate_input, process_input


def create_character():
    """
    Return dictionary with character and game information.

    :return: a dictionary
    """
    character_dict = {'Energy': 10, 'Position': [8, 4],
                      'Family': ['Laura Silver', 'Frederick Silver', 'Josephine Silver', 'Olivia Silver',
                               'Timothy Silver', 'Jack Silver', 'Melissa Silver', 'Sam Silver'],
                      'Staff': ['the cook', 'the laundry maid', 'the nurse', 'the valet', 'the stable boy',
                                'the barmaid'],
                      'Clues': ['Sarah Silver did it! I saw her murder Sir Silver!',
                                'Sir Silver was murdered by a knife from the kitchen!',
                                'Sir Silver was murdered in the cellar!'],
                      'Solution': 0}
    return character_dict


# Added bool to driver parameters and set n=1 to be able to unit test one iteration of the while loop
def driver(character_dictionary: dict, bool):
    """
    Prompt user to make a move, check energy level, or quit while continue_game boolean is true.

    :param character_dictionary: a dictionary
    :precondition: must be a dictionary with 'Energy' key
    :postcondition: while continue_game is true and character's energy is above 0, continually
    prompts user to make a next move
    """
    continue_game = True
    n = 1
    while continue_game is True and character_dictionary['Energy'] is not 0 and n > 0:
        print("\nChoose your next move...\n"
              "(n) north, (e) east, (s) south, or (w) west?\n"
              "Check your (el) energy level or (quit) at anytime!")
        user_input = input()
        if validate_input(user_input):
            continue_game = process_input(user_input, character_dictionary)
        else:
            print("Not a valid option... try again.")
        if bool:
            n -= 1
        if character_dictionary['Solution'] == 3 and character_dictionary['Position'] == [8, 4]:
            mystery_solved()
            break


def game():
    """
    Drive the game.

    """
    welcome()
    instructions()
    driver(create_character(), False)


def main():
    game()


if __name__ == '__main__':
    main()