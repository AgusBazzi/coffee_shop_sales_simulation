from __future__ import annotations
from abc import ABC, abstractmethod


class Event(ABC):
    def __init__(self, type: str, simulation, occurenceTime: int):
        self.type = type
        self.simulation = simulation
        self.occurenceTime = occurenceTime

    def execute(self):
        self._advanceTime_()
        self._createUnconditionalFutureEvents_()
        self._updateState_()
        self._createConditionalFutureEvents_()

    def _advanceTime_(self):
        self.simulation.currentTime = self.occurenceTime

    @abstractmethod
    def _createUnconditionalFutureEvents_(self):
        pass

    @abstractmethod
    def _updateState_(self):
        pass

    @abstractmethod
    def _createConditionalFutureEvents_(self):
        pass

    def __str__(self):
        return f"{self.type} event at time {self.occurenceTime}"
