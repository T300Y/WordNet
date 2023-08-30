import pygame
pygame.init()
class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text, font_size, font_color,speed_x,speed_y, x, y, screen_width,screen_height):
        super().__init__()

        self.font = pygame.font.SysFont("arial", font_size)
        self.image = self.font.render(text, True, "white")
        self.rect = self.image.get_rect()
        self.font_size=font_size
        self.rect.topleft = (x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.width = screen_width
        self.height = screen_height
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if (self.rect.x <0) or (self.rect.x > self.width-self.font_size):
                self.speed_x *= -1
        if (self.rect.y<0) or (self.rect.y > self.height-self.font_size):
            self.speed_y *= -1

        self.rect.x =self.rect.x + self.speed_x
        self.rect.y =self.rect.y + self.speed_y
        # Wrap around screen edges
        if self.rect.right < 0:
            self.rect.left = self.width 
        elif self.rect.left > self.width:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = self.height
        elif self.rect.top > self.height:
            self.rect.bottom = 0
        collide_list = pygame.sprite.spritecollide(self, group, True)
        
