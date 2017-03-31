from immdict import ImmDict
from functools import reduce

# module suffix


def empty_suffix():
    return ImmDict()


def add_word(suffix, word):
    if word in suffix.keys():
        return suffix.put(word, suffix.get(word)+1)
    else:
        return suffix.put(word, 1)


def choose_word(chain, prefix, randomizer):
    rand = randomizer(reduce(lambda x, y: x + y, chain.get(prefix).values()))
    suffix_list = [value for value in chain.get(prefix).keys() for x in range(chain.get(prefix).get(value))]
    return suffix_list[rand-1]


