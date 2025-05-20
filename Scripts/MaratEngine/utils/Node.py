import pygame


class Node2D(pygame.sprite.Sprite):
    def __init__(self, x : float=0.0, y : float=0.0, size : float=1.0):
        super().__init__()
        self.x        : float = x
        self.y        : float = y
        self.color    : tuple | str = (0, 0, 0)
        self.size     : float = size
        self.visible  : bool = True
        self._z_index : int = 0
        
        # Для Sprite обязательно нужны image и rect
        self.image = None
        self.rect = None
        self._create_surface()
    
    def _create_surface(self):
        # Создает поверхность и rect для спрайта
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    
    def draw(self, screen):
        # Отрисовка на экране (если нужно сохранить старый интерфейс)
        if self.visible and self.image:
            screen.blit(self.image, self.rect)

    def update(self):
        self.rect.topleft = (self.x, self.y)

    @property
    def z_index(self):
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = value
        for group in self.groups():
            group.change_layer(self, value)

        
# Фигуры
class Shape(Node2D):
    def __init__(self, x=0, y=0, size=1):
        super().__init__(x, y, size)
        self.contour_thickness : int = 0 # заполнить фигуру
    
    def update(self):
        super().update()
        self._draw_shape()

    def _draw_shape(self):
        pass
    

class Square(Shape):
    def __init__(self, x=0, y=0, size=1):
        super().__init__(x, y, size)
        self.border_radius = 0
        
    def _draw_shape(self):
        self.image.fill((0, 0, 0, 0))  # Прозрачный фон
        pygame.draw.rect(
            self.image, 
            self.color, 
            (0, 0, self.size, self.size),
            self.contour_thickness,
            self.border_radius
        )

class Circle(Shape):
    def _draw_shape(self):
        self.image.fill((0, 0, 0, 0))  # Прозрачный фон
        pygame.draw.circle(
            self.image,
            self.color,
            (self.size // 2, self.size // 2),
            self.size // 2,
            self.contour_thickness
        )

# Текст
class Label(Node2D):    
    def __init__(self, text : str, x=0, y=0, size=1):
        super().__init__(x, y, size)
        self.font = pygame.font.Font(None, size) 
        self.text : str = text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


# Картинки
class Sprite(Node2D):
    def __init__(self, image_path : str, x=0, y=0, size=1, angle : float=0.0):
        super().__init__(x, y, size)
        self.image = pygame.image.load(image_path).convert_alpha()
        # Масштабs
        self.image = pygame.transform.scale(
            self.image,
            (int(self.image.get_width() * self.size),
            int(self.image.get_height() * self.size))
        )

        # Вращение
        self.angle : float = angle
        self.image = pygame.transform.rotate(self.image, -self.angle)
