def introduction():
    # path through the dungeon, there are always two option on how to get to another point
    list1 = ['A0', 'B0', 'C0', 'D0', 'E0']  # A0 is one option of how to get to point B
    list2 = ['A1', 'B1', 'C1', 'D1', 'E1']  # A1 is second option of how to get to point B

    list3 = []  # the AI's solution

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

    score = 0

    # the possible choice on each list are translated to their score
    phoenetic = [mydictionary[letter] for letter in list1]
    phoenetic2 = [mydictionary[letter] for letter in list2]

    # here the AI always decides to take path that gets more score
    for i in range(5):
        if phoenetic[i] > phoenetic2[i]:
            list3.append(list1[i])
            score += int(phoenetic[i])

        elif phoenetic[i] < phoenetic2[i]:
            list3.append(list2[i])
            score += int(phoenetic2[i])

        else:
            print('ERROR')

    print('Your score is:', score)

    for j in range(5):
        print(list3[j])


def presenting_a_problem():
    # let's get this party started
    # let's add some fun rules

    # path through the dungeon, there are always two option on how to get to another point
    list1 = ['A0', 'B0', 'C0', 'D0', 'E0']  # A0 is one option of how to get to point B
    list2 = ['A1', 'B1', 'C1', 'D1', 'E1']  # A1 is second option of how to get to point B

    list3 = []  # the AI's solution

    mydictionary = {'A0': 1,
                    'A1': 5,
                    'B0': 1,
                    'B1': 5,
                    'C0': 10,
                    'C1': 5,
                    'D0': 1,
                    'D1': 5,
                    'E0': 1,
                    'E1': 5}  # each option has assigned number of points

    score = 0  # points from choices will result in an overall score

    # fun rules
    def new_rule(blacklist, score):
        # here we add a little drawback, if C0 worth of 10 points is chosen, then each following move will be extracted
        # 3 points from overall score
        if 'C0' in blacklist:
            score = score - 3
        return score

    # the possible choice on each list are translated to their points
    phoenetic = [mydictionary[letter] for letter in list1]
    phoenetic2 = [mydictionary[letter] for letter in list2]

    # here the AI always decides to take path that gets more score
    for i in range(5):
        if phoenetic[i] > phoenetic2[i]:
            score += int(phoenetic[i])
            list3.append(list1[i])
            score = new_rule(list3, score)  # updating score accordingly to our new rules

        elif phoenetic[i] < phoenetic2[i]:
            score += int(phoenetic2[i])
            list3.append(list2[i])
            score = new_rule(list3, score)  # updating score
        else:
            print('ERROR')

    print('Your score is:', score)
    # as we can see the score is lower, but if the AI chose the C1 option the score would be 25, four points higher
    print('C1 instead of C0 result:', sum(phoenetic2))

    for j in range(5):
        print(list3[j])