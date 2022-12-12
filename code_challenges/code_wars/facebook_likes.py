class LikesAmount:
    def __init__(self, friends):
        self.friends = friends

    def like(self):

        if len(self.friends) == 0:
            return "no one likes this"
        elif len(self.friends) == 1:
            return f"{self.friends[0]} likes this"
        elif len(self.friends) == 2:
            return f"{self.friends[0]} and {self.friends[1]} like this"
        elif len(self.friends) == 3:
            return (
                f"{self.friends[0]}, {self.friends[1]} and {self.friends[2]} like this"
            )
        elif len(self.friends) >= 4:
            return f"{self.friends[0]}, {self.friends[1]} and {len(self.friends) - 2} others like this"


def likes(names):
    who_likes_it = LikesAmount(names)

    return who_likes_it.like()


if __name__ == "__main__":
    names = ["Max", "John", "Mark"]
    print(likes(names))
