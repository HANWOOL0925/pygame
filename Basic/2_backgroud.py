import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("오락실 게임")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\HanWool\\Desktop\\inflearn\\Python_Game\\Basic\\background.png") # 탈출 문자 때문에 \\ 로 쓰거나 / 로 쓰면 된다.

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0)) # 맨 왼쪽 맨 위 (0, 0)에 background 삽입 / screen.fill((R, G, B)로 background image 없이 색으로 칠할 수 있다.

    pygame.display.update() # 화면을 계속해서 그려주어야 background image가 포함된다.

pygame.quit()