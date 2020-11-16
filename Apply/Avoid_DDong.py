# 하늘에서 떨어지는 똥 피하기 게임을 만드시오.

import pygame
import random

pygame.init() # 초기화 반드시 필요

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임")

#FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\HanWool\\Desktop\\inflearn\\Python_Game\\Apply\\background.png") # 탈출 문자 때문에 \\ 로 쓰거나 / 로 쓰면 된다.

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\HanWool\\Desktop\\inflearn\\Python_Game\\Apply\\character.png") # 캐릭터는 배경과 달리 움직여야 하므로 추가 코드가 필요
character_size = character.get_rect().size # 캐릭터의 이미지 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적(enemy) 캐릭터 만들기
enemy = pygame.image.load("C:\\Users\\HanWool\\Desktop\\inflearn\\Python_Game\\Apply\\DDong.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width - enemy_width) / 2
enemy_y_pos = 0

# 폰트 정의
game_font = pygame.font.Font(None, 40) # None은 default font, 40은 크기

# 이벤트 루프 - 창이 꺼지지 않도록!
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정 - 높게 설정할 수록 빠르고 부드러움

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는지 체크
        if event.type == pygame.QUIT: # 창 닫기 버튼을 누르면
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 0.5
            elif event.key == pygame.K_RIGHT:
                to_x += 0.5
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt # 프레임이 달라진다고 속도가 달라지면 안된다.
    character_y_pos += to_y * dt 

    # 가로 경계값 처리 - 캐릭터
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 적의 움직임
    enemy_y_pos += 3
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 충돌 처리
    character_rect = character.get_rect() # 캐릭터의 position update
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect): # 충돌했으면
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0)) # 맨 왼쪽 맨 위 (0, 0)에 background 삽입 / screen.fill((R, G, B)로 background image 없이 색으로 칠할 수 있다.
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 - 위치의 왼쪽 위 꼭짓점을 입력!
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update() # 화면을 계속해서 그려주어야 background image가 포함된다.

# pygame 종료
pygame.quit()