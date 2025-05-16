import pygame
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *

class Game(Loop):
    def __init__(self) -> None:
        super().__init__()
        self.BG_COLOR = GREEN

        self.cubic : Square = Square(500, 300, 20)
        self.cubic.color = RED
        self.cubic.border_radius = 4
        self.cubic.z_index = 1

        self.add_child(self.cubic)

    def _process(self) -> None:
        super()._process()
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
                self.add_child(Circle(mouse_x - self.cubic.size / 2, mouse_y - self.cubic.size / 2, 20))

if __name__ == "__main__":
    game : Game = Game()
    game.update()


#  with open("../JsonFiles/ru.json", encoding="utf-8") as file:
#     data = json.load(file)
#     print(json.dumps(data, indent=4, sort_keys=True)) 
#     for i in range(10):    
#         if "name" in data["actionHistory"][i]:
#             print(data["actionHistory"][i]["name"])  