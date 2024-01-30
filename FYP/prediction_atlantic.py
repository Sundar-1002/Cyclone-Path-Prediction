import pandas as pd
data = pd.read_csv("myvalues.csv")
import copy_of_atlantic2

latit = data['Latitude']
longi = data['Longitude']


def predcyc():
        lat,lon,title = copy_of_atlantic2.ret()
        coords = list(zip(lat,lon))
        return coords,title