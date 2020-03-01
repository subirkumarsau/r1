import pygame as pg
import random
import os
screen_width = 1024
screen_height = 650
pg.init()
pg.mixer.init()
font = pg.font.SysFont(None,30)
clock = pg.time.Clock()
gameWindow = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("SNAKE GAME BY SUBIR")
pg.display.update()
def showScore(text,color,x,y):
    temp=font.render(text,True,color)
    gameWindow.blit(temp,[x,y])
def drawSnake(color, snake_list, snake_size):
    for x,y in snake_list:
        pg.draw.circle(gameWindow,color,[x,y],snake_size)
def gameOver():
    gameExit=False
    endimg = pg.image.load("data/images/game_over.jpg")
    endimg=pg.transform.scale(endimg,(screen_width,screen_height)).convert_alpha()
    pg.mixer.music.load("data/sounds/game_over.mp3")
    pg.mixer.music.play(0)
    while(not gameExit):
        for x in pg.event.get():
            if(x.type==pg.QUIT):
                gameExit=True
            if(x.type==pg.KEYDOWN):
                if(x.key==pg.K_RETURN):
                    gameLoop()
                if(x.key==pg.K_ESCAPE):
                    gameExit=True
        gameWindow.blit(endimg,(0,0))
        pg.display.update()
        clock.tick(60)
    pg.quit()
    quit()
def welcome():
    gameExit=False
    wimg = pg.image.load("data/images/welcome.jpg")
    endimg=pg.transform.scale(wimg,(screen_width,screen_height)).convert_alpha()
    pg.mixer.music.load("data/sounds/welcome.mp3")
    pg.mixer.music.play(-1)
    while(not gameExit):
        for x in pg.event.get():
            if(x.type==pg.QUIT):
                gameExit=True
            if(x.type==pg.KEYDOWN):
                if(x.key==pg.K_RETURN):
                    gameLoop()
                if(x.key==pg.K_ESCAPE):
                    gameExit=True
        gameWindow.blit(endimg,(0,0))
        pg.display.update()
        clock.tick(60)
    pg.quit()
    quit()
def gameLoop():
    game_exit = False
    snake_size = 9
    snake_x = 30
    snake_y = 50
    init_vel = 3
    vel_x = init_vel
    vel_y = 0
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    fps = 60
    food_x = random.randint(20, screen_width - 100)
    food_y = random.randint(30, screen_height - 100)
    score = 0
    hiscore=0
    snake_list = []
    snake_len = 7
    back_image = pg.image.load("data/images/grey_background.jpg")
    back_image=pg.transform.scale(back_image,(screen_width,screen_height)).convert_alpha()
    foodimg = pg.image.load("data/images/food.png")
    foodimg = pg.transform.scale(foodimg,(35,35)) .convert_alpha()
    pg.mixer.music.load("data/sounds/background.mp3")
    pg.mixer.music.play(-1)
    while (not game_exit):
        for x in pg.event.get():
            if (x.type == pg.QUIT):
                game_exit = True
            if (x.type == pg.KEYDOWN):
                if (x.key == pg.K_RIGHT):
                    if (vel_x == 0):
                        vel_x = init_vel
                        vel_y = 0
                if (x.key == pg.K_LEFT):
                    if (vel_x == 0):
                        vel_x = -init_vel
                        vel_y = 0
                if (x.key == pg.K_UP):
                    if (vel_y == 0):
                        vel_y = -init_vel
                        vel_x = 0
                if (x.key == pg.K_DOWN):
                    if (vel_y == 0):
                        vel_y = init_vel
                        vel_x = 0
        snake_x += vel_x
        snake_y += vel_y
        gameWindow.blit(back_image,(0,0))
        head = [snake_x, snake_y]
        snake_list.append(head)
        if (len(snake_list) > snake_len):
            del snake_list[0]
        drawSnake(green, snake_list, snake_size)
        gameWindow.blit(foodimg,(food_x,food_y))
        if(not(os.path.exists("data/hiscore.txt"))):
            with open("data/hiscore.txt","w")as f:
                f.write(str(hiscore))
        with open("data/hiscore.txt","r") as f:
            hiscore=int(f.read())
        if(score>hiscore):
            hiscore=score
            with open("data/hiscore.txt","w") as f:
                f.write(str(hiscore))
        showScore("Score: " + str(score)+ "  High Score: "+ str(hiscore) ,yellow, screen_width-295, 7)
        temp_x=food_x+17
        temp_y=food_y+17
        if (abs(snake_x - temp_x) < 20 and abs(snake_y - temp_y) < 20):
            score += 10
            snake_len += 5
            food_x = random.randint(20, screen_width - 100)
            food_y = random.randint(30, screen_height - 100)
            eat = pg.mixer.Sound("data/sounds/eat.wav")
            eat.play()
            if (score > 0 and score % 100 == 0):
                init_vel += 1
        if (snake_x > screen_width or snake_x < 0 or snake_y < 0 or snake_y > screen_height or head in snake_list[: -1]):
            gameOver()
        pg.display.update()
        clock.tick(fps)
    pg.quit()
    quit()
welcome()