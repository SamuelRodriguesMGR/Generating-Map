import pygame
from .utils.Node import Node2D


BLACK  : tuple = (0, 0, 0)
WHITE  : tuple = (255, 255, 255)
RED    : tuple = (255, 0, 0)
BLUE   : tuple = (0, 0, 255)
YELLOW : tuple = (255, 255, 0)
GREEN  : tuple = (0, 255, 0)

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
        
        self.group_sprites : pygame.sprite.LayeredUpdates = pygame.sprite.LayeredUpdates()  
        

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
        self.group_sprites.draw(self.screen)  
    
    def _process(self) -> None:
        self.group_sprites.update() 
    
    def add_child(self, node : Node2D) -> None:
        self.group_sprites.add(node, layer=node.z_index)  
   
    def remove_child(self, node : Node2D) -> None:
        self.group_sprites.remove(node)