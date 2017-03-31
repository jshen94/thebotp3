import prefix
import suffix
from functools import reduce

NONWORD = '\n'


def build(filename):
    word_pair = pairs_gen(filename, line_gen)
    return build_chain(add_to_chain, word_pair, suffix.ImmDict())


def build_chain(add_prefix_func, gen, imm_dict):
    return reduce(add_prefix_func, gen, imm_dict)


def add_to_chain(chain, word_pair_gen):
    updated_dict = chain
    word_pair = tuple(word_pair_gen)
    if word_pair[0] in updated_dict.keys():
        suffix.add_word(updated_dict.get(word_pair[0]), word_pair[1])
    else:
        updated_dict = updated_dict.put(word_pair[0], suffix.empty_suffix().put(word_pair[1], 1))
    return updated_dict


def line_gen(filename):
    with open(filename) as file:
        for line in file:
            yield line


def pairs_gen(filename, line_func):
    last_prefix = prefix.new_prefix(NONWORD, NONWORD)
    for line in line_func(filename):
        line = ''.join(line).split()
        for word in line:
            yield (last_prefix, word)
            last_prefix = prefix.shift_in(last_prefix, word)
    return last_prefix, NONWORD
