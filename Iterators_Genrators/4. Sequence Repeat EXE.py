

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.count = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 0:
            temp = self.sequence[self.count]
            self.count += 1
            if self.count == len(self.sequence):
                self.count = 0
            self.number -= 1
            return temp
        raise StopIteration()




result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')



