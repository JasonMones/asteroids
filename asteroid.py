from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20,50)
        split_asteroid_velocity1 = self.velocity.rotate(split_angle)
        split_asteroid_velocity2 = self.velocity.rotate(-split_angle)
        split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        first_split_asteroid = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
        first_split_asteroid.velocity = split_asteroid_velocity1 * 1.2
        
        second_split_asteroid = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
        second_split_asteroid.velocity = split_asteroid_velocity2 * 1.2
