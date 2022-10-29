class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    # def next_second(self):
    #     if self.seconds == self.max_seconds:
    #         self.seconds = 0
    #         if self.minutes == self.max_minutes:
    #             self.minutes = 0
    #             if self.hours == self.max_hours:
    #                 self.hours = 0
    #             else:
    #                 self.hours += 1
    #         else:
    #             self.minutes += 1
    #     else:
    #         self.seconds += 1
    #
    #     return self.get_time()

    def next_second(self):
        self.seconds += 1
        self.validation_time()
        return self.get_time()

    def validation_time(self):
        if self.seconds > self.max_seconds:
            self.seconds = 0
            self.minutes += 1

            if self.minutes > self.max_minutes:

                self.minutes = 0
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 0


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
