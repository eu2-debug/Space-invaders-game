import pgzrun, random

WIDTH = 1200
HEIGHT = 600
enemy = Actor("enemy")
spacecraft = Actor("spacecraft")
spacecraft.pos = (WIDTH/2,HEIGHT - 50)
SPEED = 5
bullets = []
enemies = []
for i in range(8):
    for j in range(4):
        enemies.append(Actor("enemy"))
        enemies[-1].x = 100 + 50 * x
        enemies[-1].y = 100 + 50 * y
score = 0
direction = 1
spacecraft.dead = False
spacecraft.countdown = 90

def display_score():
    screen.draw.text(str(score),(50,30))

def gameover():
    screen.draw.text("GAMEOVER",(250,300))

def on_key_down(key):
    if spacecraft.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor("bullet"))
            bullets[-1].x = spacecraft.x
            bullets [-1].y = spacecraft.y - 50

def update():
    global score, direction
    movedown = False

    if spacecraft.dead == False:
        if keyboard.left:
            spacecraft.x -= (SPEED)
            if spacecraft.x <= 0:
                spacecraft.x = 0
        elif keyboard.right:
            spacecraft.x +=(SPEED)
            if spacecraft.x >= (WIDTH):
               spacecraft.x = (WIDTH)

    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)

        else:
            bullet.y -=10


    if len(enemies) == 0:
        gameover()
    if len(enemies) > 0 and(enemies[-1].x > WIDTH - 50 or enemies[0].x < 50):
        movedown = True
        direction *= -1
    for enemy in enemies:
        enemy.x += 5*direction
        if movedown == True:
            enemy.y+=100
        if enemy.y > (HEIGHT):
            enemies.remove(enemy)

        for bullet in bullets:
            if enemy. colliderect(bullet):
                score += 10
                bullets.remove(bullet)
                enemies.remove(enemy)
                if len(enemeies) == 0:
                    gameover()

        if enemy.colliderect(spacecraft):
            spacecraft.dead = True
    if spacecraft.dead:
        spacecraft.countdown -=1

    if spacecraft.countdown == 0:
        spacecraft.dead = False
        spacecraft.countdown = 60



def draw():
    screen.clear()
    screen.fill("black")

    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()

    if spacecraft.dead == False:
        spacecraft.draw()
    display_score()
    if len(enemies) == 0:
        gameover()




pgzrun.go()





