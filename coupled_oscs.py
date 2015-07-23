from visual import *
def get_input():
    try:
        x1 = input("Displace mass 1 by (e.g. -1): ")
        mass1.pos.x += x1
        x2 = input("Displace mass 2 by (e.g. 0): ")
        mass2.pos.x += x2
        x3 = input("Displace mass 3 by: (e.g. 1): ")
        mass3.pos.x += x3
    except:
        print "Invalid value! Try again."
        get_input()
    
        
def displacement(object1,object2): #diplacement from equilibrium
    disp = object1.pos.x - object2.pos.x 
    return disp - sign(disp)*equi
scene.visible = False

equi = 8

mass1 = box(pos = vector(-8,0), color = color.red, size = (4,4,4), M = 5, p =0)
mass2 = box(pos = vector(0,0), color = color.blue, size = (4,4,4), M = 5, p =0)
mass3 = box(pos = vector(8,0), color = color.green, size = (4,4,4),M = 5, p=0)
spring1 = helix(pos = mass1.pos, length = abs( mass1.pos.x - mass2.pos.x), thickness = 0.3)
spring2 = helix(pos = mass2.pos, length = abs( mass3.pos.x - mass2.pos.x), thickness = 0.3)
t = 0
dt = 0.01
k_s = 5
floor = box(pos = (0,-3), size = (25,2,4))


get_input()

scene.visible = True
while True:#t<10:
    rate(150)
       
    force1 = - k_s * displacement(mass1,mass2)
    mass1.p += force1*dt
    mass1.pos.x += mass1.p*dt/mass1.M
    spring1.pos.x = mass1.pos.x + mass1.size.x/2
    spring1.length = abs( mass1.pos.x - mass2.pos.x)

    force2 = - k_s * (displacement(mass2,mass1) + displacement(mass2,mass3))
    mass2.p += force2*dt
    mass2.pos.x += mass2.p*dt/mass2.M
    spring1.length = abs( mass1.pos.x - mass2.pos.x)
    spring2.pos.x = mass2.pos.x + mass2.size.x/2
    
    force3 = - k_s * displacement(mass3,mass2)
    mass3.p += force3*dt
    mass3.pos.x += mass3.p*dt/mass3.M
    spring2.length = abs(mass3.pos.x - mass2.pos.x)

    #t += dt
    
