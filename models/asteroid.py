import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from models.circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_asteroids_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        vector_one = self.velocity.rotate(new_asteroids_angle)
        vector_two = self.velocity.rotate(-new_asteroids_angle)

        asteroid_one = Asteroid(self.position.x + vector_one.x, self.position.y + vector_one.y, new_radius)
        asteroid_two = Asteroid(self.position.x + vector_two.x, self.position.y + vector_two.y, new_radius)

        asteroid_one.velocity = vector_one * 1.2
        asteroid_two.velocity = vector_two * 1.2
