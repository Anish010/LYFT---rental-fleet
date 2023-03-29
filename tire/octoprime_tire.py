from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def ServiceNeeded(self):
        return sum(self.sensor_data) >= 3
