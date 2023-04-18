

class dictionary_iter:
    def __init__(self, dict_object):
        self.dict_object = dict_object
        self.count = len(self.dict_object)
        self.keys = list(self.dict_object.keys())
        self.key_index = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.key_index >= self.count:
            raise StopIteration
        key = self.keys[self.key_index]
        value = self.dict_object[key]
        self.key_index += 1
        return key, value

result = dictionary_iter({1: "1", 2: "2", 8: "3", 9: "4", 5: "7"})
for x in result:
    print(x)
