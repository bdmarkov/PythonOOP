from project_Inheritence_EXE.hero import Hero


class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)