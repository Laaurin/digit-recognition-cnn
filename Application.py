import pygame

from keras.models import load_model
from keras.datasets import mnist
from Canvas.canvas import Canvas
from PredictionWindow.PredictionWindow import PredictionWindow
from config import *
import numpy as np


class Application:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.canvas = Canvas(self.screen)
        self.predictionWindow = PredictionWindow(self.screen)
        self.model = load_model('my_model.h5')
        self.running = True
        self.drawing = False
        self.last_pos = None

    def run(self):
        self.predictionWindow.visuals.draw_window()

        while (self.running):
            self.handle_events()
            self.canvas.visuals.draw_canvas(self.canvas.canvas)
            pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.canvas.create_canvas()
                    self.predictionWindow.visuals.draw_window()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Linke Maustaste gedrückt
                pos = pygame.mouse.get_pos()
                self.drawing = True
                x, y = self.get_cord(pos)
                self.brush(x, y)
                self.last_pos = (x, y)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Linke Maustaste losgelassen
                self.drawing = False
                prediction, prop = self.recognize_digit()
                self.predictionWindow.visuals.draw_window(prediction, prop)

            if event.type == pygame.MOUSEMOTION:  # Mausbewegung
                if not self.drawing:
                    return
                pos = pygame.mouse.get_pos()

                x, y = self.get_cord(pos)
                if (x, y) != self.last_pos:
                    self.brush(x, y)
                    self.last_pos = (x, y)

    def set_transparent_pixel(self, x, y):
        if 0 <= x < CANVAS_RESOLUTION and 0 <= y < CANVAS_RESOLUTION:

            self.canvas.canvas[y][x] += 25

            if not 0 <= self.canvas.canvas[y][x] <= 255:
                self.canvas.canvas[y][x] = 255

    def brush(self, x, y):
        if not (0 <= x < CANVAS_RESOLUTION and 0 <= y < CANVAS_RESOLUTION):
            return
        self.canvas.canvas[y][x] = 255
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.set_transparent_pixel(x+i, y+j)

    def get_cord(self, pos):
        y = ((pos[1] - WINDOW_PADDING_VERTICAL + BORDER_WIDTH) * CANVAS_RESOLUTION) // CANVAS_HEIGHT
        x = ((pos[0] - WINDOW_PADDING_HORIZONTAL + BORDER_WIDTH) * CANVAS_RESOLUTION) // CANVAS_WIDTH
        return x, y

    def recognize_digit(self):
        # Vorbereitung des Canvas-Bildes für die Vorhersage

        normalized_image = self.canvas.canvas / 255.0
        input_image = np.expand_dims(normalized_image, axis=0)
        input_image = np.expand_dims(input_image, axis=3)

        # Vorhersage mit dem Modell machen
        predictions = self.model.predict(input_image)
        predicted_class_index = np.argmax(predictions[0])
        predicted_class_probability = predictions[0][predicted_class_index]

        predicted_class = str(predicted_class_index)
        predicted_probability = str(predicted_class_probability)

        return predicted_class, predicted_probability[:5]

