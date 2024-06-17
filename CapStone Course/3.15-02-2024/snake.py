import pygame,random
pygame.init()

white,black,red,green,blue = (255,255,255),(0,0,0),(213,50,80),(0,255,0),(50,153,213)
dis_width,dis_height,snake_block = 300,300,10
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("JetBrains Mono", 25)

def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 12, dis_height / 6])

def gameLoop():
    x1,y1,x1_change,y1_change = dis_width / 2,dis_height / 2,0,0
    snake_List,Length_of_snake = [],1
    foodx,foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x1_change,y1_change = -snake_block,0
                elif event.key == pygame.K_RIGHT: x1_change,y1_change = snake_block,0
                elif event.key == pygame.K_UP: x1_change,y1_change = 0,-snake_block
                elif event.key == pygame.K_DOWN: x1_change,y1_change = 0,snake_block

        x1,y1 = x1+x1_change,y1+y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = [x1,y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake: del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                message("You Lost! Press C-Play Again or Q-Quit", red)
                your_score(Length_of_snake - 1)
                pygame.display.update()
                pygame.time.wait(1000)
                gameLoop()
        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx,foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(15)

gameLoop()