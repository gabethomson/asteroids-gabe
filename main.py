import pygame
from constants import *
from circleshape import *
from player import *   
from asteroid import *
from asteroidfield import *
from shot import *

def asteroid_points(radius: float) -> int:
    # Tune thresholds as you like
    if radius > ASTEROID_MIN_RADIUS * 2:
        return POINTS_LARGE
    elif radius > ASTEROID_MIN_RADIUS:
        return POINTS_MEDIUM
    else:
        return POINTS_SMALL

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

    score = 0
    pygame.font.init()
    hud_font = pygame.font.SysFont(None, HUD_FONT_SIZE)  # None = default font
    
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
                print(f"Final score: {score}")
                pygame.quit()
                return
        
        for rock in asteroids:
            for shot in shots:
                if rock.collide(shot):
                    score += asteroid_points(rock.radius)
                    shot.kill()
                    rock.split()
                    break

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)

        score_surf = hud_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))
        
        pygame.display.flip()
        dt = clock.tick(240) / 1000.0 
        
    
if __name__ == "__main__":
    main()
