from .servingEvent import ServingEvent
from .event import Event


class DepartEvent(Event, ServingEvent):
    def __init__(self, simulation, occurenceTime, box: int):
        super().__init__(
            type="Depart", simulation=simulation, occurenceTime=occurenceTime
        )
        self.box = box

    def _advanceTime_(self):
        super()._advanceTime_()
        self.simulation.results.totalDepartTimes += self.occurenceTime

    def _createUnconditionalFutureEvents_(self):
        return

    def _updateState_(self):
        self.simulation.state.decreaseCustomers()

    def _createConditionalFutureEvents_(self):
        if (
            self.simulation.state.customers
            >= self.simulation.controlVariables.servingEmployees
        ):
            self.serve(self.box)
        else:
            self.simulation.futureEvents.scheduleNextDeparture(99999999, self.box)
            self.simulation.results.idleStartTimes[self.box] = (
                self.simulation.currentTime
            )
