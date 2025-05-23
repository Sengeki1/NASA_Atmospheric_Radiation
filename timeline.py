import matplotlib.pyplot as plt

class TimeLine:
    def __init__(self, longitude, latitude, radiance):
        self.latitude = latitude
        self.longitude = longitude
        self.radiance = radiance

        self.mean_radiance_per_band = self.radiance.mean(axis=(1, 2))[0]

    def plot(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.mean_radiance_per_band)
        plt.title("Average Spacial Radiance Per Band (Cape Verde) 2025-05-23")
        plt.xlabel("Spacial Band Index")
        plt.ylabel("Average Radiance")
        plt.grid(True)
        plt.savefig("./exports/average spacial radiance per band.png")
        plt.show()