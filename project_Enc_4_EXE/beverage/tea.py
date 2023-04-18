from project_Enc_4_EXE.beverage.hot_bevarage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)