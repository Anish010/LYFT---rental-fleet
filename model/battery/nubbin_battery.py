from datetime import datetime
from abc import ABC

from car import Car


class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()

    def battery_should_be_serviced(self):
        if self.current_date - self.last_service_date >= 4:
            return True
        else:
            return False
