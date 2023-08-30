import pygame
import string
import random
import math
# Globals
WIDTH, HEIGHT = 900, 500
FPS = 60
BLACK = (0, 0, 0)

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WordNet")

all_sprites = pygame.sprite.Group()  # Declare all_sprites as a global variable

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text, font_size, font_color, x, y, screen_width, screen_height):
        super().__init__()

        self.font = pygame.font.SysFont("arial", font_size)
        self.image = self.font.render(text, True, font_color)
        self.rect = self.image.get_rect()
        self.font_size = font_size
        self.rect.topleft = (x, y)
        self.velocity = pygame.Vector2(1.5, 1.5)  # Fixed velocity
        self.width = screen_width
        self.height = screen_height
        self.draw_circle = False  # Flag to indicate if circle should be drawn


    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Prevent going beyond screen edges
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x *= -1
        if self.rect.right > self.width:
            self.rect.right = self.width
            self.velocity.x *= -1
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y *= -1
        if self.rect.bottom > self.height:
            self.rect.bottom = self.height
            self.velocity.y *= -1

        #collide_list = pygame.sprite.spritecollide(self, all_sprites, False)
        #for sprite in collide_list:
            #if sprite != self:
              #  if self.check_collision(sprite):
                 #   self.resolve_collision(sprite)
                  #  self.rect.move_ip(-self.velocity.x, -self.velocity.y)
              #  break

    def check_collision(self, other_sprite):
        axes = [self.velocity.normalize(), pygame.Vector2(-self.velocity.y, self.velocity.x).normalize()]
        for axis in axes:
            proj_self = [pygame.Vector2(corner).dot(axis) for corner in self.get_corners()]
            proj_other = [pygame.Vector2(corner).dot(axis) for corner in other_sprite.get_corners()]

            if proj_self[0] > proj_other[1] or proj_self[1] < proj_other[0]:
                return False
        return True

    def get_corners(self):
        corners = [
            self.rect.topleft,
            self.rect.topright,
            self.rect.bottomleft,
            self.rect.bottomright
        ]
        return corners

    def resolve_collision(self, other_sprite):
        relative_velocity = self.velocity - other_sprite.velocity
        collision_normal = pygame.Vector2(other_sprite.rect.center) - pygame.Vector2(self.rect.center)
        collision_normal = collision_normal.normalize()
        impulse = 2 * relative_velocity.dot(collision_normal)
        self.velocity = self.velocity
        other_sprite.velocity += impulse * collision_normal

def draw_window():
    WIN.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(WIN)
    for sprite in all_sprites:
        if sprite.draw_circle:
            pygame.draw.circle(WIN, (255,255,255), sprite.rect.center, 50, 2)
    pygame.display.flip()

def main():
    array_of_sprites = []
    no_active_letters = 0

    clock = pygame.time.Clock()
    run = True
    selected_sprite = None  # Variable to keep track of the selected sprite

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Left-click event
                mouse_position = pygame.mouse.get_pos()
                for sprite in all_sprites:
                    if sprite.rect.collidepoint(mouse_position):
                        if selected_sprite is not None:
                            selected_sprite.draw_circle = False  # Deselect the previously selected sprite
                        sprite.draw_circle = True  # Set the flag to draw circle for the clicked sprite
                        selected_sprite = sprite  # Update the selected sprite
                    else:
                        sprite.draw_circle = False

        if len(array_of_sprites) < 15:
            array_of_sprites, no_active_letters = letter_generator(array_of_sprites, no_active_letters)

        draw_window()

    pygame.quit()
def random_letter():
    alphabet = list(string.ascii_lowercase)
    return alphabet[random.randint(0, len(alphabet) - 1)]

def letter_generator(array_of_sprites, no_of_sprites):
    global all_sprites

    while True:
        x = random.randint(50, WIDTH - 50)  # Adjusted the range to ensure some padding from the edges
        y = random.randint(50, HEIGHT - 50)  # Adjusted the range to ensure some padding from the edges
        text_sprite = TextSprite(random_letter(), 36, (255, 0, 0), x, y, WIDTH, HEIGHT)
        
        # Check for collisions with existing sprites
        collision = False
        for sprite in all_sprites:
            if sprite != text_sprite and text_sprite.check_collision(sprite):
                collision = True
                break
        
        if not collision:
            array_of_sprites.append(text_sprite)
            all_sprites.add(text_sprite)
            no_of_sprites += 1
            break

    return array_of_sprites, no_of_sprites
if __name__ == '__main__':
    main()