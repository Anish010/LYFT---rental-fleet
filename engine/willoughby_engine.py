from engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self,  current_mileage, last_service_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def ServiceNeeded(self):
        return self.current_mileage - self.last_service_mileage > 60000
