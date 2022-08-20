from PIL import Image
import numpy as np
from filestack import Client


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3D numpy arrays of 0s.
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        # Change Os to the value provided in the color
        self.data[:] = self.color

    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)


class FileSharer:

    def __init__(self, filepath, apikey="ABbXmMQ2DRLGwfCWVAvuZz"):
        self.filepath = filepath
        self.apikey = apikey

    def share(self):
        client = Client(self.apikey)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

