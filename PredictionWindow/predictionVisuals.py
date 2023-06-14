import pygame.draw
import pygame.font

from config import *


class PredictionVisuals:
    def __init__(self, screen):
        self.screen = screen
        self.x = WINDOW_PADDING_HORIZONTAL + CANVAS_WIDTH + BORDER_WIDTH * 2
        self.y = WINDOW_PADDING_VERTICAL

    def draw_window(self, prediction="", probability=""):
        pygame.draw.rect(self.screen, 'black', (self.x, self.y, PREDICTION_WINDOW_WIDTH, PREDICTION_WINDOW_HEIGHT))
        self._draw_text(prediction, probability)
        self.draw_border()


    def draw_border(self):
        pygame.draw.rect(self.screen, 'blue', (self.x, self.y, PREDICTION_WINDOW_WIDTH, PREDICTION_WINDOW_HEIGHT),
                         BORDER_WIDTH)

    def _draw_text(self, prediction, probability):
        pred_font = pygame.font.Font(None, 200)
        prob_font = pygame.font.Font(None, 50)

        pred_text = pred_font.render(prediction, True, (255, 255, 255))  # Textfarbe anpassen
        prop_text = prob_font.render(probability, True, (255, 255, 255))

        pred_size = pred_font.size(prediction)
        prob_size = prob_font.size(probability)

        y_offset_pred = PREDICTION_WINDOW_HEIGHT // 2 - pred_size[1] // 2 - prob_size[1] // 2
        x_offset_pred = PREDICTION_WINDOW_WIDTH // 2 - pred_size[0] // 2

        y_offset_prob = y_offset_pred + pred_size[1] + prob_size[1]
        x_offset_prob = PREDICTION_WINDOW_WIDTH // 2 - prob_size[0] // 2
        self.screen.blit(pred_text, (self.x+x_offset_pred, self.y+y_offset_pred))
        self.screen.blit(prop_text, (self.x+x_offset_prob, self.y+y_offset_prob))

        x1 = self.x + min(x_offset_prob, x_offset_pred)
        x2 = self.x + PREDICTION_WINDOW_WIDTH - min(x_offset_prob, x_offset_pred)
        y = self.y + y_offset_prob - (y_offset_prob - y_offset_pred) // 4

        pygame.draw.line(self.screen, 'white', (x1, y), (x2, y))
