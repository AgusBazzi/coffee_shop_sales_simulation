class Results:
    def __init__(self, simulation):
        emptyArray = [0 for _ in range(simulation.controlVariables.servingEmployees)]

        self.simulation = simulation

        # Simulation results
        self.idleTimePercentages = emptyArray
        self.meanWaitingTime = 0
        self.meanWaitingTimeDueToQueue = 0
        self.meanWaitingTimeDueToGrinding = 0

        # Intermediate results
        self.idleStartTimes = emptyArray.copy()
        self.totalIdleTimes = emptyArray.copy()

        self.totalArriveTimes = 0
        self.totalDepartTimes = 0
        self.totalServeTimes = 0
        self.totalWaitingGrindingTimes = 0
        self.totalCustomers = 0

    def calculateFinalResults(self):
        self.idleTimePercentages = [
            totalIdleTime / self.simulation.currentTime * 100
            for totalIdleTime in self.totalIdleTimes
        ]

        self.meanWaitingTime = (
            self.totalDepartTimes - self.totalArriveTimes
        ) / self.totalCustomers

        self.meanWaitingTimeDueToQueue = (
            self.totalServeTimes - self.totalArriveTimes
        ) / self.totalCustomers

        self.meanWaitingTimeDueToGrinding = (
            self.totalWaitingGrindingTimes
        ) / self.totalCustomers

    def __str__(self):
        return """
        - Idle Time Percentages Per Box (%): {self.idleTimePercentages}
        
        - Mean Waiting Time (minutes): {self.meanWaitingTime}
        - Mean Waiting Time Due To Queue (minutes): {self.meanWaitingTimeDueToQueue}
        - Mean Waiting Time Due To Grinding (minutes): {self.meanWaitingTimeDueToGrinding}
        """.format(
            self=self
        )
