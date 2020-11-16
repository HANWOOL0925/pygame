import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("오락실 게임")


background = pygame.image.load("C:\\Users\\HanWool\\Desktop\\inflearn\\Python_Game\\Basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\HanWool\\Desktop\\inflearn\\Python_Game\\Basic\\character.png") # 캐릭터는 배경과 달리 움직여야 하므로 추가 코드가 필요
character_size = character.get_rect().size # 캐릭터의 이미지 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래에 해당하는 곳에 위치



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 - 위치의 왼쪽 위 꼭짓점을 입력!
    pygame.display.update()

pygame.quit()