import pandas as pd
import numpy as np

df=pd.read_csv(r'C:\Users\Ignacio\Documents\PYTHON DOCUMENTS\GitHub Projects\concap.csv')
#print(df)

## (The 'r' before the string converts it to a 'raw string'. 
## Python raw string treats backslash (\) as a literal character.
## This is useful when we want to have a string that contains backslash and 
## don’t want it to be treated as an escape character.)

# I'll just save the Earth's radius as the contant 'r':
r = 6371

coord_input = input("\nInport latitude and longitude separated by a comma: ")


# We create the variable for the latitude and longitude of the input values (point B):
# N.B. The input string has been typecast to a float and then to a list:
coord = list(np.float_(coord_input.split(',')))
print('The given coordinates are: ', coord)
lat_2 = coord[0]
long_2 = coord[1]

## Latitude must be in the range [-90º, +90º]
## Longitude must be in the range [-180º, +180º]

if lat_2<-90 or lat_2>+90 or long_2<-180 or long_2>+180:
    print('\nInput error: Latitude must be in the range [-90º, +90º] and longitude in the range [-180º, +180º].\n')
else:


    ## We create lists for the latitudes and longitudes in the df:
    latitudes = df['CapitalLatitude'].to_numpy()
    longitudes = df['CapitalLongitude'].to_numpy()

    #print(type(longitudes))
    #print('Latitudes: ',latitudes)
    #print('Longitudes: ',longitudes)


    ## We define the Δλ (in degrees):
    Lambda = long_2-longitudes
    #print('Δλ= ',Lambda)
    #print(type(Lambda))

    ## We can proceed to calculate the cental angle Δσ:
    Sigma = np.arccos(np.sin(latitudes*np.pi/180)*np.sin(lat_2*np.pi/180)+np.cos(latitudes*np.pi/180)*np.cos(lat_2*np.pi/180)*np.cos(Lambda*np.pi/180))
    #print('The central angle is: Δσ =',Sigma)

    ## The distance is thus given by:
    d_np = r*Sigma
    #print('The distance between the given point and all the world capitals is:\n',d_np, 'km')

    ## We will typecast the distances arrays to a DataFrame:
    d = pd.DataFrame(data=d_np,  columns=['Distances'])


    ## We will create a new DataFrame with the countries, the capitals and the found distances:
    data = [df["CountryName"], df["CapitalName"], d['Distances']]
    headers = ['Country', 'Capital', 'Distance']

    new_df = pd.concat(data, axis=1, keys=headers)
    #print(new_df)

    ## We now find the minimum value for the distance:
    min_dist_idx = new_df['Distance'].idxmin()
    #print('Dataframe index for the minimum distance: ', min_dist_idx)
    Result = df.iloc[min_dist_idx,:]
    print('The closest world capital is: \n\n', Result)
    print('\nThe distance is:', round(new_df.iloc[min_dist_idx,2],2), 'km')



## Madrid: 40.4,-3.683333
## Jakarta: -6.166666666666667,106.816667
## Hanoi: 21.033333333333335,105.850000
## Lima: -12.05,-77.050000
## Reykjavik,64.15,-21.950000
## Tokyo,35.68333333333333,139.750000