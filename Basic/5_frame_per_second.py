import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("오락실 게임")

#FPS
clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\HanWool\\Desktop\\inflearn\\Python_Game\\Basic\\background.png")


character = pygame.image.load("C:\\Users\\HanWool\\Desktop\\inflearn\\Python_Game\\Basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

running = True
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정 - 높게 설정할 수록 빠르고 부드러움

    #print('fps: ' + str(clock.get_fps()))
    # 캐릭터가 1초 동안에 100만큼 이동을 해야함
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10 * 10 = 100이므로 10만큼!
    # 10 fps : 1초 동안에 20번 동작 -> 1번에 몇 만큼 이동? 20 * 5 = 100이므로 5만큼!  
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: 
                to_x += character_speed
            elif event.key == pygame.K_UP: 
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: 
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # 프레임이 달라진다고 속도가 달라지면 안된다.
    character_y_pos += to_y * dt 
     
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

pygame.quit()