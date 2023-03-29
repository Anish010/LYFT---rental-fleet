from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def ServiceNeeded(self):
        pass
