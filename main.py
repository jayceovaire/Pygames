import pygame
import random

class Player:
    def __init__(self, SCR_WID, SCR_HEI):
        self.speed = 5
        self.x = SCR_WID // 2
        self.y = SCR_HEI // 2
        self.width = 40
        self.height = 40
        self.color = (255, 0, 0)
        player_image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(player_image, (self.width, self.height))
        self.max_health = 100
        self.health = self.max_health
        self.healthbar_width = 300
        self.healthbar_height = 20
        self.health_color = (255, 0, 0)
        self.healthbar = pygame.Surface((self.healthbar_width, self.healthbar_height))
        self.mask = pygame.mask.from_surface(self.image)
        self.moving = False

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
        # Update health bar width based on health percentage
        health_percentage = self.health / self.max_health
        current_health_width = int(self.healthbar_width * health_percentage)
        current_health_bar = pygame.Surface((current_health_width, self.healthbar_height))
        current_health_bar.fill(self.health_color)
        SCREEN.blit(current_health_bar, (100, 610))


    def movement(self, keys, SCR_WID, SCR_HEI):
        if keys[pygame.K_LEFT] and self.x - self.speed > 0:
            self.x -= self.speed
            self.moving = True

        if keys[pygame.K_RIGHT] and self.x + self.width + self.speed < SCR_WID:
            self.x += self.speed
            self.moving = True

        if keys[pygame.K_UP] and self.y - self.speed > 0:
            self.y -= self.speed
            self.moving = True

        if keys[pygame.K_DOWN] and self.y + self.height + self.speed < SCR_HEI:
            self.y += self.speed
            self.moving = True

        elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.moving = False


