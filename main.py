import sys
import pygame
from random import randint


class Rocket:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


skin = '1'

print(f'Приветствуем вас в игре Copter!\n-------------------')
while True:
    print(f'Вы в главном меню\n'
          f'1 - Запуск игры\n'
          f'2 - Выбор скина\n'
          f'3 - Выход из игры\n-------------------')
    n = input()
    if n == '1':
        break
    elif n == '2':
        print(f'Выберите скин:\n'
              f'1 - Стандартный\n'
              f'2 - Военный\n'
              f'3 - Hello kitty\n'
              f'4 - МЧС\n')
        skin = input()
    elif n == '3':
        sys.exit()
    else:
        print(f'Я вас не понимаю\n')

if skin == '1':
    skin = 'Стандартный'
elif skin == '2':
    skin = 'Военный'
elif skin == '3':
    skin = 'Hello kitty'
elif skin == '4':
    skin = 'МЧС'


def start_screen():
    intro_text = [" " * 55 + "Copter",
                  "",
                  "Управляйте вертолетом клавишами со стрелкой, уворачиваясь от блоков",
                  " " * 50 + "Приятной игры!"]

    font = pygame.font.Font(None, 30)
    text_coord = 100
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 250
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print('Игра закрыта')
                input()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(80)


pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Copter by Baty")

clock = pygame.time.Clock()

start_screen()

running = True

rockets = []

# спрайты

bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (1280, 720))

heli_left = pygame.image.load(f'{skin}_left.png')
heli_left = pygame.transform.scale(heli_left, (256, 256))

heli_right = pygame.image.load(f'{skin}_right.png')
heli_right = pygame.transform.scale(heli_right, (256, 256))

x = 25
y = 25

speed_x = 0
speed_y = 0

up_key = False
side = "right"

while True:
    if up_key:
        speed_y = speed_y - 0.5
    else:
        speed_y = speed_y + 0.5
    if speed_y > 7:
        speed_y = 7
    if speed_y < -7:
        speed_y = -7

    # выход за границы
    if x > (width + 257):
        x = -256
    if x < -257:
        x = (width + 256)
    if y > (height + 257):
        y = -256
    if y < -257:
        y = (height + 256)

    x = x + speed_x
    y = y + speed_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print('Игра закрыта')
            input()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed_x = 5
                side = "right"
            if event.key == pygame.K_LEFT:
                speed_x = -5
                side = "left"
            if event.key == pygame.K_UP:
                up_key = True
            if event.key == pygame.K_DOWN:
                speed_y = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_UP:
                up_key = False

    screen.blit(bg, (0, 0))

    if len(rockets) < 3:
        n = Rocket(width, randint(0, 1080), 30, 'red')
        rockets.append(n)

    for rocket in rockets:
        if 0 < rocket.x < (width + 1):
            rocket.x -= 10
            rocket.draw(screen)
            h = pygame.Rect(x, y, 256, 256)
            if h.collidepoint(rocket.x, rocket.y) or h.collidepoint(rocket.x, rocket.y):
                pygame.quit()
                print('Игра окончена')
                input()
        else:
            rockets.pop(rockets.index(rocket))

    if side == "right":
        screen.blit(heli_right, (x, y))
    else:
        screen.blit(heli_left, (x, y))

    pygame.display.flip()
    clock.tick(80)
