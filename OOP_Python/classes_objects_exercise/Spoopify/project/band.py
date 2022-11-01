from project.album import Album
from project.song import Song


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        check_album = [x for x in self.albums if x.name == album_name]

        if not check_album:
            return f"Album {album_name} is not found."

        if check_album[0].published:
            return f"Album has been published. It cannot be removed."

        self.albums.remove(check_album[0])
        return f"Album {album_name} has been removed."

    def details(self):
        result = [f"Band {self.name}"]
        [result.append(f"{x.details()}") for x in self.albums]
        return "\n".join(result)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
