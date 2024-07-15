import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_SIZE = 100
ENEMY_SIZE = 100
FPS = 60
GRAVITY = 0.5
PLAYER_HEALTH = 100

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Загрузка текстур
player_image_right = pygame.image.load('playerright.png')
player_image_left = pygame.image.load('playerleft.png')
enemy_image_right = pygame.image.load('enemyright.png')
enemy_image_left = pygame.image.load('enemyleft.png')
background_image = pygame.image.load('background.png')

# Изменение размера текстур
player_image_right = pygame.transform.scale(player_image_right, (PLAYER_SIZE, PLAYER_SIZE))
player_image_left = pygame.transform.scale(player_image_left, (PLAYER_SIZE, PLAYER_SIZE))
enemy_image_right = pygame.transform.scale(enemy_image_right, (ENEMY_SIZE, ENEMY_SIZE))
enemy_image_left = pygame.transform.scale(enemy_image_left, (ENEMY_SIZE, ENEMY_SIZE))
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Vitalya")

# Игрок
player = {
    'image': player_image_right,
    'rect': player_image_right.get_rect(),
    'speed': 5,
    'vel_y': 0,
    'on_ground': False,
    'health': PLAYER_HEALTH
}
player['rect'].x = SCREEN_WIDTH // 2
player['rect'].y = SCREEN_HEIGHT // 2

# Функция для создания врагов
def create_enemies():
    enemies = []
    for i in range(5):
        enemy = {
            'image': enemy_image_right,
            'rect': enemy_image_right.get_rect(),
            'vel_y': 0,
            'speed': 2,
            'direction': 1
        }
        enemy['rect'].x = i * 300 + 100
        enemy['rect'].y = SCREEN_HEIGHT // 2
        enemies.append(enemy)
    return enemies

# Враги
enemies = create_enemies()

# Платформы
platforms = []
platform = {
    'rect': pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
}
platforms.append(platform)

# Камера
camera = pygame.Rect(0, 0, 3000, 2000)  # Размер игрового мира

def update_player(keys, platforms):
    global enemies
    player['vel_y'] += GRAVITY
    player['rect'].y += player['vel_y']

    if keys[pygame.K_LEFT]:
        player['rect'].x -= player['speed']
        player['image'] = player_image_left
    if keys[pygame.K_RIGHT]:
        player['rect'].x += player['speed']
        player['image'] = player_image_right

    player['on_ground'] = False
    for platform in platforms:
        if player['rect'].colliderect(platform['rect']):
            if player['vel_y'] > 0:
                player['rect'].bottom = platform['rect'].top
                player['vel_y'] = 0
                player['on_ground'] = True

    if keys[pygame.K_UP] and player['on_ground']:
        player['vel_y'] = -10

    for enemy in enemies:
        if player['rect'].colliderect(enemy['rect']):
            if player['vel_y'] > 0:
                enemies.remove(enemy)
                player['vel_y'] = -10
            else:
                player['health'] -= 1

    # Проверка падения с платформы
    if player['rect'].top > SCREEN_HEIGHT:
        game_over_menu()
        player['health'] = PLAYER_HEALTH
        player['rect'].x = SCREEN_WIDTH // 2
        player['rect'].y = SCREEN_HEIGHT // 2
        enemies = create_enemies()

def update_enemies(platforms):
    for enemy in enemies:
        enemy['vel_y'] += GRAVITY
        enemy['rect'].y += enemy['vel_y']
        enemy['rect'].x += enemy['speed'] * enemy['direction']

        for platform in platforms:
            if enemy['rect'].colliderect(platform['rect']):
                if enemy['vel_y'] > 0:
                    enemy['rect'].bottom = platform['rect'].top
                    enemy['vel_y'] = 0

        # Изменение направления движения при столкновении с краем экрана
        if enemy['rect'].left <= 0 or enemy['rect'].right >= SCREEN_WIDTH:
            enemy['direction'] *= -1
            if enemy['direction'] == 1:
                enemy['image'] = enemy_image_right
            else:
                enemy['image'] = enemy_image_left

def update_camera(target):
    x = -target['rect'].x + int(SCREEN_WIDTH / 2)
    y = -target['rect'].y + int(SCREEN_HEIGHT / 2)

    # Ограничение движения камеры
    x = min(0, x)  # Левый край
    y = min(0, y)  # Верхний край
    x = max(-(camera.width - SCREEN_WIDTH), x)  # Правый край
    y = max(-(camera.height - SCREEN_HEIGHT), y)  # Нижний край

    camera.topleft = (x, y)

def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def main_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.fill(BLACK)
        draw_text(screen, "Супер Виталя", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text(screen, "Начать игру(Enter)", 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_text(screen, "Выйти из игры(Q)", 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        pygame.display.flip()

def game_over_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                    main_menu()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.fill(BLACK)
        draw_text(screen, "Виталя закончился", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text(screen, "Вернуться в главное меню(ENTER)", 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_text(screen, "Выйти(Q)", 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        pygame.display.flip()

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
main_menu()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    update_player(keys, platforms)
    update_enemies(platforms)
    update_camera(player)

    screen.blit(background_image, (0, 0))
    screen.blit(player['image'], player['rect'].move(camera.topleft))
    for enemy in enemies:
        screen.blit(enemy['image'], enemy['rect'].move(camera.topleft))
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform['rect'].move(camera.topleft))

    # Отображение полоски жизни
    pygame.draw.rect(screen, RED, (10, 10, PLAYER_HEALTH * 2, 20))
    pygame.draw.rect(screen, GREEN, (10, 10, player['health'] * 2, 20))

    if player['health'] <= 0:
        game_over_menu()
        player['health'] = PLAYER_HEALTH
        player['rect'].x = SCREEN_WIDTH // 2
        player['rect'].y = SCREEN_HEIGHT // 2
        enemies = create_enemies()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
