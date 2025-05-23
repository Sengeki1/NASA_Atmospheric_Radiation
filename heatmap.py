import matplotlib.pyplot as plt

class HeatMap:
    def __init__(self, longitude, latitude, radiance):
        self.latitude = latitude
        self.longitude = longitude
        self.radiance = radiance

        self.latitude = self.latitude[0, :, :]
        self.longitude = self.longitude[0, :, :]
        self.radiance = self.radiance[0, :, :, 248]

    def plot(self):
        plt.figure()
        plt.pcolormesh(self.longitude, self.latitude, self.radiance, shading='auto')
        plt.colorbar(label='Radiation')
        plt.title("Heat Map in Regions (Cape Verde) 2025-05-23")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.savefig("./exports/heatmap.png")
        plt.show()