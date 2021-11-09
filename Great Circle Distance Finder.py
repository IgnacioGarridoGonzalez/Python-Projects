import pandas as pd
import numpy as np

# I'll just save the Earth's radius as the contant 'r':
r = 6371

coord_input2 = input("Input latitude and longitude separated by a comma of the first city: ")
coord_input1 = input("Input latitude and longitude separated by a comma of the second city: ")

# Latitude must be in the range [(S) -90º, +90º (N)]
# Longitude must be in the range [(W) -180º, +180º (E)] (or viceversa, really)

# Typecast coordinates of both points to floats:
coord_2 = list(np.float_(coord_input2.split(',')))
coord_1 = list(np.float_(coord_input1.split(',')))
print('The coordinates of point B: ', coord_2)
print('The coordinates of point A: ', coord_1)

# We define the latitudes and longitudes of each point
lat_2 = coord_2[0]
lat_1 = coord_1[0]

long_2 = coord_2[1]
long_1 = coord_1[1]

# We define the Δλ:
Lambda = long_2 - long_1

# We can proceed to calculate the cental angle Δσ:
Sigma = np.arccos(np.sin(lat_1*np.pi/180)*np.sin(lat_2*np.pi/180)+np.cos(lat_1*np.pi/180)*np.cos(lat_2*np.pi/180)*np.cos(Lambda*np.pi/180))
print('The central angle is: Δσ =',Sigma)

d = r*Sigma
print('The distance between both cities is: ', round(d), 'km')


## Madrid: 40.4,-3.683333
## Jakarta: -6.166666666666667,106.816667
## Hanoi: 21.033333333333335,105.850000
## Lima: -12.05,-77.050000
## Reykjavik,64.15,-21.950000
## Tokyo,35.68333333333333,139.750000


## Paris: +48.67 (N), -2.33 (E)
## Melbourne: -37.82 (S), -144.97 (E)

# https://en.wikipedia.org/wiki/Geographical_distance
# https://en.wikipedia.org/wiki/Great-circle_distance #### La buena!!!!
# https://amsi.org.au/ESA_Senior_Years/PDF/PDFvcaa/spherical8b.pdf  ### Example!!!
# Be careful with singularities!!