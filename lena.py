'''
Created on 30/04/2015

@author: Fernando
'''
from scipy import misc
lena = misc.lena()

import pylab as plt
import numpy as np

lena = misc.lena()
plt.imshow(lena)

plt.imshow(lena, cmap=plt.gray())

crop_lena = lena[30:-30,30:-30]

y, x = np.ogrid[0:512,0:512] # x and y indices of pixels
y.shape, x.shape
#Out[16]: ((512, 1), (1, 512))
centerx, centery = (256, 256) # center of the image
mask = ((y - centery)**2 + (x - centerx)**2) > 230**2 # circle

lena[mask] = 0
plt.imshow(lena)
#Out[20]: <matplotlib.image.AxesImage object at 0xa36534c>