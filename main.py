import pygame
from constants import *
from models.player import Player
from models.asteroid import Asteroid
from models.asteroidfield import AsteroidField
from models.shot import Shot

def main() :
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    fps = 60

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # The magic happens in the Sprite class that our Player inherits from.
    # When you set the containers class variable and then create a new instance,
    # Pygame's Sprite.__init__() automatically adds the new instance to all the groups listed in containers.
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0,0,0))

        for updatable in updatables:
            updatable.update(dt)

        for drawable in drawables:
            drawable.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return

            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(fps) / 1000.0

if __name__ == "__main__":
    main()
