import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("JJ Game") # 게임 이름

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 생성되는 이벤트 (클릭이나 마우스 움직임, 키보드 입력 등등)
        if event.type == pygame.QUIT: # X버튼을 누르면 창이 닫힌다.
            running = False
# pygame 종료
pygame.quit()