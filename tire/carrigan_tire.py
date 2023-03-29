from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def ServiceNeeded(self):
        for data in self.sensor_data:
            if data >= 0.9:
                return True
        return False
