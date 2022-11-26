from unittest import main, TestCase

from project.mammal import Mammal


class MammalTests(TestCase):
    NAME = 'Mini'
    MAMMAL_TYPE = "Dog"
    SOUND = 'Bau'

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.MAMMAL_TYPE, self.SOUND)

    def test_init_corrct(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.MAMMAL_TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual('animals',  self.mammal._Mammal__kingdom)

    def test_mammal_make_sound_correct(self):
        self.assertEqual(f"{self.NAME} makes {self.SOUND}", self.mammal.make_sound())

    def test_mammal_get_kingdom_correct(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_mammal_get_info_correct(self):
        self.assertEqual(f"{self.NAME} is of type {self.MAMMAL_TYPE}", self.mammal.info())


if __name__ == "__main__":
    main()
