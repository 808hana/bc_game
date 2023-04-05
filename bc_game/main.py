import ai_monte_carlo_complex, more_complex_base, story


def choices(i, phoenetic, phoenetic2, player_choices_list):
    if i == 2:
        choice = input('Which path will you choose, brave adventurer?\n A:Steal {0} gold from an ancient chest '
                       'and risk the wrath of dungeon\n B:Kill the dungeon guardian and take {1} gold?\n'.format
                       (phoenetic[i], phoenetic2[i]))

    elif i == 5:
        choice = input('You see a stall and a merchant. The problem is, the merchant is a skeleton. '
                       'You come closer and hear him say: '
                       'Welcome! Do you need something, adventurer?\n '
                       'What will you say?\n'
                       'A: I need a good sword.\n'
                       'B: What potions do you have?\n')

    elif i == 6:
        if 'F0' in player_choices_list:
            choice = input("I have this cheap one, the merchant responds, but, if you can afford it, "
                           "I have this sword. It doesn't look like much, but it will serve you well.\n"
                           "What will it be? skeleton asked with curiosity.\n "
                           "A: You take the cheap sword for {0} gold\n"
                           "B: You buy the more expensive sword for {1} gold\n".format(phoenetic[i], phoenetic2[i]))
        else:
            choice = 'C'

    elif i == 7:
        if 'F1' in player_choices_list:
            choice = input("Oho! I have a great one! This one right here, will cure the Wrath of Dungeon! "
                           "the merchant pointed out to swamp like green potion. Or i have this black one, that "
                           "i have traded for viking helmet.\n"
                           "A: You take the swamp potion for {0} gold\n"
                           "B: You buy the black potion for {1} gold\n".format(phoenetic[i], phoenetic2[i]))
        else:
            choice = 'C'

    elif i == 0 or i == 1 or i == 3 or i == 4 or i == 8:
        choice = input('Which path will you choose, brave adventurer?\n A:Take {0} gold that is offered to you '
                       'by dungeon guardian\n B:Kill the dungeon guardian and take {1} gold?\n'.format
                       (phoenetic[i], phoenetic2[i]))
    elif i == 9:
        choice = input("You entered a dark lair. You think there might be a dangerous best. And there is. "
                       "Out of nowhere you hear a mighty roar of a dragon.\n"
                       "What will you do?\n"
                       "A: Prepare your sword and kill the dragon\n"
                       "B: Drink the black potion (only works if you have bought it)\n")

    return choice


def real_deal():
    # initialize the game
    phoenetic, phoenetic2, list_a, list_b, sword_durability = more_complex_base.base()
    score = 0
    player_choices_list = []

    wrath_of_dungeon_token = False
    black_potion_token = False
    black_potion = False
    slaying_the_dragon = False

    story.who_is_Erik()
    story.father_Erik_dialog()
    story.tavern()
    story.gate()
    story.training()
    story.challenging_the_dungeon()

    story.intro_to_dungeon()
    story.gameplay()

    # the game
    for i in range(10):
        while True:
            choice = choices(i, phoenetic, phoenetic2, player_choices_list)

            if choice == 'A' or choice == 'a':
                if i == 2:
                    print('YOU HAVE AWAKENED THE WRATH OF DUNGEON!')
                    wrath_of_dungeon_token = True
                if i == 6:
                    print('I TAKE THE CHEAP SWORD!')
                    sword_durability = 8  # you won't be able to slay the dragon
                    print('You can now slay monsters! Your sword durability is: ', sword_durability)
                elif i == 7:
                    print('I TAKE THE SWAMP POTION!')   # remove the Wrath of dungeon
                    wrath_of_dungeon_token = False
                elif i == 9:
                    slaying_the_dragon = True
                    print('SLAY THE DRAGON!')

                print('You have chosen an option: ', choice.upper())
                player_attacked = more_complex_base.detect_attack(list_a[i])
                player_choices_list, score, sword_durability = more_complex_base.add_it_to_list(player_choices_list,
                                                               list_a[i], score, int(phoenetic[i]), player_attacked,
                                                               sword_durability, wrath_of_dungeon_token,
                                                               black_potion_token, slaying_the_dragon)
                print('Your score so far is:', score)
                break

            elif choice == 'B' or choice == 'b':
                if i == 6:
                    print('I TAKE THE EXPENSIVE SWORD!')
                    sword_durability = 20  # you can slay the dragon (min.20)
                    print('You can now slay monsters! Your sword durability is: ', sword_durability)
                elif i == 7:
                    print('I TAKE THE BLACK POTION')   # you turn into a dragon
                    black_potion = True
                elif i == 9:
                    slaying_the_dragon = True
                    black_potion_token = True
                    print('KILL THE DRAGON!')

                print('You have chosen an option: ', choice.upper())
                player_attacked = more_complex_base.detect_attack(list_b[i])
                player_choices_list, score, sword_durability = more_complex_base.add_it_to_list(player_choices_list,
                                                               list_b[i], score, int(phoenetic2[i]), player_attacked,
                                                               sword_durability, wrath_of_dungeon_token,
                                                               black_potion_token, slaying_the_dragon)
                print('Your score so far is:', score)
                break

            elif choice == 'C':
                break

            else:
                print('Invalid input. You choice is either A or B. Please, try again\n')

    print('Your total score is:', score)

# for ai
def game_demo():
    # initialize the game
    phoenetic, phoenetic2, list1, list2, sword_durability = more_complex_base.base()
    score = 0
    player_choices_list = []

    story.intro_to_dungeon()
    story.gameplay()


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
            choice = ai_monte_carlo_complex.mcts(5, 5-i)

            if choice == 'A':
                print('You have chosen an option: ', choice)

                # player attacked?
                player_attacked = more_complex_base.detect_attack(list1[i])

                # check if player can make this choice
                player_choices_list, score, sword_durability = more_complex_base.add_it_to_list(player_choices_list, list1[i], score, int(phoenetic[i]), player_attacked, sword_durability)
                break
            elif choice == 'B':
                print('You have chosen an option: ', choice)
                player_attacked = more_complex_base.detect_attack(list2[i])
                player_choices_list, score, sword_durability = more_complex_base.add_it_to_list(player_choices_list, list2[i], score, int(phoenetic2[i]), player_attacked, sword_durability)
                break
            else:
                print('Invalid input. You choice is either A or B. Please, try again\n')

    print('Your total score is:', score)


if __name__ == '__main__':
    real_deal()
    # game_demo()

