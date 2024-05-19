class ControlVariables:
    def __init__(self, servingEmployees: int, grindingEmployees: int):
        self.servingEmployees = servingEmployees
        self.grindingEmployees = grindingEmployees

    def __str__(self):
        return f"ControlVariables(servingEmployees={self.servingEmployees}, grindingEmployees={self.grindingEmployees})"
