from unittest import TestCase, main

from testing_lab.CarManager.car_manager import Car


class CarTests(TestCase):

    def setUp(self) -> None:
        self.car = Car("VW", "Golf", 5, 60)

    def test_init_work_correct(self):
        self.assertEqual("VW", self.car.make)
        self.assertEqual("Golf", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_make_name_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_car_model_name_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_car_fuel_consumption_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_car_fuel_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_car_fuel_amount_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_car_fuel_for_refuel_non_positive_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_car_refuel_fuel_amount_correct(self):
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)

    def test_car_refuel_correct(self):
        self.car.refuel(70)
        self.assertEqual(60, self.car.fuel_capacity)

    def test_car_drive_big_distance_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_car_drive_distance_correct(self):
        self.car.refuel(10)
        self.car.drive(100)
        self.assertEqual(5, self.car.fuel_amount)


if __name__ == "__main__":
    main()
