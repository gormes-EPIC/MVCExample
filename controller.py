import pygame
from model import CounterModel
from view import CounterView

class CounterController:
    """Manages user input and updates the model and view accordingly."""
    
    def __init__(self):
        """Initialize the model, view, and game loop state."""
        self.model = CounterModel()
        self.view = CounterView()
        self.running = True  # Control variable for the game loop

    def run(self):
        """Main game loop to process events and update the UI."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # User closes the window
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click event
                    if self.view.is_button_clicked(event.pos):  # Check if button was clicked
                        self.model.increment()  # Update counter

            # Update the view with the latest count value
            self.view.render(self.model.get_count())

        pygame.quit()  # Cleanly exit Pygame
