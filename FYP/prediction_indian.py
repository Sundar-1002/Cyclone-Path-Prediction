import pandas as pd
data = pd.read_csv("myvalues.csv")
import indian

latit = data['Latitude']
longi = data['Longitude']


def predcyc():
        lat,lon,title = indian.ret()
        coords = list(zip(lat,lon))
        return coords,title