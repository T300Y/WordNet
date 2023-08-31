import pygame
import string
import random
import math
# Globals
WIDTH, HEIGHT = 1920, 1080
FPS = 60
BLACK = (0, 0, 0)

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WordNet")

all_sprites = pygame.sprite.Group()  # Declare all_sprites as a global variable

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text, font_size, font_color, x, y, screen_width, screen_height):
        super().__init__()
        self.text = text
        self.font = pygame.font.SysFont("arial", font_size)
        self.image = self.font.render(text, True, font_color)
        self.rect = self.image.get_rect()
        self.font_size = font_size
        self.rect.topleft = (x, y)
        self.velocity = pygame.Vector2(1, 1)  # Fixed velocity
        self.width = screen_width
        self.height = screen_height
        self.draw_circle = False  # Flag to indicate if circle should be drawn
        self.selected = False

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
    def toggle_selected(self):
        self.selected = not self.selected
        if not self.selected:
            self.draw_circle = False

def draw_window(selected_sprites, score):
    WIN.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(WIN)
    for sprite in all_sprites:
        if sprite.draw_circle or sprite in selected_sprites:
            pygame.draw.circle(WIN, (255, 255, 255), sprite.rect.center, 50, 2)
    selected_text = ''.join([sprite.text for sprite in selected_sprites])  # Use sprite.text
    selected_font = pygame.font.SysFont("arial", 24)
    selected_text_render = selected_font.render(selected_text, True, (255, 255, 255))
    selected_text_rect = selected_text_render.get_rect(center=(WIDTH // 2, 30))
    WIN.blit(selected_text_render, selected_text_rect)

    # Display the score
    score_font = pygame.font.SysFont("arial", 24)
    score_text = f"Score: {score}"
    score_text_render = score_font.render(score_text, True, (255, 255, 255))
    score_text_rect = score_text_render.get_rect(topright=(WIDTH - 20, 20))
    WIN.blit(score_text_render, score_text_rect)

    pygame.display.flip()
    pygame.display.flip()
def main():
    dictionary = read_dict()
    array_of_sprites = []
    no_active_letters = 0
    selected_sprites = []
    score = 0  # Initialize score to 0

    clock = pygame.time.Clock()
    run = True

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
                        if sprite in selected_sprites:
                            selected_sprites.remove(sprite)
                            sprite.toggle_selected()
                        else:
                            selected_sprites.append(sprite)
                            sprite.toggle_selected()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Check if selected letters form a valid word
                selected_text = ''.join([sprite.text for sprite in selected_sprites])
                if selected_text in dictionary and not dictionary[selected_text]:
                    for sprite in selected_sprites:
                        sprite.toggle_selected()
                        all_sprites.remove(sprite)  # Remove the sprite from the group
                    dictionary[selected_text] = True
                    selected_sprites.clear()
                    score += word_score(selected_text, dictionary)  # Increment score for correct word
                else:
                    selected_sprites.clear()
                    score = max(0, score - 1)  # Decrease score for incorrect word, but not below 0

        if len(array_of_sprites) < 15:
            array_of_sprites, no_active_letters = letter_generator(array_of_sprites, no_active_letters, dictionary)

        draw_window(selected_sprites, score)  # Pass the score to the draw_window function

    pygame.quit()
def random_letter():
    random = 0
    ranges = {
    'a': 8167,  'b': 9659,  'c': 12441, 'd': 16694,
    'e': 29396, 'f': 31624, 'g': 33639, 'h': 39733,
    'i': 46699, 'j': 46852, 'k': 47624, 'l': 51649,
    'm': 54055, 'n': 60804, 'o': 68311, 'p': 70240,
    'q': 70335, 'r': 76322, 's': 82649, 't': 91705,
    'u': 94463, 'v': 95441, 'w': 97801, 'x': 97951,
    'y': 99925, 'z': 100000
    }
    random = random.randint(0,100000)
    for letter in alphabet:
        if random< alphabet[letter]:
            print(letter)
            return letter

def letter_generator(array_of_sprites, no_of_sprites, dictionary):
    global all_sprites
    letters_generated = []
    while True:
        letters_generated = [random_letter() for i in range(15)]
        if check_letters(letters_generated, dictionary):
            break
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

def read_dict():

    #Change this to a hash table and make a has function
    with open("words.txt") as file:
        lines=(file.readlines())
        lines = {(line.replace("\n", "")):False for line in lines}
    file.close()
    return lines

def word_score(word, dictionary):
    points = 0
    points += len(word)
    print(points)
    points *= (backwards_score(word, dictionary)* is_palindrome(word,dictionary) * is_rotatable(word, dictionary))
    print(points)
    points += embedded_word(word, dictionary)
    print(points)
    return points
    
    
def backwards_score(word, dictionary):
    word = word[::-1]
    if word in dictionary:
        return 2
    else:
        return 1
    
def is_palindrome(word, dictionary):
    palindrome = word[::-1]
    if palindrome == word:
        return 5
    else:
        return 1
def is_rotatable(word, dictionary):
    new_word = word[1:] + word[0]
    if new_word in dictionary:
        return 10
    else:
        return 1
            
def embedded_word(word, dictionary):
    score = 0
    word_length = len(word)
    
    for i in range(word_length):
        for j in range(i + 1, word_length + 1):
            subword = word[i:j]
            if subword in dictionary and subword != word:
                if dictionary[subword]:
                    print(subword)
                    print(dictionary[subword])
                    score += 10
    
    return score

def check_letters(lttr_arr, dictionary):
    selected_letter_freq = {}
    
    # Count the frequency of each letter in the selected letters array
    for letter in lttr_arr:
        if letter in selected_letter_freq:
            selected_letter_freq[letter] += 1
        else:
            selected_letter_freq[letter] = 1
    
    valid_words = 0
    
    # Iterate through the words in the dictionary
    for word in dictionary:
        word_letter_freq = {}
        
        # Count the frequency of each letter in the word
        for letter in word:
            if letter in word_letter_freq:
                word_letter_freq[letter] += 1
            else:
                word_letter_freq[letter] = 1
        
        # Compare the letter frequencies of the word and selected letters
        is_valid_word = True
        for letter, freq in word_letter_freq.items():
            if letter not in selected_letter_freq or selected_letter_freq[letter] < freq:
                is_valid_word = False
                break
        
        if is_valid_word:
            valid_words += 1
    
    return valid_words



if __name__ == '__main__':
    main()