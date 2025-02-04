import pgzrun, random

WIDTH = 1200
HEIGHT = 600
enemy = Actor("enemy")
spacecraft = Actor("Spacecraft")
spacecraft.pos = (WIDTH/2,HEIGHT - 50)
SPEED = 5
bullets = []
enemies = []
for i in range(8):
    for j in range(4):
        enemeies.append(Actor("enemy"))
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


