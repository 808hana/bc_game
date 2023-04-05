import variables


# possible choices and assigning their value
def base():
    # path through the dungeon, there are always two option on how to get to another point
    list1 = ['A0', 'B0', 'C0', 'D0', 'E0', 'F0', 'G0', 'H0', 'I0', 'J0']  # A0 is one option of how to get to point B
    list2 = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1']  # A1 is second option of how to get to point B

    player_choices_list = []  # the solution

    sword_durability = 8  # potentially destroyed after 2 kills

    mydictionary = {'A0': 1,
                    'A1': 5,
                    'B0': 1,
                    'B1': 5,
                    'C0': 10,
                    'C1': 5,
                    'D0': 1,
                    'D1': 5,
                    'E0': 1,
                    'E1': 5,
                    'F0': 0,  # add the merchant
                    'F1': 0,
                    'G0': -3,  # cheap sword
                    'G1': -10,  # expensive sword
                    'H0': -7,  # cure the wrath of dungeon
                    'H1': -2,  # weird black liquid
                    'I0': 1,
                    'I1': 5,
                    'J0': 10,
                    'J1': 30
                    }

    # the possible choice on each list are translated to their score
    phoenetic = [mydictionary[letter] for letter in list1]
    phoenetic2 = [mydictionary[letter] for letter in list2]

    return phoenetic, phoenetic2, list1, list2, sword_durability


def detect_attack(player_choice):
    player_attacked_dictionary = {'A0': False,
                                  'A1': True,
                                  'B0': False,
                                  'B1': True,
                                  'C0': False,
                                  'C1': True,
                                  'D0': False,
                                  'D1': True,
                                  'E0': False,
                                  'E1': True,
                                  'F0': False,
                                  'F1': False,
                                  'G0': False,
                                  'G1': False,
                                  'H0': False,
                                  'H1': False,
                                  'I0': False,
                                  'I1': True,
                                  'J0': True,
                                  'J1': True
                                  }

    player_attacked = player_attacked_dictionary[player_choice]

    return player_attacked


def add_it_to_list(player_choices_list, option, score, choice_score, player_attacked, sword_durability,
                   wrath_of_dungeon_token, black_potion_token, slaying_the_dragon):

    # count score - depends only on sword durability (the ability to attack)
    score, sword_durability = score_counter(score, choice_score, player_attacked, sword_durability, slaying_the_dragon, black_potion_token)

    # add players choice to list
    player_choices_list.append(option)

    # call rules
    score = rules(score, wrath_of_dungeon_token)

    return player_choices_list, score, sword_durability


def score_counter(score, choice_score, player_attacked, sword_durability, slaying_the_dragon, black_potion_token):
    if slaying_the_dragon:
        if black_potion_token:
            score += choice_score
            print('You have turned into a dragon! You have killed the dragon with ease, and with your '
                  'excellent sense of smell found his most precious treasure! Good job!')

        elif sword_durability >= 20:
            score += choice_score
            sword_durability = sword(sword_durability)
            print('Congratulation! You have slayed the dragon!\n')
            print('Durability of your sword: ', sword_durability, '\n')

        elif sword_durability < 20:
            score += 0
            print('You are unable to kill the dragon with your current sword. You are running out of the '
                  'dragons lair without any gold!\n')
            print('Durability of your sword: ', sword_durability, '\n')

    elif player_attacked is True and sword_durability == 0:
        score += 0
        print('Your attack failed. Get a sword!\n')

    elif player_attacked is True and sword_durability > 0:
        score += choice_score
        sword_durability = sword(sword_durability)
        print('Durability of your sword: ', sword_durability, '\n')

    elif player_attacked is False:
        score += choice_score

    else:
        print('ERROR')

    return score, sword_durability


def sword(sword_durability):
    sword_gets_damaged = variables.sword_gets_damaged()
    print('Sword got damaged by: ', sword_gets_damaged)
    sword_durability -= sword_gets_damaged

    if sword_durability <= 0:
        sword_durability = 0
        print('Your sword is broken. All your attacks will fail.\n')

    return sword_durability


def rules(score, wrath_of_dungeon_token):
    wrath_of_dungeon = variables.wrath_of_dungeon()
    blessing_of_goddess = variables.blessing_of_goddess()

    if wrath_of_dungeon_token:
        if wrath_of_dungeon > 0:
            print('You have awakened the wrath of dungeon!\n')
            score = score - wrath_of_dungeon

    # if you have stolen from dungeon you can not receive the blessing
    if wrath_of_dungeon_token is False and blessing_of_goddess > 0:
        score = score + blessing_of_goddess
        print('Congratulations! You have received the Blessing of Goddess!\n')

    return score


# AI VERSIONS
def ai_add_it_to_list(player_choices_list, option, score, choice_score, player_attacked, sword_durability):
    # count score - depends only on sword durability (the ability to attack)
    score, sword_durability = ai_score_counter(score, choice_score, player_attacked, sword_durability)

    # add players choice to list
    player_choices_list.append(option)

    # call rules
    score = ai_rules(player_choices_list, score)

    return player_choices_list, score, sword_durability


def ai_score_counter(score, choice_score, player_attacked, sword_durability):
    if player_attacked is True and sword_durability == 0:
        score += 0

    elif player_attacked is True and sword_durability > 0:
        score += choice_score
        sword_durability = sword(sword_durability)

    elif player_attacked is False:
        score += choice_score

    else:
        print('ERROR')

    return score, sword_durability


def ai_sword(sword_durability):
    sword_gets_damaged = variables.sword_gets_damaged()
    sword_durability -= sword_gets_damaged

    return sword_durability


def ai_rules(ai_choices_list, score):
    wrath_of_dungeon = variables.wrath_of_dungeon()
    blessing_of_goddess = variables.blessing_of_goddess()

    if 'C0' in ai_choices_list:
        if wrath_of_dungeon > 0:
            score = score - wrath_of_dungeon

    if 'C0' not in ai_choices_list and blessing_of_goddess > 0:
        score = score + blessing_of_goddess

    return score
