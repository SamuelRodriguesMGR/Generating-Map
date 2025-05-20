import pygame
from .utils.Node import Node2D

# endesega16
DICT_PALLETE : dict = {
    "very_light_brown" : "#e4a672",
    "light_brown"      : "#b86f50",
    "dark_brown"       : "#743f39",
    "very_dark_brown"  : "#3f2832",
    "dark_red"         : "#9e2835",
    "red"              : "#e53b44",
    "orange"           : "#fb922b",
    "yellow"           : "#ffe762",
    "light_green"      : "#63c64d",
    "green"            : "#327345",
    "dark_green"       : "#193d3f",
    "gray"             : "#4f6781",
    "light_gray"       : "#afbfd2",
    "white"            : "#ffffff",
    "cyan"             : "#2ce8f4",
    "blue"             : "#0484d1"
}

class Loop:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("My Game")

        self.FPS      : int = 60
        self.HEIGHT   : int = 648
        self.WIDTH    : int = 1152
        self.running  : bool = True

        self.BG_COLOR = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.stack : pygame.sprite.LayeredUpdates = pygame.sprite.LayeredUpdates()  
        

    def update(self):
        while self.running:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT: 
                    self.running = False  
                self._input(event)

            self.clock.tick(self.FPS)

            # Рендеринг
            self.screen.fill(self.BG_COLOR)

            self._process()
            self._draw()

            # после отрисовки всего, переворачиваем экран
            pygame.display.flip()
    pygame.quit()

    def _input(self, event) -> None:
        pass

    def _draw(self) -> None:
        self.stack.draw(self.screen)  
    
    def _process(self) -> None:
        self.stack.update() 
    
    def add_child(self, node : Node2D) -> None:
        self.stack.add(node, layer=node.z_index)  
   
    def remove_child(self, node : Node2D) -> None:
        self.stack.remove(node)

def lerp(fr : float, to : float, weight : float):
    return fr + (to - fr) * weight