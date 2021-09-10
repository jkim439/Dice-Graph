__author__ = 'Junghwan Kim'
__copyright__ = 'Copyright 2016-2018 Junghwan Kim. All Rights Reserved.'
__version__ = '1.0.0'

import numpy as np
import matplotlib.pyplot as plt

# Average
dice_ave = (0.9, 0.79, 0.74, 0.9, 0.69, 0.74, 0.75, 0.53, 0.67, 0.66, 0.84, 0.78, 0.62, 0.87, 0.8, 0.8, 0.69, 0.68, 0.81, 0.7, 0.54)

# Standard deviation
dice_std = (0.059, 0.169, 0.166, 0.052, 0.157, 0.092, 0.087, 0.161, 0.128, 0.267, 0.048, 0.198, 0.25, 0.139, 0.115, 0.077, 0.157, 0.111, 0.029, 0.228, 0.268)

# User configuration
width = 1920    # image width (px)
height = 1080    # image height (px)
number = 21    # the number of x axis
bar_width = 0.5    # width of bar graph
title = '20181029115554726150'
label = ('FL', 'PL', 'OL', 'TL', 'CC', 'CN', 'LN', 'IC', 'Insula', 'Thalamus', 'Midbrain', 'Pons', 'Medulla', 'Cbll', 'LatV', '3rdV', '4thV', 'BasalC', 'SylvF', 'QuadC', 'CPcist')
legend = 'Dice'

# DO NOT CHANGE
ind = np.arange(number)
fig = plt.figure()
ax = fig.add_subplot(111)
fig.set_size_inches(float(width)/100, float(height)/100)

rects = ax.bar(ind, dice_ave, bar_width, yerr=dice_std, color='IndianRed', error_kw=dict(ecolor='gray', lw=1, capsize=2, capthick=1))

ax.set_title(title)
ax.set_xticklabels(label)
ax.set_xticks(ind)
ax.legend(['Dice'])
ax.set_ylim(0, 1.2)


def create_label(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, 1.01 * h, '{}'.format(h), ha='center', va='bottom')


create_label(rects)

plt.show()
