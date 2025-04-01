import pygame

class CounterView:
    def __init__(self, width=400, height=300):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("MVC Counter")
        self.font = pygame.font.Font(None, 50)
        self.button_rect = pygame.Rect(150, 150, 100, 50)

    def render(self, count):
        self.screen.fill((30, 30, 30))
        text = self.font.render(f"Count: {count}", True, (255, 255, 255))
        self.screen.blit(text, (150, 50))

        pygame.draw.rect(self.screen, (0, 255, 0), self.button_rect)
        button_text = self.font.render("+", True, (0, 0, 0))
        self.screen.blit(button_text, (175, 160))

        pygame.display.flip()

    def is_button_clicked(self, pos):
        return self.button_rect.collidepoint(pos)
