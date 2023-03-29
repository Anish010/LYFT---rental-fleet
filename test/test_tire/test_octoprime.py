import unittest
from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        sensor_data = [2, 1, 0.1, 1]
        engine = OctoprimeTire(sensor_data)
        self.assertTrue(engine.ServiceNeeded())

    def test_engine_should_not_be_serviced(self):
        sensor_data = [0, 0.2, 1.1, 0.3]
        engine = OctoprimeTire(sensor_data)
        self.assertFalse(engine.ServiceNeeded())
