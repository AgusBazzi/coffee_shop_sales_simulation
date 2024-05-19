from ..events.arrivalEvent import ArrivalEvent
from ..events.departEvent import DepartEvent
from ..events.grindingEvent import GrindingEvent
from ..events.event import Event

HV = 99999999


class FutureEvents:
    def __init__(self, simulation, servingEmployees: int):
        self.simulation = simulation
        self.nextArrive = ArrivalEvent(simulation, 30)
        self.nextDeparts = [
            DepartEvent(simulation, HV, i) for i in range(servingEmployees)
        ]
        self.nextGrinding = GrindingEvent(simulation, 10)

    def scheduleNextArrival(self, time):
        self.nextArrive = ArrivalEvent(self.simulation, time)

    def stopArrivals(self):
        self.nextArrive = ArrivalEvent(self.simulation, HV)

    def scheduleNextDeparture(self, time, employee):
        self.nextDeparts[employee] = DepartEvent(self.simulation, time, employee)

    def getFirstFreeEmployee(self):
        for i, depart in enumerate(self.nextDeparts):
            if depart.occurenceTime == HV:
                return i
        return None

    def scheduleNextGrinding(self, time):
        self.nextGrinding = GrindingEvent(self.simulation, time)

    def getNextEvent(self) -> Event:
        allEvents = [self.nextGrinding] + [self.nextArrive] + self.nextDeparts
        return min(allEvents, key=lambda x: x.occurenceTime)

    def __str__(self):
        return f"FutureEvents(nextArrive={self.nextArrive}, nextDepart={self.nextDeparts}, nextGrinding={self.nextGrinding})"
