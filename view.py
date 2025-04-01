import pygame

class CounterView:
    """Handles the graphical representation of the application."""
    
    def __init__(self, width=400, height=300):
        """Initialize the Pygame window and UI elements."""
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("MVC Counter")  # Set window title
        self.font = pygame.font.Font(None, 50)  # Default font with size 50
        
        # Define button properties
        self.button_rect = pygame.Rect(150, 150, 100, 50)

    def render(self, count):
        """Render the counter value and button on the screen."""
        self.screen.fill((30, 30, 30))  # Background color (dark gray)
        
        # Render the counter text
        text = self.font.render(f"Count: {count}", True, (255, 255, 255))
        self.screen.blit(text, (150, 50))

        # Draw the button (green rectangle)
        pygame.draw.rect(self.screen, (0, 255, 0), self.button_rect)
        
        # Draw the "+" symbol on the button
        button_text = self.font.render("+", True, (0, 0, 0))
        self.screen.blit(button_text, (175, 160))

        pygame.display.flip()  # Update the display

    def is_button_clicked(self, pos):
        """Check if the mouse click position is inside the button."""
        return self.button_rect.collidepoint(pos)