class Fist:
    def __init__(self, ftype):
        self.speed_x = 5
        self.speed_y = 5
        self.width = random.randint(10, 90)
        self.height = random.randint(10, 90)
        self.timer = pygame.time.get_ticks() + 5000
        self.type = ftype
        self.hit_player = False

        if self.type == 'fist_v_bot_l':
            fist_image = pygame.image.load('fist_bottom_left.png')
            self.image = pygame.transform.scale(fist_image, (200, 800))
            self.mask = pygame.mask.from_surface(self.image)
            self.x = random.randint(0, 980)
            self.y = 615

        if self.type == 'fist_v_bot_r':
            fist_image = pygame.image.load('fist_bottom_right.png')
            self.image = pygame.transform.scale(fist_image, (200, 800))
            self.mask = pygame.mask.from_surface(self.image)
            self.x = random.randint(0, 980)
            self.y = 615


        if self.type == 'fist_h_l':
            fist_image = pygame.image.load('fist_left_smash.png')
            self.image = pygame.transform.scale(fist_image, (700, 200))
            self.mask = pygame.mask.from_surface(self.image)
            self.x = -600
            self.y = random.randint(0, 300)

        if self.type == 'fist_h_r':
            fist_image = pygame.image.load('fist_right_smash.png')
            self.image = pygame.transform.scale(fist_image, (700, 200))
            self.mask = pygame.mask.from_surface(self.image)
            self.x = 850
            self.y = random.randint(0, 640)

        if self.type == 'fist_v_top_l':
            fist_image = pygame.image.load('fist_top_left.png')
            self.image = pygame.transform.scale(fist_image, (200, 700))
            self.mask = pygame.mask.from_surface(self.image)
            self.x = random.randint(0, 980)
            self.y = -600

        if self.type == 'fist_v_top_r':
            fist_image = pygame.image.load('fist_top_right.png')
            self.image = pygame.transform.scale(fist_image, (200, 700))
            self.mask = pygame.mask.from_surface(self.image)
            self.x = random.randint(0, 980)
            self.y = -600




    def movement(self):
        if self.type == 'fist_v_bot_l':
            self.y -= self.speed_y
            if self.y == 200:
                self.speed_y = 0
                self.x -= self.speed_x + 3

        if self.type == 'fist_v_bot_r':
            self.y -= self.speed_y
            if self.y == 200:
                self.speed_y = 0
                self.x += self.speed_x + 3

        if self.type == 'fist_h_l':
            self.x -= -self.speed_x
            if self.x == -175:
                self.speed_x = 0
                self.y += self.speed_y + 2

        if self.type == 'fist_h_r':
            self.x -= self.speed_x
            if self.x == 400:
                self.speed_x = 0
                self.y += self.speed_y + 2

        if self.type == 'fist_v_top_l':
            self.y += self.speed_y
            if self.y == -300:
                self.speed_y = 0
                self.x -= self.speed_x + 3

        if self.type == 'fist_v_top_r':
            self.y += self.speed_y
            if self.y == -300:
                self.speed_y = 0
                self.x += self.speed_x + 3

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Shadow:
    def __init__(self, stype=None):
        # Initialization code...
        self.x = random.randint(50, 930)
        self.y = random.randint(50, 590)
        self.speed_x = random.choice([3, -3])
        self.speed_y = random.choice([3, -3])
        self.width = random.randint(10, 90)
        self.height = random.randint(10, 90)
        self.size = self.height + self.width
        self.color = (0, 0, 0)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rotation_angle = 0
        self.rotation_speed = random.choice([1, -1])
        self.growing = bool(random.getrandbits(1))
        self.timer = pygame.time.get_ticks() + 15000
        self.type = stype
        self.mask = pygame.mask.from_surface(self.image)

        if self.type == 'bar_v':
            self.x = random.randint(0, 980)
            self.y = 0
            self.speed_x = random.choice([3, -3])
            self.speed_y = random.choice([3, -3])
            self.width = 20
            self.height = 1
            self.color = (0, 0, 0)
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(self.color)
            self.timer = pygame.time.get_ticks() + 4000
            self.mask = pygame.mask.from_surface(self.image)

        if self.type == 'bar_h':
            self.x = 0
            self.y = random.randint(0, 680)
            self.speed_x = random.choice([3, -3])
            self.speed_y = random.choice([3, -3])
            self.width = 1
            self.height = 20
            self.color = (0, 0, 0)
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(self.color)
            self.timer = pygame.time.get_ticks() + 4000
            self.mask = pygame.mask.from_surface(self.image)


    def movement(self, SCR_WID, SCR_HEI):

        if self.type == 'bar_v':
            if self.height < SCR_HEI:
                self.height += 6
                self.image = pygame.Surface((self.width, self.height))
                self.image.fill(self.color)
                self.mask = pygame.mask.from_surface(self.image)

        elif self.type == 'bar_h':
            if self.height < SCR_WID:
                self.width += 6
                self.image = pygame.Surface((self.width, self.height))
                self.image.fill(self.color)
                self.mask = pygame.mask.from_surface(self.image)


        else:
            self.x += self.speed_x
            self.y += self.speed_y

            if self.x <= 0 or self.x >= SCR_WID - self.width:
                self.speed_x *= -1
            if self.y <= 0 or self.y >= SCR_HEI - self.height:
                self.speed_y *= -1

            self.rotation_angle += self.rotation_speed
            if self.rotation_angle >= 360:
                self.rotation_angle = 0

            if self.growing:
                self.width += 1
                self.height += 1
            else:
                self.width -= 1
                self.height -= 1

            if self.width <= 10 or self.width >= 90:
                self.growing = not self.growing
            if self.height <= 10 or self.height >= 90:
                self.growing = not self.growing



    def draw(self, SCREEN):
        rotated_image = pygame.transform.rotate(self.image, self.rotation_angle)
        if self.width > 0 and self.height > 0:  # Check for non-negative width and height
            resized_image = pygame.transform.scale(rotated_image, (self.width, self.height))
            SCREEN.blit(resized_image, (self.x, self.y))


