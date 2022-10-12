class Vehicle:
    def __init__(self, seats, wheels, engine):
        self.seats = seats
        self.wheels = wheels
        self.engine = engine
        self.classname = Vehicle
        

class Planet:
    def __init__(self, moon):
        self.moon = moon
        self.classname = Planet


def show_me(instance):
    reply = f"Hi, I'm one of those {instance.__class__}s! Have a look at my {instance} "
    
    return reply


#In [5]: porsche.__dict__
# Out[5]:
# {'seats': 2,
#  'wheels': 4,
#  'engine': 'Gas',
#  'classname': code_challenges.code_wars.instance.Vehicle}
 # .__class__  is returning a string