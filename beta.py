import pygame
import random
import datetime
import math
from calsses import *
pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
value = 6
start_time = datetime.datetime.now()
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set up the clock
clock = pygame.time.Clock()
bg = pygame.image.load(r"C:\Users\91820\OneDrive\Desktop\huma\dg34rsu-29a3d144-dc3f-473e-a949-f73a4ba1ef7c.png")
bg =pygame.transform.scale(bg, (800, 600))

all_sprites = pygame.sprite.Group()

# Create your sprite
my_sprite = MySprite(r"C:\Users\91820\OneDrive\Pictures\Screenshots\sidhu.png", 50, 50,screen_width = 800,screen_height = 600)
sprite2 =MySprite(r"dg34rsu-29a3d144-dc3f-473e-a949-f73a4ba1ef7c.png", 100, 100,screen_width = 800,screen_height = 600)
all_sprites.add(my_sprite)

balls = pygame.sprite.Group(bala() for _ in range(30))
HP = 20

darts = pygame.sprite.Group()
game_over=0
BAR_LENGTH = 100
BAR_HEIGHT = 20
max_health=20
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dart = Dart(my_sprite.rect.midright)
                darts.add(dart)

    # Update the game
    current_time = datetime.datetime.now()
    screen.blit(bg, (0, 0))
    darts.update()

    time_difference = current_time - start_time
    value += time_difference.total_seconds()
    speed  = math.log1p(math.log1p(value))

    if pygame.sprite.spritecollide(my_sprite, balls,True):
        HP -= 1
        balls.add(bala())

    for ball in balls:
        ball.update(speed)

    if pygame.sprite.groupcollide(darts, balls,True,True):
        balls.add(bala())

    for ball in balls:
        ball.draw(screen)

    keys = pygame.key.get_pressed()
    my_sprite.update(keys)
    all_sprites.draw(screen)
    darts.draw(screen)
    pygame.draw.rect(screen, (255,0,0), (20, 20, BAR_LENGTH, BAR_HEIGHT))  # Red bar
    pygame.draw.rect(screen, (0,255,0), (20, 20, BAR_LENGTH * (HP/max_health), BAR_HEIGHT))  # Green bar

    if HP==0:
        game_over=1

    if game_over:
        # Create a new surface with the game over text
        text_surface = my_font.render("Game Over", True, (0,0,0))
        # Scale up the surface to create a pixelated effect
        pixelated_surface = pygame.transform.scale(text_surface, (WIDTH/10, HEIGHT/10))
        # Draw the pixelated surface on the screen
        screen.blit(pixelated_surface, (WIDTH/2, HEIGHT/2))
        speed=0
        pygame.time.delay(50)
        pygame.quit()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

pygame.quit()
