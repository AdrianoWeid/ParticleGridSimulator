import pygame
import sys
import numpy as np
import math
from particle import Particle, fade_trails, update_trail



NUM_PARTICLES = 5000
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900 

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    rotation_input = 0
    trails = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT, 3), dtype=np.float32)
    particles = []
    radius = 200
    for i in range(NUM_PARTICLES):
        angle = 2 * math.pi * i / NUM_PARTICLES  # Winkel für jeden Partikel
        particles.append(Particle(SCREEN_WIDTH, SCREEN_HEIGHT, radius, angle))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()

        fade_trails(trails)
        update_trail(trails, particles)
        for particle in particles:
            particle.update(SCREEN_WIDTH, SCREEN_HEIGHT, rotation_input)
            pygame.draw.circle(screen, (255,255,255), (int(particle.x), int(particle.y)),2)

        pygame.surfarray.blit_array(screen, trails.astype("uint8"))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()