class CounterModel:
    """Handles the data and logic for the counter."""
    
    def __init__(self):
        """Initialize the counter with a default value of 0."""
        self.count = 0

    def increment(self):
        """Increase the counter value by 1."""
        self.count += 1

    def get_count(self):
        """Return the current counter value."""
        return self.count
