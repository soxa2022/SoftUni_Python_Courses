from project.song import Song


class Album:

    def __init__(self, name: str, *args):
        self.name = name
        # self.songs = [*args]
        self.songs = list(args)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song = [x for x in self.songs if x.name == song_name]
        if self.published:
            return "Cannot remove songs. Album is published."

        if not song:
            return "Song is not in the album."

        self.songs.remove(song[0])
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]
        [result.append(f"== {x.get_info()}") for x in self.songs]
        return '\n'.join(result)
