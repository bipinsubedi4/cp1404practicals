from datetime import datetime

class Project:
    """Represent a project with name, start date, priority, cost, and completion."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is complete, i.e., completion is 100%."""
        return self.completion == 100

    def update_completion(self, new_completion):
        """Update the completion percentage of the project."""
        self.completion = new_completion

    def update_priority(self, new_priority):
        """Update the priority of the project."""
        self.priority = new_priority
