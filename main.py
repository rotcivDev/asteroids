import pygame

from constants import *
from player import Player


def main() :
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    # The magic happens in the Sprite class that our Player inherits from.
    # When you set the containers class variable and then create a new Player instance,
    # Pygame's Sprite.__init__() automatically adds the new instance to all the groups listed in containers.
    Player.containers = (updatables, drawables)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0,0,0))

        for updatable in updatables:
            updatable.update(dt)

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)

if __name__ == "__main__":
    main()
