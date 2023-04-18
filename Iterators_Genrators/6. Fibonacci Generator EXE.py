

def fibonacci():
    num1 = 0
    num2 = 1



    yield num1
    yield num2
    while True:
        num = num1 + num2
        yield num
        num1, num2 = num2, num





generator = fibonacci()
for i in range(5):
    print(next(generator))
