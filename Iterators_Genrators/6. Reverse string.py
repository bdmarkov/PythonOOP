
def reverse_text(some_string):
    num = len(some_string) - 1

    while num >= 0:
        yield some_string[num]
        num -= 1


for char in reverse_text("step"):
    print(char, end='')
