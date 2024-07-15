import pygame
import sys

pygame.init()


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1000
FPS = 60
GRAVITY = 0.5


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario")

player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (50, 50))
platform_image = pygame.image.load("platform.png")
platform_image = pygame.transform.scale(platform_image, (200, 20))
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


player_rect = player_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
player_speed = 5
player_velocity_y = 0
player_on_ground = False

platforms = [
    pygame.Rect(300, 400, 200, 20),
    pygame.Rect(100, 300, 200, 20),
    pygame.Rect(500, 500, 200, 20),
    pygame.Rect(700, 600, 200, 20),
    pygame.Rect(900, 700, 200, 20)
]

def apply_gravity():
    global player_velocity_y, player_on_ground
    player_velocity_y += GRAVITY
    player_rect.y += player_velocity_y
    if player_rect.bottom > SCREEN_HEIGHT:
        player_rect.bottom = SCREEN_HEIGHT
        player_velocity_y = 0
        player_on_ground = True

def check_collisions():
    global player_velocity_y, player_on_ground
    for platform in platforms:
        if player_rect.colliderect(platform):
            player_rect.bottom = platform.top
            player_velocity_y = 0
            player_on_ground = True

def update_player():
    global player_on_ground
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and player_on_ground:
        player_velocity_y = -10
        player_on_ground = False
    apply_gravity()
    check_collisions()

def draw_platforms():
    for platform in platforms:
        screen.blit(platform_image, platform.topleft)

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        update_player()


        screen.blit(background_image, (0, 0))
        screen.blit(player_image, player_rect.topleft)
        draw_platforms()
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
