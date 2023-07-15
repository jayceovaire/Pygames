import pygame
import random

class Player():
    def __init__(self, SCR_WID, SCR_HEI):
        self.speed = 4
        self.x = SCR_WID // 2
        self.y = SCR_HEI // 2
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)
        player_image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(player_image, (self.width, self.height))
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

    def movement(self, keys, SCR_WID, SCR_HEI):
        if keys[pygame.K_LEFT] and self.x - self.speed > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.width + self.speed < SCR_WID:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y - self.speed > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.height + self.speed < SCR_HEI:
            self.y += self.speed

def main():
    pygame.init()

    SCR_WID, SCR_HEI = 980, 640
    SCREEN = pygame.display.set_mode((SCR_WID, SCR_HEI))
    BACKGROUND = (255, 255, 255)
    FPS = 60

    pygame.display.set_caption("Fight Bill Cipher")

    # player
    player = Player(SCR_WID, SCR_HEI)
    game_active = True

    while game_active:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

        keys = pygame.key.get_pressed()
        player.movement(keys, SCR_WID, SCR_HEI)

        SCREEN.fill(BACKGROUND)
        player.draw(SCREEN)

        pygame.display.flip()
        pygame.time.wait(1000//FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
