from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum(x.guests for x in self.rooms)

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [x for x in self.rooms if x.number == room_number]
        if room:
            return room[0].take_room(people)

    def free_room(self, room_number):
        room = [x for x in self.rooms if x.number == room_number]
        room_guest = room[0].guests
        if room:
            room[0].guests -= room_guest
            return room[0].free_room()


def status(self):
    result = [f"Hotel {self.name} has {self.guests} total guests"]
    result.append(f"Free rooms: {', '.join([str(x.number) for x in self.rooms if not x.is_taken])}")
    result.append(f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}")
    return '\n'.join(result)
