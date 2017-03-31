import copy


class ImmDict:

    def __init__(self):
        self.immdict = {}

    def put(self, key, value):
        updated_dict = self.immdict
        updated_dict.update({key: value})
        new_dict = copy.deepcopy(self)
        new_dict.immdict = updated_dict
        return new_dict

    def get(self, key):
        return self.immdict.get(key)

    def keys(self):
        return copy.deepcopy(list(self.immdict.keys()))

    def values(self):
        return copy.deepcopy(list(self.immdict.values()))
