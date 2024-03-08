import pygame
import sys
import numpy as np
import math
from particle import Particle



NUM_PARTICLES = 500
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900 

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    trails = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT, 3), dtype=np.float32)
    particles = []

    for i in range(NUM_PARTICLES):
        speed = np.random.randint(1, 3)
        particles.append(Particle(SCREEN_WIDTH, SCREEN_HEIGHT, speed))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))
        dynamic_radius = min(20,2 * speed)

        for particle in particles:
            particle.update(SCREEN_WIDTH, SCREEN_HEIGHT)
            
            for trail_pos in particle.trail:
                pygame.draw.circle(screen, trail_pos[1], (int(trail_pos[0][0]), int(trail_pos[0][1])), int(dynamic_radius))
            
            pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), int(dynamic_radius))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()