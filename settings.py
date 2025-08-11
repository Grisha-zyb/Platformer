import pygame

pygame.init()

W, H = 1280, 700
fps = 30
coins_count = 0
is_key = False
level_count = 1
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Platformer")
pygame.display.set_icon(pygame.image.load("assets/character/frame1.png"))

clock = pygame.time.Clock()

platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()

bg = pygame.transform.scale(pygame.image.load("assets/background/background.jpg"), (W, H))

platform_image = pygame.image.load("assets/platform/platform.png")

player_images = [
    pygame.image.load("assets/character/frame1.png"),
    pygame.image.load("assets/character/frame2.png"),
    pygame.image.load("assets/character/frame3.png"),
    pygame.image.load("assets/character/frame4.png"),
    pygame.image.load("assets/character/frame5.png"),
    pygame.image.load("assets/character/frame6.png"),
    pygame.image.load("assets/character/frame7.png"),
    pygame.image.load("assets/character/frame8.png"),
]

coin_image = pygame.image.load("assets/crystal/crystal.png")

portal_image = [
    pygame.image.load("assets/portal/frame01.png"),
    pygame.image.load("assets/portal/frame02.png"),
    pygame.image.load("assets/portal/frame03.png"),
    pygame.image.load("assets/portal/frame04.png"),
    pygame.image.load("assets/portal/frame05.png"),
]

key_image = pygame.image.load("assets/key/key.png")
chest_image = pygame.image.load("assets/chest/chest.png")

pygame.font.init()
font1 = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 80)
font3 = pygame.font.SysFont(None, 160, bold = True)

find_key_txt = font2.render("Знайди ключ!", True, (255,255,255))
open_chest_txt = font2.render("Натисни Е щоб відкрити!", True, (255,255,255))
get_key_txt = font2.render("Натисни Е щоб підібрати!", True, (255,255,255))
game_nape = font3.render("sss",True,(116,89,70), (255,255,255))