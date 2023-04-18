

class vowels:
    def __init__(self, vowels_input):
        self.vowels_input = vowels_input
        self.start = -1
        self.all_vowels = "AOIUYEaoiuye"
        self.vowels_input = [el for el in self.vowels_input if el in self.all_vowels]

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == len(self.vowels_input) - 1:
            raise StopIteration
        self.start += 1
        return self.vowels_input[self.start]




my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
