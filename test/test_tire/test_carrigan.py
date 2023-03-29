import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        sensor_data = [0, 0.2, 0.9, 0.3]
        engine = CarriganTire(sensor_data)
        self.assertTrue(engine.ServiceNeeded())

    def test_engine_should_not_be_serviced(self):
        sensor_data = [0, 0.2, 0.1, 0.3]
        engine = CarriganTire(sensor_data)
        self.assertFalse(engine.ServiceNeeded())
