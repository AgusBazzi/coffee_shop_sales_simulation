from .event import Event


class GrindingEvent(Event):
    def __init__(self, simulation, occurenceTime):
        self.simulation = simulation
        self.occurenceTime = occurenceTime
        self.type = "Grinding"

    def _createConditionalFutureEvents_(self):
        nextGrindingTime = (
            self.simulation.currentTime + self.simulation.data.grindingFrequency
        )
        self.simulation.futureEvents.scheduleNextGrinding(nextGrindingTime)

    def _updateState_(self):
        employees = self.simulation.controlVariables.grindingEmployees
        velocity = self.simulation.data.grindingVelocity
        minutes = self.simulation.data.grindingFrequency
        self.simulation.state.increaseGroundCoffeeStock(employees * velocity * minutes)

    def _createUnconditionalFutureEvents_(self):
        return
