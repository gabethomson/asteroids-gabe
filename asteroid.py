import random
import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
    
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20,50)

        v1 = self.velocity.rotate(split_angle) * 1.2
        v2 = self.velocity.rotate(-split_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a = Asteroid(self.position.x, self.position.y, new_radius)
        b = Asteroid(self.position.x, self.position.y, new_radius)
        a.velocity = v1
        b.velocity = v2