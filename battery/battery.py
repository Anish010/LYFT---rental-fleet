from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def ServiceNeeded(self):
        pass
