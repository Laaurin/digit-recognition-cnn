import pygame
from config import *


class CanvasVisuals:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen

    def draw_border(self):
        pygame.draw.rect(self.screen, 'blue',
                         (WINDOW_PADDING_HORIZONTAL, WINDOW_PADDING_VERTICAL, CANVAS_WIDTH, CANVAS_HEIGHT),
                         BORDER_WIDTH)

    def draw_canvas(self, canvas):
        size = CANVAS_WIDTH // CANVAS_RESOLUTION
        for i in range(len(canvas)):
            for j in range(len(canvas[i])):
                color = (canvas[i][j], canvas[i][j], canvas[i][j])
                pygame.draw.rect(self.screen, color, (WINDOW_PADDING_HORIZONTAL + j * size,
                                                      WINDOW_PADDING_VERTICAL + i * size,
                                                      size, size))

        self.draw_border()
