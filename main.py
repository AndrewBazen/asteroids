import pygame
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    
    player = Player(x, y)
    asteroid_field = AsteroidField()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        
        for a in asteroids:
            if player.check_collision(a):
                player.kill()
                print("Game Over!")
                return
            for s in shots:
                if s.check_collision(a):
                    a.split()
                    s.kill()
                    break
        
        screen.fill("black")
        
        for d in drawable:
            d.draw(screen)
        
        
       
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    

if __name__ == "__main__":
    main()