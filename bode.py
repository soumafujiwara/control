# coding: UTF-8

from control import matlab
from matplotlib import pyplot as plt
sys = matlab.tf([1],[1,1,1])
matlab.bode(sys)
plt.show()
