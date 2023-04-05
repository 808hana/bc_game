from simple import game_base
import random


def random_game(num_games):
    phoenetic, phoenetic2, list1, list2 = game_base.base()
    total_score = 0

    for i in range(num_games):
        score = 0
        for j in range(5):
            choice = random.choice(['A', 'B'])
            if choice == 'A':
                score += int(phoenetic[j])
            else:
                score += int(phoenetic2[j])

        total_score += score

    avg_score = total_score / num_games

    return avg_score


def mcts(length, nodes):
    phoenetic, phoenetic2, list1, list2 = game_base.base()
    ai_choice = ''

    options = ['A', 'B']

    total_score_A = 0
    total_score_B = 0

    avg_score_A = 0
    avg_score_B = 0

    num_games = 5

    # length = number of nodes in game

    # nodes = number of nodes to search

    # starting point -> i = (lenght - nodes)+1

    for option in options:
        ai_choices_list = []
        if option == 'A':
            ai_choices_list.append(option)
            for starting_point_score in range(num_games):
                total_score_A += int(phoenetic[0])
        else:
            ai_choices_list.append(option)
            for starting_point_score in range(num_games):
                total_score_B += int(phoenetic2[0])

        for j in range(num_games):
            # i -> from which node it starts
            i = length - nodes + 1
            while i < length:
                # print(i)
                choice = random.choice(['A', 'B'])
                # print(choice)
                if choice == 'A':
                    #print(list1[i])
                    if option == 'A':
                        ai_choices_list, total_score_A = game_base.ai_add_it_to_list(ai_choices_list, list1[i], total_score_A)
                        #total_score_A += int(phoenetic[i])
                    else:
                        #total_score_B += int(phoenetic[i])
                        ai_choices_list, total_score_B = game_base.ai_add_it_to_list(ai_choices_list, list1[i], total_score_B)
                else:
                    #print(list2[i])
                    if option == 'A':
                        #total_score_A += int(phoenetic2[i])
                        ai_choices_list, total_score_A = game_base.ai_add_it_to_list(ai_choices_list, list2[i], total_score_A)
                    else:
                        #total_score_B += int(phoenetic2[i])
                        ai_choices_list, total_score_B = game_base.ai_add_it_to_list(ai_choices_list, list2[i], total_score_B)
                i += 1

    #print('A', total_score_A)
    #print('B', total_score_B)

    avg_score_A = total_score_A/num_games
    avg_score_B = total_score_B/num_games

    if avg_score_A > avg_score_B:
        ai_choice = 'A'
    elif avg_score_A < avg_score_B:
        ai_choice = 'B'
    else:
        ai_choice = 'A'

    # print(ai_choice)

    return ai_choice
