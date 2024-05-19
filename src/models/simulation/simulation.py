from scipy.stats import rv_continuous

from .controlVariables import ControlVariables
from .futureEvents import FutureEvents
from .results import Results
from .state import State
from .data import Data


class Simulation:
    def __init__(
        self,
        simulationTime: int,
        servingEmployees: int,
        grindingEmployees: int,
        interarrivalTimeDist: rv_continuous,
    ):
        self.currentTime = 0
        self.simulationTime = simulationTime

        self.data = Data(interarrivalTimeDist)
        self.controlVariables = ControlVariables(servingEmployees, grindingEmployees)
        self.state = State()
        self.results = Results(self)

        self.futureEvents = FutureEvents(self, servingEmployees)

    def start(self):
        self.executeNextEvent()

        while self.currentTime < self.simulationTime:
            self.executeNextEvent()

        self.futureEvents.stopArrivals()

        while self.state.customers != 0:
            self.executeNextEvent()

        self.printResults()

    def executeNextEvent(self):
        event = self.futureEvents.getNextEvent()
        # print(event)
        event.execute()

    def printResults(self):
        self.results.calculateFinalResults()
        # print(self.results)

    def __str__(self):
        return f"Simulation(currentTime={self.currentTime}, simulationTime={self.simulationTime})"
