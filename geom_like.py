#!/usr/bin/env python
# coding: utf-8


# 1. Bounded


import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

p = 0.3
a = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6] #possible jitter times

for i in range(0,100):
    while True:
        try:
            q = np.random.geometric(p, size = 228) - 1 #228 is the number of jitter needed
            t = [a[k] for k in q]       
        except IndexError:
            continue
        break

print(t)

num_2 = t.count(2)
print("2 occurences:", num_2)
num_2_5 = t.count(2.5)
print("2.5 occurences:",num_2_5)
num_3 = t.count(3)
print("3 occurences:",num_3)
num_3_5 = t.count(3.5)
print("3.5 occurences:",num_3_5)
num_4 = t.count(4)
print("4 occurences:",num_4)
num_4_5 = t.count(4.5)
print("4.5 occurences:",num_4_5)
num_5 = t.count(5)
print("5 occurences:",num_5)
num_5_5 = t.count(5.5)
print("5.5 occurences:",num_5_5)
num_6 = t.count(6)
print("6 occurences:",num_6)

df = pd.DataFrame({'freq': t})
df.groupby('freq', as_index=False).size().plot(kind='bar')
plt.show()



# second option
# this is much faster for significant values and slightly faster for non-sig values
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

p = .03
a = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6] #possible jitter times

prb = np.asarray([p*(1.0-p)**k for k in range(0, len(a))])
prb /= np.sum(prb)

result = np.random.choice(a, size=228, replace = True, p=prb)

print(result)

df = pd.DataFrame({'freq': result})
df.groupby('freq', as_index=False).size().plot(kind='bar')
plt.show()
