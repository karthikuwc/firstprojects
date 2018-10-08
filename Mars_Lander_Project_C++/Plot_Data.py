# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np


import matplotlib.pyplot as plt

Kh = '0.018000'
scenario = 1
results = np.loadtxt('/Users/admin/Dropbox/Cambridge/1A/Computing/MarsLander/landerproject/alt_actual_descent_rate_data_Kh_' + str(Kh) +'_scenario_'+ str(scenario) + '.txt')
plt.figure(1)
plt.clf()
plt.xlabel('Altitude (m)')
plt.grid()
plt.plot(results[:, 0], results[:, 1], label='altitude vs descent rate')

plt.legend()
plt.show()
