import pygame
import math
import numpy as np


class Particle():
    def __init__(self, screen_width, screen_height):
        self.x = np.random.randint(0, screen_width)
        self.y = np.random.randint(0, screen_height)
        self.angle = np.random.rand() * 360

    def update(self, screen_width, screen_height, rotation_input):
        self.x += math.cos(math.radians(self.angle))
        self.y += math.sin(math.radians(self.angle))

        if self.x < 0 or self.x >= screen_width: self.angle = 180 - self.angle
        if self.y < 0 or self.x >= screen_height: self.angle = -self.angle

        self.angle += rotation_input
        self.angle %= 360

        self.x = min(max(self.x,0), screen_width - 1)
        self.y = min(max(self.y,0), screen_height - 1)

def update_trail(trails, particles):
    for particle in particles:
        x, y = int(particle.x), int(particle.y)
        trails[x, y, :] = [255, 255, 255]

def fade_trails(trails, fade_rate=0.95):
    trails *= fade_rate
    np.clip(trails, 0, 255, out=trails)

    
