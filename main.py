# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys
from shot import Shot


def main():
    pygame.init()
    print ("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Create a player object
    # and add it to the updatable and drawable groups
    # This allows us to use the player object
    # in the updatable and drawable groups
    # and update and draw it
    # in the main loop
    Player.containers = (updatable, drawable)

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)
    
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    pygame.time.Clock
    dt = 0
    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for each in asteroids:
            if player.collide(each):
                print("Game over!")
                return
            for shot in shots:
                if each.collide(shot):
                    each.split()
                    shot.kill()## remove the shot
                
        for each in drawable:
            each.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60)/1000.0

    


if __name__ == "__main__":
    main()
