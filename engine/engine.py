from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def ServiceNeeded(self):
        pass
