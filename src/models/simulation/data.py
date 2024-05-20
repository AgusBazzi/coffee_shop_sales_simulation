from scipy.stats import rv_continuous, norm
import random


class Data:
    def __init__(self, interarrivalTimeDist: rv_continuous):
        self.interarrivalTimeDist = interarrivalTimeDist
        self.atentionTimeDist = norm(loc=3, scale=2 / 1.96)

        # Common recommendation gr:ml is 1:15
        self.coffeeSizes = {
            "small": {
                "probability": 0.29,
                "coffeeGrams": 15,
                "additionalTime": 0,
            },
            "regular": {
                "probability": 0.36,
                "coffeeGrams": 23,
                "additionalTime": 1,
            },
            "large": {
                "probability": 0.35,
                "coffeeGrams": 31,
                "additionalTime": 2,
            },
        }

        self.coffeeQuantities = {
            "1": {
                "probability": 0.49,
            },
            "2": {
                "probability": 0.51,
            },
        }

        self.grindingFrequency = 10
        self.grindingVelocity = 3

    def generateInterarrivalTime(self):
        value = self.interarrivalTimeDist.rvs()
        return value

    def generateAtentionTime(self):
        return self.atentionTimeDist.rvs()

    def generateCoffeeSize(self):
        randomValue = random.random()

        for _, data in self.coffeeSizes.items():
            if randomValue < data["probability"]:
                return data["coffeeGrams"], data["additionalTime"]

            randomValue -= data["probability"]

    def generateCoffeeQuantity(self):
        randomValue = random.random()

        for value, data in self.coffeeQuantities.items():
            if randomValue < data["probability"]:
                return int(value)

            randomValue -= data["probability"]
