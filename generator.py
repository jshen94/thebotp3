import prefix
import suffix


def get_word_list(chain, pre, rand_func, num, NONWORD):
    if chain.get(pre) is None or num == 0:
        return ""
    else:
        next_word = suffix.choose_word(chain, pre, rand_func)
        new_pre = prefix.shift_in(pre, next_word)
        return next_word + " " + get_word_list(chain, new_pre, rand_func, num - 1, NONWORD)


def generate(chain, rand_func, num, NONWORD):
    output = ''.join(str(get_word_list(chain, prefix.new_prefix(NONWORD, NONWORD), rand_func, num, NONWORD)))
    return output
