from project_Enc_4_EXE.food.food import Food


class MainDish(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)