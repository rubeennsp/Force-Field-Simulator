# Ruben Solomon Partono
# make sure you check out the website that introduced me to physics simulations
# http://buildnewgames.com/gamephysics/
import math


class Body:
    # constructor

    GRAVITY = 0

    def __init__(self, initial_position, initial_velocity, initial_force, initial_mass):
        x, y = initial_position
        self.xpos = float(x)
        self.ypos = float(y)
        x, y = initial_velocity
        self.xvel = float(x)
        self.yvel = float(y)
        x, y = initial_force
        self.xforce = float(x)
        self.yforce = float(y)
        self.mass = float(initial_mass)
        self.xacc = self.xforce / self.mass
        self.yacc = self.yforce / self.mass
        self.color = [0,0,0]
        self.type = "BODY"

        self.forceDict = {}

    # Haven't figured this out.
    # The Body object should keep a list of all the forces working on it,
    # and this updateforce method is supposed to refresh that list.
    # But for the time being we're okay with only one force working:
    # The click force.
    def updateforce(self):
        self.xacc = self.xforce / self.mass
        self.yacc = self.yforce / self.mass

    # This should be generelized, not to work for just force generated from clicks.
    # After all we'd want various types of forces:
    # damping, springs, magnets, gravity, friction, etc.
    def clickforce(self, magnitude, xsource, ysource):
        GRAVITY = 0
        deltax = float(xsource)/100.0 - self.xpos
        deltay = float(ysource)/100.0 - self.ypos
        angle = math.atan2(deltay,deltax)
        if deltax != 0 or deltay != 0:
            self.xforce = float(magnitude)*math.cos(angle)
            self.yforce = float(magnitude)*math.sin(angle) + GRAVITY
        else:
            self.xforce = 0
            self.yforce = GRAVITY
        self.updateforce()

    # Vertlet Integration:
    # This calculates the position, velocity, and acceleration of the Body
    # after the specified time steps.
    # The Vertlet Integration is more accurate than the Euler Integration.
    # However Runge Kutta is more accurate than Vertlet.
    def vertletstep(self,time_step):
        lastxacc = self.xacc
        lastyacc = self.yacc
        self.xpos = self.xpos + self.xvel*time_step + (0.5 * lastxacc * time_step**2)
        self.ypos = self.ypos + self.yvel*time_step + (0.5 * lastyacc * time_step**2)
        self.updateforce()
        newxacc = self.xacc
        newyacc = self.yacc
        self.xvel += (lastxacc+newxacc)*time_step/2.0
        self.yvel += (lastyacc+newyacc)*time_step/2.0

"""
#these were for testing. Go ahead, try unquoting this and run the phile
abody = Body([0.0,0.0], [1.0,1.0], [13.4,-2.3], 3.0)
print "position is (%d,%d)" %(abody.xpos, abody.ypos)
print "velocity is (%d,%d)" %(abody.xvel, abody.yvel)
print "force is (%d, %d)" %(abody.xforce, abody.yforce)
print "acceleration is (%d,%d)" %(abody.xacc, abody.yacc)
print "How many vertlet steps do you want to do?"
steps = raw_input(">>>")
for i in range (int(steps)):
    raw_input("...")
    print "position is (%f,%f)." %(abody.xpos, abody.ypos),
    print "velocity is (%f,%f)" %(abody.xvel, abody.yvel)
    abody.vertletstep(0.1)
"""
