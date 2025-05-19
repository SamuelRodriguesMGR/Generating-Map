import pygame
from .utils.Node import Node2D


BLACK  : tuple = (0, 0, 0)
WHITE  : tuple = (255, 255, 255)
RED    : tuple = (255, 0, 0)
BLUE   : tuple = (0, 0, 255)
YELLOW : tuple = (255, 255, 0)
GREEN  : tuple = (0, 255, 0)

# endesega16
PALLETE : list =[
    "#e4a672", "#b86f50", "#743f39", "#3f2832",
    "#9e2835", "#e53b44", "#fb922b", "#ffe762", 
    "#63c64d", "#327345", "#193d3f", "#4f6781", 
    "#afbfd2", "#ffffff", "#2ce8f4", "#0484d1"
]

class Loop:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("My Game")

        self.FPS      : int = 60
        self.HEIGHT   : int = 648
        self.WIDTH    : int = 1152
        self.running  : bool = True

        self.BG_COLOR = BLACK

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