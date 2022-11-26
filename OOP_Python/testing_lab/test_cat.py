import unittest

from testing_lab.cat import Cat


class CatTests(unittest.TestCase):
    NAME = "Tom"

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_cat__size_increase_correct(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat__check_is_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_after_is_fed_raise(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertIsNotNone(ex)
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_sleep_not_fed_raise(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertIsNotNone(ex)
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()

"""•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping
"""
