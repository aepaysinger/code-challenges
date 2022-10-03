class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


    def how_many(self, listeners):
        number_of_new_listeners = 0

        for name in listeners:
            names_of_listeners = []
            name.lower()
            if name not in names_of_listeners:
                number_of_new_listeners += 1
                names_of_listeners.append(name)

        return number_of_new_listeners
