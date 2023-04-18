from project.hero import Hero

from unittest import TestCase, main

class TestHero(TestCase):
    def test_hero_initialization(self):
        hero = Hero("Name", 10, 100, 75)
        self.assertEqual("Name", hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(75, hero.damage)

    def test_hero_str_should_return_proper_string(self):
        hero = Hero("Name", 10, 100, 75)
        expected = f"Hero {hero.username}: {hero.level} lvl\n" \
               f"Health: {hero.health}\n" \
               f"Damage: {hero.damage}\n"
        actual = (str(hero))

        self.assertEqual(expected, actual)

    def test_battle_raises_error_when_hero_Attacks_himself(self):
        hero = Hero("Name", 10, 100, 75)
        enemy = Hero("Name", 10, 100, 75)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raises_error_when_hero_attacks_with_zero_or_less_health(self):
        for health in [0, -25]:
            hero = Hero("Name", 10, health, 75)
            enemy = Hero("Enemy", 10, 100, 75)
            with self.assertRaises(ValueError) as ex:
                hero.battle(enemy)

            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_raises_error_enemy_has_zero_or_less_health(self):
        for health in [0, -25]:
            hero = Hero("Name", 10, 100, 75)
            enemy = Hero("Enemy", 10, health, 75)
            with self.assertRaises(ValueError) as ex:
                hero.battle(enemy)

            self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))


    def test_battle_returns_Draw_when_both_heroes_die(self):
        hero = Hero("Name", 10, 100, 75)
        enemy = Hero("Enemy",hero.level, hero.health, hero.damage)

        expected_health = hero.health - enemy.level * enemy.damage

        result = hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(expected_health, hero.health)
        self.assertEqual(expected_health, enemy.health)


    def test_battle_returns_win_when_enemy_dies(self):
        hero_level, hero_health, hero_damage = 10, 100, 75
        enemy_level, enemy_health, enemy_damage = hero_level, (hero_level * hero_damage) + 250, hero_health

        hero = Hero("Name",hero_level, hero_health, hero_damage)
        enemy = Hero("Enemy", enemy_level, enemy_health, enemy_damage)

        result = enemy.battle(hero)

        self.assertEqual("You win", result)
        self.assertEqual(enemy_level + 1, enemy.level)
        self.assertEqual(enemy_health - hero_level * hero_damage + 5, enemy.health)
        self.assertEqual(enemy_damage + 5, enemy.damage)


    def test_battle_returns_lose_when_hero_dies(self):
        hero_level, hero_health, hero_damage = 10, 100, 75
        enemy_level, enemy_health, enemy_damage = hero_level, (hero_level * hero_damage) + 250, hero_health

        hero = Hero("Name", hero_level, hero_health, hero_damage)
        enemy = Hero("Enemy", enemy_level, enemy_health, enemy_damage)

        result = hero.battle(enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(enemy_level + 1, enemy.level)
        self.assertEqual(enemy_health - hero_level * hero_damage + 5, enemy.health)
        self.assertEqual(enemy_damage + 5, enemy.damage)

if __name__ == "__main__":
    unittest.main()

