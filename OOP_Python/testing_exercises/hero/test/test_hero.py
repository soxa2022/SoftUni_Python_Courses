from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("sox", 2, 10, 5)
        self.enemy_hero = Hero("enemy", 2, 10, 5)

    def test_init_correct(self):
        self.assertEqual("sox", self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(5, self.hero.damage)

    def test_hero_username_equal_enemy_username_expect_raise_exception(self):
        self.enemy_hero.username = "sox"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_non_positive_expected_raise_exception(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_enemy_hero_health_non_positive_expected_raise_exception(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ve.exception))

    def test_hero_health_reduce_draw_result_correct(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_hero_add_points_result_win_correct(self):
        self.hero.health = 40
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(35, self.hero.health)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(10, self.hero.damage)
        self.assertEqual("You win", result)

    def test_enemy_hero_add_points_result_win_correct(self):
        self.enemy_hero.health = 40
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(35, self.enemy_hero.health)
        self.assertEqual(3, self.enemy_hero.level)
        self.assertEqual(10, self.enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_str_method_correct(self):
        result = str(self.hero)
        expected_result = f"Hero {'sox'}: {2} lvl\n" \
                          f"Health: {10}\n" \
                          f"Damage: {5}\n"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
