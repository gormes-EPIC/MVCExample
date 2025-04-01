import pygame
from model import CounterModel
from view import CounterView

class CounterController:
    def __init__(self):
        self.model = CounterModel()
        self.view = CounterView()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.view.is_button_clicked(event.pos):
                        self.model.increment()

            self.view.render(self.model.get_count())

        pygame.quit()
