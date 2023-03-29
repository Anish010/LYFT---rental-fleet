from datetime import datetime
from abc import ABC
import service_date
from car import Car


class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def ServiceNeeded(self):
        date_limit_for_service = service_date(self.last_service_date, 4)
        if date_limit_for_service < self.current_date:
            return True
        else:
            return False
