import ai_monte_carlo
from simple import game_base


# playable game
def real_deal():
    # initialize the game
    phoenetic, phoenetic2, list1, list2 = game_base.base()
    score = 0
    player_choices_list = []

    # some intro
    print('\nWelcome, brave adventurer!\n'
          'This dungeon holds many treasures, but also many deadly traps and strong foes.\n'
          "Beware of it's tricks! Many have died because of their pride, greed or simple stupidity!\n"
          'I wish you luck!\n\n')

    # basics
    print('Note: You will always be presented two choices. It is completely up to you which one you will choose.\n'
          '      Keep in mind that each choice will affect you final score and overall wealth.\n\n')

    # the game
    for i in range(5):
        while True:
            if i == 2:
                choice = input('Which path will you choose, brave adventurer?\n A:Steal {0} gold from an ancient chest '
                               'and risk the wrath of dungeon\n B:Kill the dungeon guardian and take {1} gold?\n'.format
                               (phoenetic[i], phoenetic2[i]))
            else:
                choice = input('Which path will you choose, brave adventurer?\n A:Take {0} gold that is offered to you '
                               'by dungeon guardian\n B:Kill the dungeon guardian and take {1} gold?\n'.format
                               (phoenetic[i], phoenetic2[i]))

            if choice == 'A' or choice == 'a':
                print('You have chosen an option: ', choice.upper())
                score += int(phoenetic[i])
                player_choices_list, score = game_base.add_it_to_list(player_choices_list, list1[i], score)

                break
            elif choice == 'B' or choice == 'b':
                print('You have chosen an option: ', choice.upper())
                score += int(phoenetic2[i])
                player_choices_list, score = game_base.add_it_to_list(player_choices_list, list2[i], score)
                break
            else:
                print('Invalid input. You choice is either A or B. Please, try again\n')

    print('Your total score is:', score)

# for ai
def game_demo():
    # initialize the game
    phoenetic, phoenetic2, list1, list2 = game_base.base()
    score = 0
    player_choices_list = []

    # some intro
    print('\nWelcome, brave adventurer!\n'
          'This dungeon holds many treasures, but also many deadly traps and strong foes.\n'
          "Beware of it's tricks! Many have died because of their pride, greed or simple stupidity!\n"
          'I wish you luck!\n\n')

    # basics
    print('Note: You will always be presented two choices. It is completely up to you which one you will choose.\n'
          '      Keep in mind that each choice will affect you final score and overall wealth.\n\n')

    # the game
    for i in range(5):
        while True:
            if i == 2:
                print('Which path will you choose, brave adventurer?\n A:Steal {0} gold from an ancient chest '
                               'and risk the wrath of dungeon\n B:Kill the dungeon guardian and take {1} gold?\n'.format
                               (phoenetic[i], phoenetic2[i]))
            else:
                print('Which path will you choose, brave adventurer?\n A:Take {0} gold that is offered to you '
                               'by dungeon guardian\n B:Kill the dungeon guardian and take {1} gold?\n'.format
                               (phoenetic[i], phoenetic2[i]))
            choice = ai_monte_carlo.mcts(5, 5-i)

            if choice == 'A':
                print('You have chosen an option: ', choice)
                score += int(phoenetic[i])
                player_choices_list, score = game_base.add_it_to_list(player_choices_list, list1[i], score)
                break
            elif choice == 'B':
                print('You have chosen an option: ', choice)
                score += int(phoenetic2[i])
                player_choices_list, score = game_base.add_it_to_list(player_choices_list, list2[i], score)
                break
            else:
                print('Invalid input. You choice is either A or B. Please, try again\n')

    print('Your total score is:', score)


if __name__ == '__main__':
    # ai_starter.first_fun()   # standard game, solved by choosing always the option with more points
    # ai_starter.second_fun()  # game with one added rule, solved by choosing always the option with more points
    # real_deal()  # game with added rules, supposed to be played by real player

    #avg_score = ai_monte_carlo.random_game(5)
    #print('Expected score: {:.2f}'.format(avg_score))

    #ai_monte_carlo.mcts(5, 5)
    #ai_monte_carlo.mcts(5, 4)

    game_demo()

