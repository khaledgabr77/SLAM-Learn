#plot the ticks from left and right motors.
#28/6/2020
#Read all value from file left and right motors.
#left motor L2 && right motor R6


from pylab import *
f = open("robot4_motors.txt")
left_list = []
right_list = []
for l in f:
    sp = l.split()
   
    left_list.append(int(sp[2]))
    right_list.append(int(sp[6]))

plot(left_list)
plot(right_list)    
show()
