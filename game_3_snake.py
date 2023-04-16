import pygame,random
 

#initialize pygame
pygame.init()

#create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~snake~~")



# define a clock to slow down the while loop and make sure it runs at the same speed on every single computer (FPS = frame per second)
FPS  = 20
clock = pygame.time.Clock()
#VELOCITY = 10 it runs 10 times a second


#set game values
SNAKE_SIZE = 20
head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100
snake_dx = 0
snake_dy = 0
score = 0


#colors
BLUE = (1,175,209)
YELLOW = (248, 231,28)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
RED = (255,0,0)

#set fonts
font = pygame.font.Font("Franxurter.ttf", 32)

#set text 
title_text = font.render("~~ SNAKE ~~", True, YELLOW)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_text = font.render("Score: "+ str(score), True, RED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("Game Over!", True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2 , WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to continue!", True, BLUE, YELLOW)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2 , WINDOW_HEIGHT//2+ 60)

#set music
cpickup_sound = pygame.mixer.Sound("click_sound.wav")

#set images
#for a rectsnagle (top-left.x, top-left.y , width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw. rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw. rect(display_surface, RED, head_coord)

body_coords = []


#the main game loop
running = True
while running:
    #lopp through a list of ecents 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False 
         
 
    #blit the HUD
    display_surface.fill(WHITE)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    #blit assets
    pygame.draw.rect(display_surface, GREEN, head_coord)
    pygame.draw.rect(display_surface, RED, apple_coord)

        
    #update the display
    pygame.display.update()
    
    #tick the clock
    clock.tick(FPS)

           
# end the  game
pygame.quit()
