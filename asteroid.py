from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
  # Asteroid class that inherits from CircleShape
   

    def __init__(self, x, y, radius):   
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)
        
    def update(self, dt):
        # Update the position of the asteroid
        self.position += self.velocity * dt
        # Wrap around the screen edges
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius