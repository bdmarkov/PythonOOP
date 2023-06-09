from project_Enc_4_EXE.beverage.hot_bevarage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.5

    def __init__(self, name, caffeine):
        self.__caffeine = caffeine
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)

    @property
    def caffeine(self):
        return self.__caffeine

