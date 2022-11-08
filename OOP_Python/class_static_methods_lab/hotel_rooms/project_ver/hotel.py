from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [x for x in self.rooms if x.number == room_number]
        if room:
            if room[0].take_room(people) is None:
                self.guests += people

    def free_room(self, room_number):
        room = [x for x in self.rooms if x.number == room_number]
        if room:
            room_guests = room[0].guests
            if room[0].free_room() is None:
                self.guests -= room_guests

    def status(self):
        result = [f"Hotel {self.name} has {self.guests} total guests"]
        result.append(f"Free rooms: {', '.join([str(x.number) for x in self.rooms if not x.is_taken])}")
        result.append(f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}")
        return '\n'.join(result)
