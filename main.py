from math import sin, cos
from matplotlib import pyplot as plt
from random import randrange, random

class Print_Iface:
    def shoot_cannonball(self, x, y):
        print("The ball is at (%.1f, %.1f)" % (x, y))
        plt.scatter(x, y)
        plt.pause(.01)

## Represent a cannonball, tracking its position and velocity.
#
class Cannonball:
    print_iface_cls = Print_Iface
    ## Create a new cannonball at the provided x position.
    #  @param x the x position of the ball
    #
    def __init__(self, x):
        self.print_iface = self.print_iface_cls() #Has-A Print_Iface
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0

    ## Move the cannon ball, using its current velocities.
    #  @param sec the amount of time that has elapsed.
    #
    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec

        self._vy = self._vy - grav * sec

        self._x = self._x + dx
        self._y = self._y + dy

    ## Get the current x position of the ball.
    #  @return the x position of the ball
    #
    def getX(self):
        return self._x

    ## Get the current y position of the ball.
    #  @return the y position of the ball
    #
    def getY(self):
        return self._y

    ## Shoot the canon ball.
    #  @param angle the angle of the cannon
    #  @param velocity the initial velocity of the ball
    #
    def shoot(self, angle, velocity, user_grav):
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)

        while self.getY() > 1e-14:
            self.print_iface.shoot_cannonball(self.getX(), self.getY())
            self.move(0.1, user_grav)


class Crazyball(Cannonball):
    def __init__(self, x):
        super().__init__(x)
        self.rand_q = None

    def move(self, sec, grav=9.81):
        super().move(sec, grav=9.81)
        self.rand_q = randrange(0, 10)
        dx = self._vx * sec
        if self.getX() < 400:
            dx += self.rand_q
            self._x = self._x + dx
        print(f"Random value: {self.rand_q}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ##
    #  Demonstrate the cannonball class.
    #
    #from cannonball import Cannonball

    done = False
    while not done:
        angle = float(input("Enter starting angle: "))
        v = float(input("Enter initial velocity: "))
        print("1 - Earth Gravity")
        print("2 - Moon Gravity")
        print("3 - Crazy Trajectory")
        print("4 - Quit")
        try:
            answer = int(input("Enter 1 - 4: "))
            if answer == 1:
                c = Cannonball(0)
                c.shoot(angle, v, 9.81)
            elif answer == 2:
                d = Cannonball(0)
                d.shoot(angle, v, 1.625)
            elif answer == 3:
                crazy = Crazyball(0)
                crazy.shoot(angle, v, 9.81)
            elif answer == 4:
                print("goodbye")
                done = True
            else:
                print("Invalid answer: enter 1 - 4 only")
        except ValueError: print("Invalid answer: enter 1 - 4 only")



