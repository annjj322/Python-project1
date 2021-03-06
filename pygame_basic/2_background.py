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

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 생성되는 이벤트 (클릭이나 마우스 움직임, 키보드 입력 등등)
        if event.type == pygame.QUIT: # X버튼을 누르면 창이 닫힌다.
            running = False

    #screen.fill((0,0,255)) 그림을 넣기보다 색을 넣을 수도 있다
    screen.blit(background, (0,0)) # 배경 그리기

    pygame.display.update() # 게임화면을 다시 그리기! 반드시 호출이 되어야 되는 부분.
    

# pygame 종료
pygame.quit()