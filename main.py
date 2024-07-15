import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.5

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario")

# Игровые объекты
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5
        self.velocity_y = 0
        self.on_ground = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.on_ground:
            self.velocity_y = -10
            self.on_ground = False

        # Применение гравитации
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Проверка выхода за границы экрана
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity_y = 0
            self.on_ground = True

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Level:
    def __init__(self, player):
        self.player = player
        self.platforms = pygame.sprite.Group()
        self.create_level()

    def create_level(self):
        # Пример платформ
        platform1 = Platform(300, 500, 200, 20)
        platform2 = Platform(100, 450, 200, 20)
        self.platforms.add(platform1, platform2)

    def update(self):
        self.platforms.update()
        self.check_collisions()

    def check_collisions(self):
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.rect.bottom = hits[0].rect.top
            self.player.velocity_y = 0
            self.player.on_ground = True

    def draw(self, screen):
        self.platforms.draw(screen)

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    player = Player()
    level1 = Level(player)
    level2 = Level(player)  # Можно создать другой уровень с другими платформами
    levels = [level1, level2]
    current_level_index = 0
    current_level = levels[current_level_index]

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        all_sprites.update()
        current_level.update()

        # Проверка перехода на следующий уровень
        if player.rect.x > SCREEN_WIDTH:
            current_level_index = (current_level_index + 1) % len(levels)
            current_level = levels[current_level_index]
            player.rect.x = 0

        # Рендеринг
        screen.fill(WHITE)
        all_sprites.draw(screen)
        current_level.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()