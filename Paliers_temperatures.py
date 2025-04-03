#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:37:10 2025

@author: justine
"""

import numpy as np
import matplotlib.pyplot as plt

temp = np.array([-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-5,-5,-5,-2.5,-2.5,-2.5,-1,-1,-1,0,0,0])
temps = np.arange(0,27,1)*60

plt.figure()
plt.plot(temps,temp)
plt.plot(temps,np.ones(27)*-15, label = "T=-15°C")
plt.plot(temps,np.ones(27)*-5, label = "T=-5°C")
plt.plot(temps,np.ones(27)*-2.5, label = "T=-2.5°C")
plt.plot(temps,np.ones(27)*-1, label = "T=-1°C")
plt.plot(temps,np.zeros(27), label = "T=0°C")
plt.legend()
plt.ylabel('T°C')
plt.xlabel('t(s)')
plt.show()