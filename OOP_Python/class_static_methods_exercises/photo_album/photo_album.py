import math


class PhotoAlbum:
    COUNT_PHOTOS_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        current_pages = math.ceil(photos_count / cls.COUNT_PHOTOS_PAGE)
        return cls(current_pages)

    def add_photo(self, label: str):
        if all([True if len(x) == self.COUNT_PHOTOS_PAGE else False for x in self.photos]):
            return "No more free slots"
        for i in range(len(self.photos)):
            if len(self.photos[i]) < self.COUNT_PHOTOS_PAGE:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {self.photos[i].index(label) + 1}"
                # return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"

    def display(self):
        separator = f"-----------"
        result = [separator]

        for i in range(len(self.photos)):
            result.append(("[] " * len(self.photos[i])).rstrip())
            result.append(separator)

        return '\n'.join(result)
