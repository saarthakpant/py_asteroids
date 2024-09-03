import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.positon = pygame.Vector2(x, y) 
        self.vector  = pygame.Vector2(0, 0) 
        self.radius = radius
            
    def draw(self, screen):
        pass
    
    def update(self, dt):
        pass