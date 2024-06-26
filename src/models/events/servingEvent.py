from abc import ABC


class ServingEvent(ABC):
    def __init__(self, simulation):
        self.simulation = simulation

    def serve(self, box: int):
        self.simulation.results.totalServeTimes += self.simulation.currentTime

        coffeeGrams, additionalTime = self.simulation.data.generateCoffeeSize()
        coffeeQty = self.simulation.data.generateCoffeeQuantity()

        totalGrams = coffeeGrams * coffeeQty
        self.simulation.results.totalConsumedCoffee += totalGrams

        individualAttentionTime = (
            self.simulation.data.generateAtentionTime() + additionalTime
        )
        attentionTime = individualAttentionTime * coffeeQty

        if self.simulation.state.groundCoffeeStock < totalGrams:
            requiredGrinding = totalGrams - self.simulation.state.groundCoffeeStock
            self.simulation.results.totalGrindedCoffee += requiredGrinding
            grindingTime = requiredGrinding / self.simulation.data.grindingVelocity
            self.simulation.results.totalWaitingGrindingTimes += grindingTime
            self.simulation.results.totalWaitingGrinding += 1
            attentionTime += grindingTime

        self.simulation.state.decreaseGroundCoffeeStock(totalGrams)

        self.simulation.futureEvents.scheduleNextDeparture(
            self.simulation.currentTime + attentionTime, box
        )
