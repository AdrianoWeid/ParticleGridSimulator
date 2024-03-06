import pygame
import sys
import numpy as np
from particle import Particle, fade_trails, update_trail


NUM_PARTICLES = 1000
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900 

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    rotation_input = 0
    particles = [Particle(SCREEN_WIDTH, SCREEN_HEIGHT) for _ in range(NUM_PARTICLES)]
    trails = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT, 3), dtype=np.float32)
    print(trails)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()

        fade_trails(trails)
        update_trail(trails, particles)
        for particle in particles:
            particle.update(SCREEN_WIDTH, SCREEN_HEIGHT, rotation_input)
            pygame.draw.circle(screen, (255,255,255), (int(particle.x), int(particle.y)),200.0)

        pygame.surfarray.blit_array(screen, trails.astype("uint8"))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()