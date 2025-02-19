from abc import ABC, abstractmethod
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    @abstractmethod
    def ServiceNeeded(self):
        return self.engine.ServiceNeeded() or self.battery.ServiceNeeded() or self.tire.ServiceNeeded()
