import matplotlib.pyplot as plt
import numpy as np

class Radial:
    def __init__(self, longitude, latitude, radiance):
        self.latitude = latitude
        self.longitude = longitude
        self.radiance = radiance

        self.mean_radiance_per_band = self.radiance.mean(axis=(1, 2))[0]
        self.num_band = len(self.mean_radiance_per_band)
        self.process()

    def process(self):
        self.angles = np.linspace(0, 2 * np.pi, self.num_band, endpoint=False).tolist()
        self.media_rad = np.append(self.mean_radiance_per_band, self.mean_radiance_per_band[0])
        self.angles.append(self.angles[0])
        
    def plot(self):
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

        ax.plot(self.angles, self.media_rad, color='orange', linewidth=1.5)
        ax.fill(self.angles, self.media_rad, color='orange', alpha=0.4)

        ax.set_title("Average Distribution of Radition per Spectral Band (Cape Verde) 2025-05-23", va='bottom')
        plt.savefig("./exports/average distribution.png")
        plt.show()