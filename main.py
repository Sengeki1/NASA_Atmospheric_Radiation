import h5py
from heatmap import HeatMap
from timeline import TimeLine
from radial import Radial
import matplotlib.pyplot as plt
import numpy as np

def process(file):
    band5 = file['BAND5_RADIANCE']
    standard = band5['STANDARD_MODE']
    geodata = standard['GEODATA']
    observations = standard['OBSERVATIONS']

    radiance = observations['radiance'][:]
    longitude = geodata['longitude'][:]
    latitude = geodata['latitude'][:]

    return {"radiance": radiance, "latitude": latitude, "longitude": longitude}

def main():
    file = h5py.File('dataset/dataset.nc', 'r')

    data = process(file)

    heatmap = HeatMap(data["longitude"], data["latitude"], data["radiance"])
    heatmap.plot()

    timeline = TimeLine(data["longitude"], data["latitude"], data["radiance"])
    timeline.plot()

    radial = Radial(data["longitude"], data["latitude"], data["radiance"])
    radial.plot()

if __name__ == "__main__":
    main()
