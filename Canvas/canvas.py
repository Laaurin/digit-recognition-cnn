from Canvas.canvasVisuals import CanvasVisuals
import numpy as np
from config import *


class Canvas:
    def __init__(self, screen):
        self.visuals = CanvasVisuals(screen)
        self.canvas = None
        self.create_canvas()

    def create_canvas(self):
        self.canvas = np.zeros((CANVAS_RESOLUTION, CANVAS_RESOLUTION), dtype=np.uint16)
        return
        for i in range(len(self.canvas)):
            for j in range(len(self.canvas[i])):
                self.canvas[i][j] = 255



