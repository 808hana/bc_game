import random as rn


def wrath_of_dungeon():
    value = rn.random()

    if value > 0.3:
        wrath_of_dungeon = 3

    if value < 0.3:
        wrath_of_dungeon = 0

    return wrath_of_dungeon


def blessing_of_goddess():
    value = rn.random()

    if value > 0.8:
        blessing_of_goddess = 1

    if value < 0.8:
        blessing_of_goddess = 0

    return blessing_of_goddess


def sword_gets_damaged():
    value = rn.random()

    if value < 0.2:
        sword_gets_damaged = 1

    if 0.2 < value < 0.4:
        sword_gets_damaged = 2

    if 0.4 < value < 0.6:
        sword_gets_damaged = 3

    if 0.6 < value < 0.8:
        sword_gets_damaged = 4

    if 0.8 < value:
        sword_gets_damaged = 5

    return sword_gets_damaged
