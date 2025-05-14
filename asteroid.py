from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
  # Asteroid class that inherits from CircleShape
   

    def __init__(self, x, y, radius):   
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        
        # Split the asteroid into two smaller asteroids
        # Generate a random split angle between 20 and 50 degrees.
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current velocity.
        new_velocity_1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2

        # Calculate the new radius for the smaller asteroids.
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new Asteroid objects at the current position with the new radius and velocities.
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity_1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity_2
        
    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)
        
    def update(self, dt):
        # Update the position of the asteroid
        self.position += self.velocity * dt