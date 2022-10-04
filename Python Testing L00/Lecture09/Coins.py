import pgzrun
from random import randint
width=800
height=600
fox=Actor('fox')
fox.pos=100,100
coin=Actor('coin')
coin.pos=200,200
score=0
game_over=False
def draw():
    screen.fill('green')
    fox.draw()
    coin.drwa()
    screen.draw.text('Score : '+str(score),color='white',topleft=(10,10))
    if game_over:
        screen.draw.text(message,topleft(10,10),fontsize=50)
def place_coin():
    coin.x=randint(20,(width-20))
    coin.y=randint(20,(height-20))
def update():
    global score
    if keyboard.left:
        fox.x=fox.x-2
    elif keyboard.right:
        fox.x=fox.x+2
    elif keyborad.up:
        fox.y=fox.y-2
    elif keyborad.down:
        ox.y=fox.y+2
    coin_collected=fox.colliderect(coin)
    if coin_collected:
        place_coin()
def time_up():
    global gamer_over
    gamer_over=True

    
clock.schedule(time_up,10.0)
place_coin()
pgzrun.go()