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
        result = [x for x in self.tasks if x.name == task_name]
        # try:
        #   result = next(filter(lambda x: x.name == task_name, self.tasks))
        # except StopIteration:
        #   return f"Could not find task with the name {task_name}"

        if not result:
            return f"Could not find task with the name {task_name}"
        result[0].completed = True
        # result.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        # remove_tasks = 0
        # for t in filter(lambda x: x.completed,self.tasks):
        #     self.tasks.remove(t)
        #     remove_tasks += 1
        removed_tasks = len(self.tasks) - len([x for x in self.tasks if not x.completed])
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        # [result.append(el.details()) for el in self.tasks]
        for el in self.tasks:
            result.append(el.details())
        return '\n'.join(result)


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
