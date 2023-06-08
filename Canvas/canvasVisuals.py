import pygame
from config import *


class CanvasVisuals:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen

    def draw_border(self):
        pygame.draw.rect(self.screen, 'blue',
                         (WINDOW_PADDING_HORIZONTAL, WINDOW_PADDING_VERTICAL, CANVAS_WIDTH, CANVAS_HEIGHT),
                         CANVAS_BORDER_WIDTH)

    def draw_canvas(self, canvas):
        size = CANVAS_WIDTH // 25
        for i in range(len(canvas)):
            for j in range(len(canvas[i])):
                color = (canvas[i][j], canvas[i][j], canvas[i][j])
                pygame.draw.rect(self.screen, color, (WINDOW_PADDING_HORIZONTAL + i * size,
                                                      WINDOW_PADDING_VERTICAL + j * size,
                                                      size, size))
        # surface = pygame.surfarray.make_surface(canvas)
        # scaled_surface = pygame.transform.scale(surface, (CANVAS_WIDTH, CANVAS_HEIGHT))

        # self.screen.blit(scaled_surface, (WINDOW_PADDING_HORIZONTAL, WINDOW_PADDING_VERTICAL))

        self.draw_border()
