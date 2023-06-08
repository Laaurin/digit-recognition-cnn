from Canvas.canvasVisuals import CanvasVisuals
import numpy as np


class Canvas:
    def __init__(self, screen):
        self.visuals = CanvasVisuals(screen)
        self.resolution = 25
        self.canvas = np.zeros((self.resolution, self.resolution), dtype=np.uint16)


