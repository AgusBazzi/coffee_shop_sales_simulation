class Results:
    def __init__(self, simulation):
        emptyArray = [0 for _ in range(simulation.controlVariables.servingEmployees)]

        self.simulation = simulation

        # Simulation results
        self.idleTimePercentages = emptyArray
        self.meanWaitingTime = 0
        self.meanWaitingTimeDueToQueue = 0
        self.waitingTimeDueToQueuePercentage = 0
        self.meanWaitingTimeDueToGrinding = 0
        self.waitingTimeDueToGrindingPercentage = 0
        self.waitingDueToGrindingPercentage = 0
        self.grindedCoffeeRatio = 0

        # Intermediate results
        self.totalCustomers = 0

        self.idleStartTimes = emptyArray.copy()
        self.totalIdleTimes = emptyArray.copy()

        self.totalArriveTimes = 0
        self.totalDepartTimes = 0
        self.totalServeTimes = 0
        self.totalWaitingGrindingTimes = 0

        self.totalGrindedCoffee = 0
        self.totalConsumedCoffee = 0

        self.totalWaitingGrinding = 0

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

        self.waitingTimeDueToQueuePercentage = (
            self.meanWaitingTimeDueToQueue / self.meanWaitingTime * 100
        )

        self.meanWaitingTimeDueToGrinding = (
            self.totalWaitingGrindingTimes
        ) / self.totalCustomers

        self.waitingTimeDueToGrindingPercentage = (
            self.meanWaitingTimeDueToGrinding / self.meanWaitingTime * 100
        )

        self.waitingDueToGrindingPercentage = (
            self.totalWaitingGrinding / self.totalCustomers * 100
        )

        self.grindedCoffeeRatio = self.totalConsumedCoffee / self.totalGrindedCoffee

    def __str__(self):
        return """
        • Total Customers: {self.totalCustomers}
        
        • Idle Time Percentages Per Box (%): {self.idleTimePercentages}
        
        • Mean Waiting Time (minutes): {self.meanWaitingTime}
            
        • Waiting Time Due To Queue:
            - Mean in minutes: {self.meanWaitingTimeDueToQueue}
            - Percentage (%): {self.waitingTimeDueToQueuePercentage}
        
        • Waiting Time Due To Grinding:
            - Mean in minutes: {self.meanWaitingTimeDueToGrinding}
            - Percentage (%): {self.waitingTimeDueToGrindingPercentage}
        
        • Clients that had to wait due to grinding percentage (%): {self.waitingDueToGrindingPercentage}
        
        • Grinded Coffee Ratio: {self.grindedCoffeeRatio}
        """.format(
            self=self
        )
