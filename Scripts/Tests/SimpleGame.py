from pathlib import Path
from sys import path
path.append(str(Path(__file__).parent.parent))

import pygame
from random import random
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *


class Game(Loop):
    def __init__(self) -> None:
        super().__init__()
        self.BG_COLOR = DICT_PALLETE["very_dark_brown"]

        self.cubic : Square = Square(500, 300, 20)
        self.cubic.color = DICT_PALLETE["dark_red"]
        self.cubic.border_radius = 4
        self.cubic.z_index = 2

        self.add_child(self.cubic)

    def _process(self) -> None:
        super()._process()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.cubic.x = mouse_x - self.cubic.size / 2
        self.cubic.y = mouse_y - self.cubic.size / 2

        mouse_pressed : tuple = pygame.mouse.get_pressed()
        node : GravityAgent

        if mouse_pressed[0]:
            node = GravityAgent(self.cubic, -1, mouse_x - self.cubic.size, mouse_y - self.cubic.size, 20)
            self.add_child(node)
            node.color = DICT_PALLETE["blue"]

        if mouse_pressed[2]:
            node = GravityAgent(self.cubic, 1, mouse_x - self.cubic.size, mouse_y - self.cubic.size, 20)
            node.color = DICT_PALLETE["red"]
            self.add_child(node)



    def _input(self, event) -> None:
        # события мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # if event.button == 3: 

class GravityAgent(Circle):
    def __init__(self, target : Node2D, dir : int, x=0, y=0, size=1):
        super().__init__(x, y, size)
        self.target = target
        self.speed : float = random() * 10 * dir

    def update(self) -> None:
        super().update()
        vector : list = [self.target.x - self.x, self.target.y - self.y]
        distance : float = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
        normalized_vector : list = [0.0] * 2

        if distance:
            normalized_vector = [vector[0] / distance, vector[1] / distance]

        self.x += normalized_vector[0] * self.speed
        self.y += normalized_vector[1] * self.speed

        if self.x < 0 or self.x > game.WIDTH:
            self.x = max(0, min(game.WIDTH - self.size, self.x))

        if self.y < 0 or self.y > game.HEIGHT:
            self.y = max(0, min(game.HEIGHT - self.size, self.y))



if __name__ == "__main__":
    game : Game = Game()
    game.update()
