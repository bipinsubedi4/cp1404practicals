import datetime
from project import Project

FILENAME = "projects.txt"


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            name, start_date, priority, cost, completion = line.strip().split("\t")
            projects.append(Project(name, start_date, int(priority), float(cost), int(completion)))
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion}\n")


def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")
    print("Completed projects:")
    for project in sorted(complete):
        print(f"  {project}")


def filter_projects_by_date(projects, date_str):
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    print(f"Projects starting on or after {date_str}:")
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(f"  {project}")


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion = int(input("Completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))
    print(f"Added project: {name}")


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} - {project}")
    choice = int(input("Project choice: "))
    selected_project = projects[choice]

    new_completion = int(input("New completion percentage: "))
    selected_project.update_completion(new_completion)

    new_priority = int(input("New priority: "))
    selected_project.update_priority(new_priority)
    print(f"Updated project: {selected_project}")


def main():
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

    choice = input(menu + "\n>>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice.")
        choice = input(menu + "\n>>> ").lower()

    if input("Save changes before quitting? (y/n): ").lower() == 'y':
        save_projects(FILENAME, projects)
        print(f"Projects saved to {FILENAME}")
    print("Thank you for using the project management software.")


if __name__ == "__main__":
    main()
