from urllib.request import urlopen
import numpy as np
f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')
f_ar = np.loadtxt(f, skiprows=1, delimiter=',')
print(f_ar)
