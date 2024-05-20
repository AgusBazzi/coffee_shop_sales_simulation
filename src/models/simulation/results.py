import matplotlib.pyplot as plt
import pandas as pd


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
        • Serving Employees: {self.simulation.controlVariables.servingEmployees}
        • Grinding Employees: {self.simulation.controlVariables.grindingEmployees}
        • Simulation Time: {self.simulation.simulationTime} minutes
        
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

    def plot(self):
        self.plotIdleTime()
        self.plotWaitingTimes()

    def plotIdleTime(self):
        plt.figure(figsize=(10, 5))
        plt.bar(
            [f"Box {i}" for i in range(1, len(self.idleTimePercentages) + 1)],
            self.idleTimePercentages,
        )
        # Add the percentage on top of each bar
        for i, value in enumerate(self.idleTimePercentages):
            plt.text(
                i,
                value - 5,
                f"{value:.2f}%",
                ha="center",
                va="bottom",
            )

        plt.ylim(0, 100)
        plt.title(
            f"Idle Time Percentages Per Box --- Serving={self.simulation.controlVariables.servingEmployees} Grinding={self.simulation.controlVariables.grindingEmployees}"
        )
        plt.ylabel("Percentage (%)")
        plt.show()

    def plotWaitingTimes(self):
        plt.figure(figsize=(10, 5))
        plt.bar(
            [
                "Mean Waiting Time",
                "Waiting Time Due To Queue",
                "Waiting Time Due To Grinding",
            ],
            [
                self.meanWaitingTime,
                self.meanWaitingTimeDueToQueue,
                self.meanWaitingTimeDueToGrinding,
            ],
        )
        for i, value in enumerate(
            [
                self.meanWaitingTime,
                self.meanWaitingTimeDueToQueue,
                self.meanWaitingTimeDueToGrinding,
            ]
        ):
            plt.text(
                i,
                value,
                f"{value:.2f}min -- {value/self.meanWaitingTime*100:.2f}%",
                ha="center",
                va="bottom",
            )
        plt.title(
            f"Waiting Times --- Serving={self.simulation.controlVariables.servingEmployees} Grinding={self.simulation.controlVariables.grindingEmployees}"
        )
        plt.ylabel("Minutes")
        plt.show()

    def printTable(self):
        data = [
            {
                "Metric": "Serving Employees",
                "Value": self.simulation.controlVariables.servingEmployees,
            },
            {
                "Metric": "Grinding Employees",
                "Value": self.simulation.controlVariables.grindingEmployees,
            },
            {"Metric": "Total Customers", "Value": self.totalCustomers},
            {
                "Metric": "Mean Idle Time Percentage",
                "Value": sum(self.idleTimePercentages) / len(self.idleTimePercentages),
            },
            {
                "Metric": "Mean Waiting Time (minutes)",
                "Value": int(self.meanWaitingTime),
            },
            {
                "Metric": "Waiting Time Due To Queue (minutes)",
                "Value": self.meanWaitingTimeDueToQueue,
            },
            {
                "Metric": "Waiting Time Due To Queue (%)",
                "Value": self.waitingTimeDueToQueuePercentage,
            },
            {
                "Metric": "Waiting Time Due To Grinding (minutes)",
                "Value": self.meanWaitingTimeDueToGrinding,
            },
            {
                "Metric": "Waiting Time Due To Grinding (%)",
                "Value": self.waitingTimeDueToGrindingPercentage,
            },
            {
                "Metric": "Clients that had to wait due to grinding (%)",
                "Value": self.waitingDueToGrindingPercentage,
            },
            {"Metric": "Grinded Coffee Ratio", "Value": self.grindedCoffeeRatio},
        ]
        return pd.DataFrame(data)

    def oneLineTable(self):
        return pd.DataFrame(
            [
                {
                    "Serving Employees": self.simulation.controlVariables.servingEmployees,
                    "Grinding Employees": self.simulation.controlVariables.grindingEmployees,
                    "Total Customers": self.totalCustomers,
                    "Mean Idle Time Percentage (%)": sum(self.idleTimePercentages)
                    / len(self.idleTimePercentages),
                    "Mean Waiting Time (minutes)": int(self.meanWaitingTime),
                    "Waiting Time Due To Queue (minutes)": self.meanWaitingTimeDueToQueue,
                    "Waiting Time Due To Queue (%)": self.waitingTimeDueToQueuePercentage,
                    "Waiting Time Due To Grinding (minutes)": self.meanWaitingTimeDueToGrinding,
                    "Waiting Time Due To Grinding (%)": self.waitingTimeDueToGrindingPercentage,
                    "Clients that had to wait due to grinding (%)": self.waitingDueToGrindingPercentage,
                    "Grinded Coffee Ratio": self.grindedCoffeeRatio,
                }
            ]
        )
