import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("JJ Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/Junje Ahn/Desktop/Python-project1/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/Junje Ahn/Desktop/Python-project1/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width/2 # 화면 가로의 절반에 위치
character_y_pos = screen_height - character_height # 화면의 제일 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 생성되는 이벤트 (클릭이나 마우스 움직임, 키보드 입력 등등)
        if event.type == pygame.QUIT: # X버튼을 누르면 창이 닫힌다.
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확임
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= 1 # 1만큼 왼쪽으로 (to_x = to_x - 1)
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        if event.type == pygame.KEYUP: # 키를 뗐을 때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y=0
        
    character_x_pos += to_x 
    character_y_pos += to_y # while문이라서 계속 누적이 되는 값. to_x,y를 0으로 초기화한다 해도 돌아오지 X

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #screen.fill((0,0,255)) 그림을 넣기보다 색을 넣을 수도 있다
    screen.blit(background, (0,0)) # 배경 그리기

    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기! 반드시 호출이 되어야 되는 부분.
    

# pygame 종료
pygame.quit()