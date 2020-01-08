def welcome():
    """
    Print welcome message.

    """
    print("\nThe butler: Welcome to the Silver Lake Manor, detective. I've called you here because\n"
          "\t\t\tthere has been a murder. Sir Silver is dead. Yes, that Sir Silver, the wealthiest man\n"
          "\t\t\tin Silver Lake. I suspect that someone in the family is involved as everyone knows he was\n"
          "\t\t\thoarding the family fortune. I have a good feeling that the other staff working on the\n"
          "\t\t\tproperty not only agree but have evidence, only I'm not able to talk to them for fear of\n"
          "\t\t\tbeing fired. I can't lose this job! None of us can risk our jobs. And I'm sure we will if\n"
          "\t\t\tthe culprit finds us conspiring. I need you to look around the property and speak to the\n"
          "\t\t\tstaff. Watch out for the family, they'll try and distract you from your investigation.\n"
          "\t\t\tThey'll bore you to death with insufferable stories and you'll lose all energy and give\n"
          "\t\t\tup. Once you figure out: (1) who did it, (2) where the murder took place, and (3) what\n"
          "\t\t\tthe weapon was, come back and find me. I'll be here waiting by the entrance.")


def instructions():
    """
    Print instructions.

    :return:
    """
    print("\nIf you look at the map, you're at point [8, 4], that's where I am, the entrance to the manor.\n"
          "Ahead (north), is the great hall, to the left is the living room, main kitchen, and the cellar.\n"
          "To the right is the dining room, the ballroom, and the library. Beyond the great hall, you'll\n"
          "find the gardens and the stables. You'll start out with 10 energy points. When you run into a\n"
          "family member and choose to engage, you'll risk losing energy. You will gain 2 energy points\n"
          "each time you make a move and don't run into a family member. Ready? Well go on, and hurry!")


def mystery_solved():
    """
    Print game completion message.

    """
    print("\nThe butler: The mystery is solved! I knew it was someone in the family. Well done!")


def game_over(char_dict: dict, family_name: str):
    """
    Set character's energy to zero which ends the game.

    :param char_dict: a dictionary
    :param family_name: a string
    :precondition char_dict: must be a dictionary with 'Energy' key
    :precondition family_name: must be a string
    :postcondition: set char_dict energy to 0 and inform user that game is over
    """
    char_dict['Energy'] = 0
    print(family_name + " is persistent and painful and you lose all interest in the case.\n"
                        "You secretly slink out the back entrance so the butler doesn't see that\n"
                        "you've given up.\n\nGame over!")


def main():
    pass


if __name__ == '__main__':
    main()