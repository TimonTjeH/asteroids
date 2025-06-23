from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

import pygame

from shot import Shot


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    Shot.containers = (shot_group, updatable_group, drawable_group)
    player = Player(x, y)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable_group.update(dt)

        for asteroid in asteroid_group:
            if player.hasCollided(asteroid):
                print("Game over!")
                exit()
            for shot in shot_group:
                if asteroid.hasCollided(shot):
                    asteroid.split()
                    shot.kill()


        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

