from project.vehicle import Vehicle

from unittest import TestCase

class Testehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 200)

    def test_initialize(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)


    def test_str_vehicle(self):
        actual = str(self.vehicle)
        expected =  f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        self.assertEqual(expected, actual)

    def test_drive_should_raise_error(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(max_distance + 1)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_should_decrease(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption

        self.vehicle.drive(max_distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_should_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_should_increase(self):
        distance = 10
        self.vehicle.drive(distance)
        consumed_fuel = 10 * self.vehicle.fuel_consumption
        recharged_fuel = consumed_fuel / 2
        exprected_fuel = self.vehicle.fuel + recharged_fuel
        self.vehicle.refuel(recharged_fuel)

        self.assertEqual(exprected_fuel, self.vehicle.fuel)

if __name__ == "__main__":
    unittest.main()