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
snake_dx = 0 # specify the direction of the snake movement
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
pickup_sound = pygame.mixer.Sound("click_sound.wav")

#set images
#for a rectsnagle (top-left.x, top-left.y , width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw. rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw. rect(display_surface, GREEN, head_coord)

body_coords = []


#the main game loop
running = True
while running:
    #lopp through a list of ecents 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False 
           
        #move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1* SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1 * SNAKE_SIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE
 
 
    # add teh haed coordinat to the first index of body coordinate/ move all the snake body
    body_coords.insert(0, head_coord)
    body_coords.pop()
    
    #update the x,y position of the snakes head and make a new coordinate
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
    
      
    #check for gameover
    if head_rect.left <0 or head_rect.right >WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom >WINDOW_HEIGHT or head_coord in body_coords:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()  
        
        #pause the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    head_x = WINDOW_WIDTH//2
                    head_y = WINDOW_HEIGHT//2 + 100
                    head_coord= (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
                    body_coords = []
                    snake_dx = 0 
                    snake_dy = 0
                    is_paused = False
                if event.type == pygame.QUIT:
                    running = False                    
                    is_paused = False

                                         
    #check for collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        pickup_sound.play()
        head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

        # new position of apple
        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
        
        body_coords.append(head_coord)
    
    #blit the HUD
    display_surface.fill(WHITE)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    #blit assets
    for body in body_coords:
        pygame.draw.rect(display_surface, GREEN, body)
        
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

    #update the HUD
    score_text = font.render("Score: "+ str(score), True, RED)

        
    #update the display
    pygame.display.update()
    
    #tick the clock
    clock.tick(FPS)

           
# end the  game
pygame.quit()
