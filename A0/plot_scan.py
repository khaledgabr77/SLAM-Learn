import matplotlib.pyplot as plt
from lego_robot import*

from matplotlib import *



logfile = LegoLogfile()
logfile.read("robot4_scan.txt")


plt.plot(logfile.scan_data[7])
plt.show()
