from .servingEvent import ServingEvent
from .event import Event


class ArrivalEvent(Event, ServingEvent):
    def __init__(self, simulation, occurenceTime):
        super().__init__(
            type="Arrival", simulation=simulation, occurenceTime=occurenceTime
        )

    def _advanceTime_(self):
        super()._advanceTime_()
        self.simulation.results.totalCustomers += 1
        self.simulation.results.totalArriveTimes += self.occurenceTime

    def _createUnconditionalFutureEvents_(self):
        interarrivalTime = self.simulation.data.generateInterarrivalTime()
        nextArrivalTime = self.simulation.currentTime + interarrivalTime
        self.simulation.futureEvents.scheduleNextArrival(nextArrivalTime)

    def _updateState_(self):
        self.simulation.state.increaseCustomers()

    def _createConditionalFutureEvents_(self):
        if (
            self.simulation.state.customers
            <= self.simulation.controlVariables.servingEmployees
        ):
            assignedBox = self.simulation.futureEvents.getFirstFreeEmployee()
            self.serve(assignedBox)

            idleTime = (
                self.simulation.currentTime
                - self.simulation.results.idleStartTimes[assignedBox]
            )

            self.simulation.results.totalIdleTimes[assignedBox] = (
                self.simulation.results.totalIdleTimes[assignedBox] + idleTime
            )
