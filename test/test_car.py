import unittest
from datetime import datetime

from carFactory import CarFactory
from car import Car


class TestCalliope(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car = CarFactory.create_calliope(last_service_date, current_mileage,
                                         last_service_mileage)
        self.assertTrue(car.ServiceNeeded())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, current_mileage,
                                         last_service_mileage)
        self.assertFalse(car.ServiceNeeded())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, current_mileage,
                                         last_service_mileage)
        self.assertTrue(car.ServiceNeeded())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(last_service_date, current_mileage,
                                         last_service_mileage)
        self.assertFalse(car.ServiceNeeded())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car = CarFactory.create_glissade(last_service_date, current_mileage,
                                         last_service_mileage)
        self.assertTrue(car.ServiceNeeded())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(last_service_date, current_mileage,
                                         last_service_mileage)
        self.assertFalse(car.ServiceNeeded())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(last_service_date, current_mileage,
                                         last_service_mileage)
        self.assertTrue(car.ServiceNeeded())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(last_service_date, current_mileage,
                                         last_service_mileage)
        self.assertFalse(car.ServiceNeeded())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            last_service_date, warning_light_is_on)
        self.assertTrue(car.ServiceNeeded())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            last_service_date, warning_light_is_on)
        self.assertFalse(car.ServiceNeeded())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = CarFactory.create_palindrome(
            last_service_date, warning_light_is_on)
        self.assertTrue(car.ServiceNeeded())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            last_service_date, warning_light_is_on)
        self.assertFalse(car.ServiceNeeded())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(last_service_date, current_mileage,
                                          last_service_mileage)
        self.assertTrue(car.ServiceNeeded())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(last_service_date, current_mileage,
                                          last_service_mileage)
        self.assertFalse(car.ServiceNeeded())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_rorschach(last_service_date, current_mileage,
                                          last_service_mileage)
        self.assertTrue(car.ServiceNeeded())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(last_service_date, current_mileage,
                                          last_service_mileage)
        self.assertFalse(car.ServiceNeeded())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.ServiceNeeded())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.ServiceNeeded())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.ServiceNeeded())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.ServiceNeeded())


if __name__ == '__main__':
    unittest.main()
