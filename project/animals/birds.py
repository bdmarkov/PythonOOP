from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOODS = ["Meat"]
    WEIGHT_MULTIPLYER = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)


    def make_sound(self):
        return f"Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOODS = ["Vegetable", "Fruit", "Meat", "Seed"]
    WEIGHT_MULTIPLYER = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)


    def make_sound(self):
        return f"Cluck"