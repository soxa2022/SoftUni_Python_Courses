from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in [s.name for s in self.tasks]:
            return f"Could not find task with the name {task_name}"
        else:
            for element in self.tasks:
                if task_name == element.name:
                    element.completed = True
                    return f"Completed task {task_name}"

    def clean_section(self):
        count_tasks = len(self.tasks)
        completed_tasks = len([s.completed for s in self.tasks if not s.completed])
        return f"Cleared {count_tasks - completed_tasks } tasks."

    def view_section(self):
        result = ''
        result += f'Section {self.name}:\n'
        for element in self.tasks:
            result += element.details() + "\n"
        return result


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
