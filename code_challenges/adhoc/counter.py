# create a counter that has an incriment , decremet, and value method (return current value)
class Counter:
    def __init__(self):
        self._value = 0

    def value(self):
        return self._value

    def increment(self):
        self._value += 1

    def decrement(self):
        self._value -= 1
