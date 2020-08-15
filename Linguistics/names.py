from random import randint
from .adjectives import adjectives
from .nouns import nouns


def generate_username():
    """
    pattern:
        adjective + noun + number
    """

    # pick random adjective
    adj_position = randint(0, len(adjectives))
    adjective = adjectives[adj_position]

    # pick random noun
    noun_position = randint(0, len(nouns))
    noun = nouns[noun_position]
    
    # pick random number
    number = randint(0, 1000)

    username = adjective + noun + str(number)

    return username