import pygame
from constants import *
from circleshape import *
from player import *   
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)

    field = AsteroidField()
    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        updateable.update(dt)

        for rock in asteroids:
            if rock.collide(player):
                print("Game over!")
                pygame.quit()
                return
        
        for rock in asteroids:
            for shot in shots:
                if rock.collide(shot):
                    shot.kill()
                    rock.split()
                    break

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(240) / 1000.0 
        
    
if __name__ == "__main__":
    main()
