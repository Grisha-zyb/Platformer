from objects import *
from levels import *

pygame.init()

level1_objects, key, chest = draw_level(level1)
player = Player(50, H - 90, 40, 50, 10, player_images)
portal = MapObject(-300, -300, 80, 80, portal_image)

level1_objects.add(portal)
level1_objects.add(player)

btn_play = Button(465, 250, 350, 100, (170,139,231), "PLAY", 60, (255, 255, 255))
btn_exit = Button(465, 550, 350, 100, (170, 139, 231), "EXIT", 60, (255, 255, 255))

mode = "menu"

game = True
finish = False
while game:
    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if mode == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_play.rect.collidepoint(x, y):
                    mode = "game"
                if btn_exit.rect.collidepoint(x, y):
                    game = False
    
    if mode == "menu":
        window.blit(bg, (0,0))
        window.blit(game_nape, (200, 50))

        btn_play.draw(120,30)
        btn_exit.draw(120,30)

    if mode == "game":
        if not finish:
            window.blit(bg, (0, 0))

            for obj in level1_objects:
                window.blit(obj.image, camera.apply(obj))
            camera.update(player)

            player.update(platforms)

    pygame.display.update()
    clock.tick(fps)