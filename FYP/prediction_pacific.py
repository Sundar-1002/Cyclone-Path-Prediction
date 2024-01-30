import pandas as pd
data = pd.read_csv("myvalues.csv")
import pacific

latit = data['Latitude']
longi = data['Longitude']


def predcyc():
        lat,lon,title = pacific.ret()
        coords = list(zip(lat,lon))
        return coords,title