class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self._names_of_listeners = set()

    def how_many(self, listeners):
        number_of_new_listeners = 0
        for name in listeners:
            name = name.lower()
            if name not in self._names_of_listeners:
                number_of_new_listeners += 1
                self._names_of_listeners.add(name)

        return number_of_new_listeners
