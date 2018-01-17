class Rocket():
    """
    ATTRIBUTES
    location
    starting location
    fuel

    METHODS
    move
    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.vel_x = 1
        self.vel_y = 15
        self.grav = -1
        self.fuel = 100

a = Rocket()
b = Rocket()

def move(self):
    """One unit of time passes"""
    if self.y >= 0:
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += self.grav
    if self.fuel > 0:
        self.vel_y += self.boost
        self.fuel -= 0.5

def status(self):
    print(f"Location: {self.x}, {self.y}")
    print(f"Velocity: {self.vel_x}, {self.vel_y}")
    print(f"Fuel: {round(self.fuel, 2)}%")


for x in range(2000):
    a.move()
    if x % 10 == 0:
        a.status()
