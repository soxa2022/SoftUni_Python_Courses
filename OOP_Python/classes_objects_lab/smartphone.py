# class Smartphone:
#
#     def __init__(self, memory: int):
#         self.memory = memory
#         self.apps = []
#         self.is_on = False
#
#     def power(self):
#         if not self.is_on:
#             self.is_on = True
#         else:
#             self.is_on = False
#
#     def install(self, app: str, app_memory: int):
#         if self.memory >= app_memory:
#             if self.is_on:
#                 self.memory -= app_memory
#                 self.apps.append(app)
#                 return f"Installing {app}"
#             return f"Turn on your phone to install {app}"
#         return f"Not enough memory to install {app}"
#
#     def status(self):
#         return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

class Smartphone:

    def __init__(self, memory: int):
        self.memory_used = 0
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int):
        if not self.is_on:
            return f"Turn on your phone to install {app}"
        if self.calc_memory_left() < app_memory:
            return f"Not enough memory to install {app}"
        self.memory_used += app_memory
        self.apps.append(app)
        return f"Installing {app}"

    def status(self):
        count_apps = len(self.apps)
        memory_left = self.calc_memory_left()
        return f"Total apps: {count_apps}. Memory left: {memory_left}"

    def calc_memory_left(self):
        return self.memory - self.memory_used


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
