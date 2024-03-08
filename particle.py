import math
import numpy as np


class Particle():
    def __init__(self, screen_width, screen_height, speed):
        self.color = [255,255,255]
        self.speed = speed
        self.x = np.random.randint(0, screen_width)
        self.y = np.random.randint(0, screen_height)
        self.trail = []
        self.trail_length = 15
        self.trail_color = self.color
        self.fade_amount = 20
        self.angle = np.random.rand() * 360

    def update(self, screen_width, screen_height):
        radian_angle = math.radians(self.angle)  # Konvertiere Winkel zu Radiant
        self.x += self.speed * math.cos(radian_angle)
        self.y += self.speed * math.sin(radian_angle)

        # Update der Trail-Punkte und ihrer Farben
        self.trail.append(((self.x, self.y), self.color))
        self.trail = [(pos, fade_color(color, self.fade_amount)) for pos, color in self.trail]

        if len(self.trail) > self.trail_length:
            self.trail.pop(0)

        # Wandkollision und Farbänderung
        if self.x < 0 or self.x >= screen_width - 1: 
            self.angle = 180 - self.angle
            self.color = [np.random.randint(0, 255) for _ in range(3)]
        if self.y < 0 or self.y >= screen_height - 1: 
            self.angle = -self.angle
            self.color = [np.random.randint(0, 255) for _ in range(3)]
        
        self.x = min(max(self.x, 0), screen_width - 1)
        self.y = min(max(self.y, 0), screen_height - 1)

def fade_color(color, fade_amount):
    return tuple(max(0, component - fade_amount) for component in color)
