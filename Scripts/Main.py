import pygame
import math
import random
import json
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *
from os import system

system("cls")

class Game(Loop):
    def __init__(self) -> None:
        super().__init__()
        self.BG_COLOR = GREEN

        self.cubic : Square = Square(self.screen, 500, 300)
        self.cubic.color = RED
        self.cubic.size = 20
        self.cubic.border_radius = 4

        self.add_child(self.cubic)

        self.TOWNS        : list[str] = ["Moscow", "Perm", "Ekaterinburg"]
        self.player_towns : list[Town | None] = [None] * self.TOWNS.__len__()
        self.current_town : int = 0

    def _process(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.cubic.x = mouse_x - self.cubic.size / 2
        self.cubic.y = mouse_y - self.cubic.size / 2

    def _input(self, event) -> None:
        if event.type == pygame.QUIT: 
            self.running = False
        
        # события клавиатуры
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.current_town = 0

            if event.key == pygame.K_2:
                self.current_town = 1
                
            if event.key == pygame.K_3:
                self.current_town = 2

        # события мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if event.button == 1: 
                self.add_town(mouse_x, mouse_y)
        
    def add_town(self, x, y) -> None:
        SCALE : int = 2
        pos : list = [x - 8 * SCALE, y - 8 * SCALE]

        if not self.player_towns[self.current_town]:
            self.player_towns[self.current_town] = Town(self.screen, self.TOWNS[self.current_town], x=pos[0], y=pos[1], size=SCALE)
            self.add_child(self.player_towns[self.current_town])

        else:
            self.player_towns[self.current_town].change_position(pos)


    def distances(self) -> None:
        for town1 in self.player_towns:
            for town2 in self.player_towns:
                if (town1 == town2) or (town1 is None) or (town2 is None):
                    continue
                
                vector   : list = [town2.x - town1.x, town2.y - town1.y]
                distance : float = math.sqrt(vector[0] ** 2 + vector[1] ** 2)

                normalized_vector : list = [0] * 2
                
                if distance:
                    normalized_vector = [vector[0] / distance, vector[1] / distance]

                angle_rad : float = math.atan2(normalized_vector[0], normalized_vector[1])
                angle_deg : float = math.degrees(angle_rad)

                print(town1.name, town2.name, angle_deg, distance)
                
        print()

class Town(Sprite):
    def __init__(self, screen, name_town : str, image_path = "Assets/town.png", x = 0, y = 0, size = 1):
        super().__init__(screen, image_path, x, y, size)
        self.name = name_town

        self.label_town : Label = Label(self.screen, name_town, x, y + 32, 20)
        self.label_town.color = BLACK
        game.add_child(self.label_town)
    
    def change_position(self, pos : list) -> None:
        self.x = pos[0]
        self.y = pos[1]

        self.label_town.x = pos[0]
        self.label_town.y = pos[1] + 32

if __name__ == "__main__":
    game : Game = Game()
    game.update()


#  with open("../JsonFiles/ru.json", encoding="utf-8") as file:
#     data = json.load(file)
#     print(json.dumps(data, indent=4, sort_keys=True)) 
#     for i in range(10):    
#         if "name" in data["actionHistory"][i]:
#             print(data["actionHistory"][i]["name"])  