import random
from A3.messages import game_over


def battle_round(char_dict: dict):
    """
    Call attack function while it returns a list of length two containing no zeros.

    :param char_dict: a dictionary
    :precondition char_dict: must be a dictionary with 'Family' and 'Energy' keys
    :postcondition char_dict: creates a new dictionary with information from char_dict
    """
    family_dict = create_family_character(char_dict)
    print("\nOh no, it's " + family_dict['Name'] + "...")
    print("\nThey live here so you let them speak first...\n")
    attack_results = list([char_dict['Energy'], family_dict['Energy']])
    while attack_results[0] != 0 and attack_results[1] != 0:
        attack_results = attack(char_dict, family_dict)
    if attack_results[0] == 0:
        game_over(char_dict, family_dict['Name'])


def create_family_character(character_dict: dict):
    """
    Return a dictionary with a family member's name and energy level.

    :param character_dict: a dictionary
    :precondition character_dict: must be a dictionary with a 'Family' key
    :postcondition: pops the value at the first index of list in character_dict 'Family' key, forms new dictionary
    :return: a new dictionary
    """
    return {'Name': character_dict['Family'].pop(0), 'Energy': 5}


def roll_die(number_of_rolls: int, number_of_sides: int):
    """
    Return an integer.

    Uses the range function to call the randint function number_of_rolls
    times, and adds up all random totals and returns that value.
    :param number_of_rolls: positive integer
    :param number_of_sides: positive integer
    :precondition: both parameters much represent a positive integer
    :postcondition: adds up random integers that result when a dice with
    1-number_of_sides is rolled number_of_rolls times
    :return: positive integer
    """
    sum_of_rolls = 0
    for each_roll in range(1, number_of_rolls + 1):
        sum_of_rolls += random.randint(1, number_of_sides)
    return sum_of_rolls


def meet_family(char_dict: dict):
    """
    Return boolean value indicating user's response to fight or flight prompt.

    :param char_dict: a dictionary
    :precondition char_dict: must be a dictionary
    :postcondition: randint function determines whether user meets a family member, user prompted
    to make choice between staying and running away
    :return: a boolean value
    """
    if random.randint(1, 4) == 1:
        print("\nOh no... It's someone from the family.")
        response = 'none'
        while response is not 's' or 'r':
            response = input("(s) stay or (r) run?\n")
            if response == 's':
                return True
            if response == 'r':
                run_away(char_dict)
                return False
    return False


def meet_staff(char_dict: dict):
    """
    Print message to user if they encounter a staff member.

    :param char_dict: a dictionary
    :precondition char_dict: must be a dictionary with 'Staff', 'Solution', and 'Clues' keys
    :postcondition: calls randint function to determine whether user meets a staff member who
    may have clues for them
    :return: boolean value
    """
    if random.randint(1, 4) == 1:
        staff = char_dict['Staff'][:]
        if staff: # checks to see if there are any staff members left in the staff list in char_dict
            char_dict['Staff'].pop(0)
            print("\nOh look, it's " + staff[0] + "!\n")
            if (len(staff[0]) > 9):
                char_dict['Solution'] += 1
                print(staff[0].capitalize() + ": You have to tell the Butler that " + char_dict['Clues'].pop() +
                                              "\n\t\t\tI have to go! Good luck!")
                print("\nYou now have " + str(char_dict['Solution']) + " out of 3 of the clues!")
            else:
                print(staff[0].capitalize() + ": I heard the butler has you looking for clues! I'm sorry but I don't\n"
                                              "\t\t\thave anything for you. I have to get back to work. Good luck!")
        return True
    return False

def attack(char_dictionary: dict, family_dictionary: dict):
    """
    Return updated list of user and family member's energy levels.

    :param char_dictionary: a dictionary
    :param family_dictionary: a dictionary
    :precondition char_dictionary: must be a dictionary with 'Energy' key
    :precondition family_dictionary: must be a dictionary with 'Energy' and 'Name' keys
    :postcondition: calls roll_die function and deducts results from opponent's health
    :return: a list of length two with the character's energy in index 0 and family member's
    energy in index 1
    """
    family_attack_roll = roll_die(1, 6)
    if char_dictionary['Energy'] > family_attack_roll:
        char_dictionary['Energy'] -= family_attack_roll
        char_attack_roll = roll_die(1, 6)
        if family_dictionary['Energy'] > char_attack_roll:
            family_dictionary['Energy'] -= char_attack_roll
            return [char_dictionary['Energy'], family_dictionary['Energy']]
        else:
            print("Luckily, you bored " + family_dictionary['Name'] + " and they walked away.")
            return [char_dictionary['Energy'], 0]
    else:
        return [0, 5]


def run_away(char_dict: dict):
    """
    Inform user if energy points are lost running away.

    :param char_dict: a dictionary
    :precondition char_dict: must be a dictionary with 'Energy' key
    :postcondition: uses randint function to determine whether deduct energy points using roll_die function
    """
    if random.randint(1, 10) == 1:
        damage = roll_die(1, 4)
        char_dict['Energy'] -= damage
        print("\nIn your rush running away, you lost " + str(damage) + " energy points!")


def main():
    pass


if __name__ == '__main__':
    main()