import pygame

from Canvas.canvas import Canvas
from config import *


class Application:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.canvas = Canvas(self.screen)
        self.running = True
        self.drawing = False
        self.last_pos = None

    def run(self):
        c = 0
        for i in range(len(self.canvas.canvas)):
            line = ""
            break
            for j in range(len(self.canvas.canvas[i])):
                c += 255 // 25
                self.canvas.canvas[i][j] = 30
                line += f" {c % 255:3} "
            print(line)

        while (self.running):
            self.handle_events()
            self.canvas.visuals.draw_canvas(self.canvas.canvas)
            pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Linke Maustaste gedrückt
                self.drawing = True
                pos = pygame.mouse.get_pos()
                x, y = self.get_cord(pos)
                self.brush(x, y)
                self.last_pos = (x, y)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Linke Maustaste losgelassen
                self.drawing = False
                print("not drawing")

            if event.type == pygame.MOUSEMOTION:  # Mausbewegung
                if self.drawing:
                    pos = pygame.mouse.get_pos()
                    x, y = self.get_cord(pos)
                    if (x, y) != self.last_pos:
                        self.brush(x, y)
                        self.last_pos = (x, y)

    def set_transparent_pixel(self, x, y):
        if 0 <= x < self.canvas.resolution and 0 <= y < self.canvas.resolution:

            self.canvas.canvas[y][x] += 255 // 10

            if self.canvas.canvas[y][x] > 255:
                self.canvas.canvas[y][x] = 255

    def brush(self, x, y):
        self.canvas.canvas[y][x] = 255

        for i in range(-1, 2):
            for j in range(-1, 2):
                self.set_transparent_pixel(x+i, y+j)

    def get_cord(self, pos):
        x = ((pos[1] - WINDOW_PADDING_HORIZONTAL + CANVAS_BORDER_WIDTH) * self.canvas.resolution) // CANVAS_WIDTH
        y = ((pos[0] - WINDOW_PADDING_VERTICAL + CANVAS_BORDER_WIDTH) * self.canvas.resolution) // CANVAS_HEIGHT
        return x, y
