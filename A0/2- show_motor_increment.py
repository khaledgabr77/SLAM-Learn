from lego_robot import LegoLogfile
from pylab import*

logfile = LegoLogfile()
logfile.read("robot4_motors.txt")
#print (logfile.motor_ticks)

for i in range (40):
    print (logfile.motor_ticks[i])

plot(logfile.motor_ticks)    
show()