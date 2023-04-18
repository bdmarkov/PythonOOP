from project.mammal import Mammal
from unittest import TestCase, main

class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("name", "type", "sound")

    def test_initialize(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_sound(self):
        expected =  f"{self.mammal.name} makes {self.mammal.sound}"
        actual = self.mammal.make_sound()

        self.assertEqual(expected, actual)

    def test_knigdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        actual = self.mammal.info()
        expected = f"{self.mammal.name} is of type {self.mammal.type}"

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()