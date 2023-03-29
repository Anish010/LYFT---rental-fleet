from abc import ABC, abstractmethod
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engineType = engine
        self.batteryType = battery

    @abstractmethod
    def ServiceNeeded(self):
        return self.engineType.ServiceNeeded() or self.batteryType.ServiceNeeded()
