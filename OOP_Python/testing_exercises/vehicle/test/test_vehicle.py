from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(75, 100)

    def test_default_fuel_consumption_correct(self):
        self.assertEqual(self.FUEL_CONSUMPTION, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init_correct(self):
        self.assertEqual(75, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(self.FUEL_CONSUMPTION, self.vehicle.fuel_consumption)
        self.assertEqual(100, self.vehicle.horse_power)

    def test_vehicle_fuel_need_expect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_vehicle_fuel_need_correct(self):
        self.vehicle.drive(20)
        self.assertEqual(50, self.vehicle.fuel)

    def test_vehicle_refuel_expect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_refuel_correct(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(10)
        self.assertEqual(60, self.vehicle.fuel)

    def test_str_information_correct(self):
        result = self.vehicle.__str__()
        # result = str(self.vehicle)
        expected_result = f"The vehicle has {100} horse power with {75} fuel left and {self.FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
