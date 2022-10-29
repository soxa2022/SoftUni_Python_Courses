from project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = [*args]

    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        if song_name not in [x.name for x in self.songs]:
            return f"Song is not in the album."
        self.songs = [s for s in self.songs if not s.name == song_name]
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]
        for s in self.songs:
            result.append(f'== {s.get_info()}')
        return '\n'.join(result) + '\n'
