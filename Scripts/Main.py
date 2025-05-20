import pygame
from random import random
from MaratEngine import *


class Game(Loop):
    def __init__(self) -> None:
        super().__init__()
        self.BG_COLOR = DICT_PALLETE["very_dark_brown"]

        self.cubic : Square = Square(500, 300, 20)
        self.cubic.color = DICT_PALLETE["dark_red"]
        self.cubic.border_radius = 4
        self.cubic.z_index = 2
        self.add_child(self.cubic)

        node : Character = Character(500, 300, 20)
        self.add_child(node)
        node.color = DICT_PALLETE["blue"]
        
    def _process(self) -> None:
        super()._process()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.cubic.x = mouse_x - self.cubic.size / 2
        self.cubic.y = mouse_y - self.cubic.size / 2

        mouse_pressed : tuple = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            pass

    def _input(self, event) -> None:
        # события мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # if event.button == 3: 

class Character(Circle):
    def __init__(self, x=0, y=0, size=1):
        super().__init__(x, y, size)
        self.speed : float = 5
        self.lerp_factor = 0.1  
        self.velocity : list = [x, y]

    def update(self) -> None:
        super().update()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity[1] -= self.speed
        if keys[pygame.K_s]:
            self.velocity[1] += self.speed
        if keys[pygame.K_a]:
            self.velocity[0] -= self.speed
        if keys[pygame.K_d]:
            self.velocity[0] += self.speed

        self.x = lerp(self.x, self.velocity[0], self.lerp_factor)
        self.y = lerp(self.y, self.velocity[1], self.lerp_factor)

        if self.x < 0 or self.x > game.WIDTH:
            self.x = max(0, min(game.WIDTH - self.size, self.x))

        if self.y < 0 or self.y > game.HEIGHT:
            self.y = max(0, min(game.HEIGHT - self.size, self.y))

    

if __name__ == "__main__":
    game : Game = Game()
    game.update()
