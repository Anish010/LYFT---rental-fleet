from datetime import datetime
from battery import service_date
from battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def ServiceNeeded(self):
        date_limit_for_service = service_date(self.last_service_date, 4)
        if date_limit_for_service < self.current_date:
            return True
        else:
            return False
