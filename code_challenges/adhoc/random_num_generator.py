# takes 2 numbers (min and max(inclusive)). get method returns a random number between them w.o repeating
import random


class RandomNumGenerator:
    def __init__(self, min, max):
        self.choices = set(range(min, max + 1))
        
    def get(self):
        try:
            random_num = random.choice(list(self.choices))
        except IndexError:
            raise ValueError("no more choices")
        self.choices.remove(random_num)
        
        return random_num

    