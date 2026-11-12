import pygame
import time
pygame.init()
back = (190, 255, 12)
mw = pygame.display.set_mode((900, 500))
mw.fill(back)
dx = 3
dy = 3
platform_x = 50
platform_x2 = 850
platform_y = 330
move_up= False
move_down= False 
move_right = False
move_left = False
game_over = False
clock = pygame.time.Clock()
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None): 
        self.rect = pygame.Rect(x, y, width, height)  
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('Times New Roman', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.transform.scale(pygame.image.load(filename),(width, height))
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

ball = Picture('2.png', 160, 200, 50, 50)
platform = Picture('3.png', platform_x, platform_y, 30, 100)
platform2= Picture('3.png', platform_x2, platform_y, 30, 100)
start_x = 5
start_y = 5
count = 9

j = 0
for i in range(3):
    y = start_y + (55 * i)
    x = start_x + (27.5 * j)
    
    count = count - 1
    j += 1
while not game_over:
    mw.fill(back)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move_right = True 
            if event.key == pygame.K_UP:
                move_left = True 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                move_right = False
            if event.key == pygame.K_UP:
                move_left = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                move_up = True 
            if event.key == pygame.K_w:
                move_down = True 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                move_up = False
            if event.key == pygame.K_w:
                move_down = False  
    if platform.rect.y < 400:
        platform.rect.y += 3   
    if platform.rect.y > 0:
        platform.rect.y -= 3
    if move_right:
        platform.rect.y += 3
    if move_left:
        platform.rect.y -= 3
    
    if platform2.rect.y < 400:
        platform2.rect.y += 3   
    if platform2.rect.y > 0:
        platform2.rect.y -= 3
    if move_up:
        platform2.rect.y += 3
    if move_down:
        platform2.rect.y -= 3
    ball.rect.x += dx
    ball.rect.y += dy
    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.x > 850 or ball.rect.x < 0:
        dx *= -1
    if ball.rect.y > 450:
        dy *= -1
    if ball.rect.colliderect(platform.rect):
        dx *= -1 
    if ball.rect.colliderect(platform2.rect):
        dx *= -1
    platform.draw()
    platform2.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(80)