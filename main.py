from src.models.simulation.simulation import Simulation
from src.data.interarrivalTimeDist import winterDist, springDist


def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive integer.")


def get_user_input():
    servingEmployees = get_positive_integer_input("Number of serving employees: ")
    grindingEmployees = get_positive_integer_input("Number of grinding employees: ")
    simulationTimeWorkingDays = get_positive_integer_input(
        "Simulation time (working days): "
    )

    return servingEmployees, grindingEmployees, simulationTimeWorkingDays


def main(
    defaultServingEmployees=2,
    defaultGrindingEmployees=1,
    defaultSimulationTime=365,
    defaultSeason="Both",
    defaultOutput="verbose",
):
    servingEmployees = defaultServingEmployees
    grindingEmployees = defaultGrindingEmployees
    simulationTimeWorkingDays = defaultSimulationTime
    season = defaultSeason

    if defaultOutput != "quiet":
        print("Welcome to the Coffee Shop Simulation")
        while True:
            print("\nThis is the current configuration:")
            print(f"• Serving Employees: {servingEmployees}")
            print(f"• Grinding Employees: {grindingEmployees}")
            print(f"• Simulation Time: {simulationTimeWorkingDays} working days")

            proceed = (
                input("\nDo you want to enter another set of details? (yes/no): ")
                .strip()
                .lower()
            )
            if proceed != "yes":
                break

            servingEmployees, grindingEmployees, simulationTimeWorkingDays = (
                get_user_input()
            )
            print(
                "--------------------------------------------------------------------------"
            )

    simulationTimeMinutes = simulationTimeWorkingDays * 8 * 60

    winterSimulation = Simulation(
        simulationTimeMinutes, servingEmployees, grindingEmployees, winterDist
    )
    springSimulation = Simulation(
        simulationTimeMinutes, servingEmployees, grindingEmployees, springDist
    )

    print("--------------------------------------------------------------------------")

    if season != "Spring":
        winterSimulation.start()

    if season != "Winter":
        springSimulation.start()

    if defaultOutput != "quiet":
        print("WINTER SIMULATION RESULTS")
        print(winterSimulation.results)

        print("SPRING SIMULATION RESULTS:")
        print(springSimulation.results)

    return winterSimulation, springSimulation


if __name__ == "__main__":
    main()
