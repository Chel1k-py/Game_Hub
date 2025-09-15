import random
import pygame
import sys
from enemy import Enemy
from explosionEffect import ExplosionEffect
import settings_stats




def events(aim):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                aim.mright = True
                print("+1")

            if event.key == pygame.K_a:
                aim.mleft = True
                print("+2")




        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                aim.mright = False
                print("-1")
            if event.key == pygame.K_a:
                aim.mleft = False
                print("-2")


def update_display(master, aim, enemies, followers, effects_group, hearts, score):
    master.fill(f"#{settings_stats.stat['bg_color']}")
    effects_group.update()
    effects_group.draw(master)
    hearts.draw()
    score.draw()
    for follower in followers.sprites():
        follower.draw_follower()
    aim.output()
    enemies.draw(master)
    pygame.display.flip()


def create_enemy(master, enemies):
    enemy = Enemy(master)
    x, y = master.get_size()
    enemy.rect.x = random.randint(20, x - 20)
    enemies.add(enemy)


def count_frame(master, enemies):
    stat = settings_stats.stat
    if stat['frame'] % 200 == 0:
        create_enemy(master, enemies)
        stat['frame'] += 1
    elif stat['frame'] % 601 == 0 and stat['speed_enemy'] > 8:
        stat['speed_enemy'] += 500
        stat['frame'] += 1
    else:
        stat['frame'] += 1


def run_update_enemies(enemies, follower, effects_group):
    stat = settings_stats.stat
    enemies.update(effects_group, enemies)
    collishions = pygame.sprite.groupcollide(follower, enemies, False, True)

    for follower_sprite, hit_enemies in collishions.items():
        stat['score'] += 50
        for enemy in hit_enemies:
            effect = ExplosionEffect(enemy.rect.centerx, enemy.rect.centery)
            effects_group.add(effect)
    if stat['bg_color'] != "000000":
        stat['count_frame'] += 1
    if stat['count_frame'] == 3:
        stat['bg_color'] = "000000"
        stat['count_frame'] = 0
