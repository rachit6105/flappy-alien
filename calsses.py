import pygame
import sys
import random
import datetime

class MySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y,screen_width,screen_height):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (50, 50))  # Load the image
        self.rect = self.image.get_rect()  # Get the rectangle of the image
        self.rect.x = x  # Set x position
        self.rect.y = y  # Set y position
        self.screen_width=screen_width
        self.screen_height=screen_height
    def update(self, keys):
        clock = pygame.time.Clock()

        dt = clock.tick(60) / 1000
        if self.rect.top < 0:
            self.rect.top = 0
        if keys[pygame.K_w]:
            self.rect.y -= 300 * dt
        if keys[pygame.K_s]:
            self.rect.y += 300 * dt
        if keys[pygame.K_a]:
            self.rect.x -= 300 * dt
        if keys[pygame.K_d]:
            self.rect.x += 300 * dt
        if self.rect.x <0 :
            self.rect.x = 0
        if self.rect.x > self.screen_width :
            self.rect.x = self.screen_width
        if self.rect.y>self.screen_width-40:
            self.rect.y = self.screen_width-40



def random_color_channel():
    # Choose a random color channel: Red, Green, or Blue
    color_channel = random.choice(['R', 'G', 'B'])
    if color_channel == 'R':
        return (255, 0, 0)
    elif color_channel == 'G':
        return (0, 255, 0)
    else:
        return (0, 0, 255)

# Example usage
WIDTH,HEIGHT=800,600

class bala(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        pygame.draw.circle(self.image, (66, 158, 56), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(0, HEIGHT-40)

    def update(self,speed):
        self.rect.x -= speed*random.randint(1, 5)
        if self.rect.x < 0:
            self.rect.x = WIDTH
            self.rect.y = random.randint(0, HEIGHT)
            self.speed = random.randint(1, 5)*speed
    def draw(self, screen):
        pygame.draw.circle(screen, (66, 158, 56), (self.rect.x, self.rect.y), 10)


class Dart(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        image = pygame.image.load(r"C:\Users\91820\OneDrive\Desktop\huma\dart-11530964834pvokt1feau.png")
        self.image=pygame.transform.scale(image,(30,30))
        self.rect = self.image.get_rect(center=pos)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH:
            self.kill()

            
# class Ball(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__
#         self.x = WIDTH
#         self.y = random.randint(0, HEIGHT)
#         self.rect = pygame.Rect(self.x, self.y, 10*2, 10*2)
#     def update(self,speed):
#         self.speed=speed*random.randint(1,5)
#         self.x -= self.speed
#         if self.x < 0:
#             self.x = WIDTH
#             self.y = random.randint(0, HEIGHT)
#             self.speed = speed*random.randint(1,5)

#     def draw(self, screen):
#         pygame.draw.circle(screen, (66, 158, 56), (self.x, self.y), 10)


