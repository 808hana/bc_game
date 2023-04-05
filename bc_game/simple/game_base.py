import random as rn


# possible choices and assigning their value
def base():
    # path through the dungeon, there are always two option on how to get to another point
    list1 = ['A0', 'B0', 'C0', 'D0', 'E0']  # A0 is one option of how to get to point B
    list2 = ['A1', 'B1', 'C1', 'D1', 'E1']  # A1 is second option of how to get to point B

    player_choices_list = []  # the solution

    mydictionary = {'A0': 1,
                    'A1': 5,
                    'B0': 1,
                    'B1': 5,
                    'C0': 10,
                    'C1': 5,
                    'D0': 1,
                    'D1': 5,
                    'E0': 1,
                    'E1': 5}  # each option has a score

    # the possible choice on each list are translated to their score
    phoenetic = [mydictionary[letter] for letter in list1]
    phoenetic2 = [mydictionary[letter] for letter in list2]

    return phoenetic, phoenetic2, list1, list2


def add_it_to_list(player_choices_list, option, score):
    # add players choice to list
    player_choices_list.append(option)

    # call rules
    score = rules(player_choices_list, score)

    return player_choices_list, score


def ai_add_it_to_list(player_choices_list, option, score):
    # add players choice to list
    player_choices_list.append(option)

    # call rules
    score = ai_rules(player_choices_list, score)

    return player_choices_list, score


def make_it_random():
    value = rn.random()

    if value > 0.3:
        wrath_of_dungeon = 3
    if value < 0.3:
        wrath_of_dungeon = 0
    if value > 0.8:
        blessing_of_goddess = 1
    if value < 0.8:
        blessing_of_goddess = 0

    return wrath_of_dungeon, blessing_of_goddess


def rules(player_choices_list, score):
    # here we add a little drawback, if C0 worth of 10 points is chosen, then with each move will be extracted
    # 3 points from overall score
    # if 'C0' in player_choices_list:
    # score = score - 3

    # maybe use random?
    wrath_of_dungeon, blessing_of_goddess = make_it_random()

    if 'C0' in player_choices_list:
        score = score - wrath_of_dungeon
    else:
        # if you have stolen from dungeon you can not receive the blessing
        if blessing_of_goddess > 0:
            print('Congratulations! You have received the Blessing of Goddess!\n')
            score = score + blessing_of_goddess

    return score


def ai_rules(ai_choices_list, score):

    wrath_of_dungeon, blessing_of_goddess = make_it_random()

    if 'C0' in ai_choices_list:
        score = score - wrath_of_dungeon
    else:
        # if you have stolen from dungeon you can not receive the blessing
        if blessing_of_goddess > 0:
            score = score + blessing_of_goddess

    return score