class Boss:
    def __init__(self, SCR_WID, SCR_HEI):

        self.forms = {
            'shadow': 'dark_cipher.png',
            'normal': 'bill.png',
            'angry': 'cipher_mad.png',
            'fire': 'cipher_blue_fire.png',
            'monster': 'cipher_monster.png',
            'monster_two': 'cipher_monster_two.png',
            'selfie': 'cipher_selfie.png'
        }
        self.form = 'monster'
       # self.form = random.choice(['shadow', 'normal', 'angry', 'fire', 'monster', 'monster_two', 'selfie'])
        self.width = 200
        self.height = 300
        self.x = SCR_WID // 2 - self.width // 2
        self.y = SCR_HEI // 2 - self.height
        boss_image = pygame.image.load(f'{self.forms[self.form]}')

        self.used_attack = False
        self.shadows_spawned = False
        self.shadows = []
        self.num_fists_spawned = 0
        self.fists_spawned = False
        self.fists = []


        if self.form == 'monster':
            self.width = 500
            self.height = 500
            self.x = SCR_WID // 2 - self.width // 2
            self.y = SCR_HEI // 2 - 200
        self.image = pygame.transform.scale(boss_image, (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)

    def shadows_attack(self):
        if self.form == 'shadow':
            if not self.shadows and self.form == 'shadow' and not self.used_attack:
                self.shadows_spawned = False
            if not self.shadows_spawned:
                shadows_spawned = random.randint(13, 23)
                for _ in range(shadows_spawned):
                    shadow = Shadow()
                    self.shadows.append(shadow)
                self.shadows_spawned = True

    def shadow_bar_attack(self):
        if self.form == 'shadow':
            if not self.shadows and self.form == 'shadow' and not self.used_attack:
                self.shadows_spawned = False
            if not self.shadows_spawned:
                shadows_spawned = 35
                for _ in range(shadows_spawned):
                    shadow = Shadow(stype=random.choice(['bar_v', 'bar_h']))
                    self.shadows.append(shadow)
                    self.shadows_spawned = True

    def choose_shadow_attack(self):
        if self.form == 'shadow':
            coinflip = random.choice([1, 2])
            if coinflip == 1:
                self.shadow_bar_attack()
            elif coinflip == 2:
                self.shadows_attack()

        if self.form == 'monster':
            self.fist_attack()

    def fist_attack(self):
        if self.form == 'monster':
            if not self.fists and self.form == 'monster' and not self.used_attack:
                self.fists_spawned = False
            if self.num_fists_spawned < 20 and not self.fists_spawned:
                fists_spawned = random.randint(2, 4)
                for _ in range(fists_spawned):
                    fist = Fist(ftype=random.choice(['fist_h_l', 'fist_h_r', 'fist_v_bot_l', 'fist_v_bot_r', 'fist_v_top_l', 'fist_v_top_r']))
                    self.fists.append(fist)
                    self.fists_spawned = True
                    self.num_fists_spawned += 1


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
        for shadow in self.shadows:
            shadow.draw(SCREEN)

def collides(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def main():
    pygame.init()

    SCR_WID, SCR_HEI = 980, 640
    SCREEN = pygame.display.set_mode((SCR_WID, SCR_HEI))
    BACKGROUND = (255, 255, 255)
    FPS = 60

    pygame.display.set_caption("Fight Bill Cipher")

    # player
    player = Player(SCR_WID, SCR_HEI)
    # boss
    boss = Boss(SCR_WID, SCR_HEI)
    game_active = True

    collided_fists = set()

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        player.movement(keys, SCR_WID, SCR_HEI)

        SCREEN.fill(BACKGROUND)
        player.draw(SCREEN)
        boss.draw(SCREEN)
        boss.choose_shadow_attack()

        if collides(player, boss):
            player.health -= .25

        for shadow in boss.shadows:
            shadow.movement(SCR_WID, SCR_HEI)
            shadow.draw(SCREEN)

            # attack timer
            if shadow.timer <= current_time:
                boss.shadows.remove(shadow)
                # boss.used_attack = True

            # collision
            if collides(player, shadow):
                boss.shadows.remove(shadow)
                if shadow.type is None:
                    if shadow.size > 90:
                        player.health -= 8
                    else:
                        player.health -= 5
                elif shadow.type == 'bar_h' or shadow.type == 'bar_v':
                    player.health -= 15

                if player.health <= 0:
                    game_active = False
                    break

        for fist in boss.fists:
            fist.movement()
            fist.draw(SCREEN)

            if fist.timer <= current_time:
                boss.fists.remove(fist)

            if collides(player, fist):
                if fist not in collided_fists:
                    player.health -= 35
                    collided_fists.add(fist)





            if player.health <= 0:
                game_active = False
                break




        pygame.display.flip()
        pygame.time.wait(1000 // FPS)

    pygame.quit()


if __name__ == '__main__':
    main()

