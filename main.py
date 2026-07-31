import pgzrun
import pygame

from pgzClasses import *
condition = False
class platform:
   def __init__(self, x ,y ):
       self.image = Actor("platform.png")
       self.image.x = x
       self.image.y = y


def spawner(x, y):
    spawned = platform(x, y)
    return spawned

class Plt:
    def __init__(self):
            self.plat = spawner(200,200)
            self.plat2 = spawner(432,200)
            self.plat3 = spawner(75, 200)
            self.plat4 = spawner(50, 200)
            self.plat5 = spawner(10, 200)
            self.plat6 = spawner(500, 200)
            self.plat7 = spawner(489, 200)
            self.plat8 = spawner(250, 200)
            self.espeed = 5
            self.timer = 0
            self.button = True
    def myUpdate(self, player):
        global condition

        self.plat.image.y += self.espeed
        self.plat2.image.y += self.espeed
        self.plat3.image.y += self.espeed
        self.plat4.image.y += self.espeed
        self.plat5.image.y += self.espeed
        self.plat6.image.y += self.espeed
        self.plat7.image.y += self.espeed
        self.plat8.image.y += self.espeed
        if self.plat.image.y > HEIGHT:
            self.plat.image.y = 0
        if self.plat2.image.y > HEIGHT:
            self.plat2.image.y = 0
        if self.plat3.image.y > HEIGHT:
            self.plat3.image.y = 0
        if self.plat4.image.y > HEIGHT:
             self.plat4.image.y = 0
        if self.plat5.image.y > HEIGHT:
            self.plat5.image.y = 0
        if self.plat6.image.y > HEIGHT:
            self.plat6.image.y = 0
        if self.plat7.image.y > HEIGHT:
            self.plat7.image.y = 0
        if self.plat8.image.y > HEIGHT:
            self.plat8.image.y = 0
        if player.colliderect(self.plat.image):
            condition = True
            self.button = False
        if player.colliderect(self.plat2.image):
            condition = True
            self.button = False
        if player.colliderect(self.plat3.image):
            condition = True
            self.button = False
        if player.colliderect(self.plat4.image):
            condition = True
            self.button = False
        if player.colliderect(self.plat5.image):
            condition = True
            self.button = False
        if player.colliderect(self.plat6.image):
            condition = True
            self.button = False
        if player.colliderect(self.plat7.image):
            condition = True
            self.button = False
        if player.colliderect(self.plat8.image):
            condition = True
            self.button = False
    def draw(self):
        self.plat.image.draw()
        self.plat2.image.draw()
        self.plat3.image.draw()
        self.plat4.image.draw()
        self.plat5.image.draw()
        self.plat6.image.draw()
        self.plat7.image.draw()
        self.plat8.image.draw()


plt = Plt()
plt2 = Plt()
plt3 = Plt()
player = Actor("player.png")
ICON = "images/icon.png"
background = "bg.png"
win  = "object.png"
winAct = Actor("object.png")
WIDTH = 800
HEIGHT = 600
player.x = 400
player.y = 565
player.speed = 5
player.width = 128
player.height = 128
winAct.x = 200
winAct.y = 570
winAct.width = 32
winAct.height = 32
GRAVITY = 0.5
JUMP_STRENGTH = -12
timer = 0
button_rect = Rect((125, 120), (150, 50))
button_rect1 = Rect((300, 120), (150, 50))
button_color = (0, 128, 255)  # Default Blue
TITLE = "Dodge The duck!"
TITLE_SIZE = 50
is_fullscreen = False

def toggle_fs():
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    flags = pygame.FULLSCREEN if is_fullscreen else 0
    screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), flags)
def player_movement():
    if player.x >= WIDTH - player.width/2:
        player.x = WIDTH - player.width / 2

    elif keyboard.right or keyboard.d:
        player.x = player.x + player.speed
    elif keyboard.left or keyboard.a:
        player.x = player.x - player.speed
        if player.x <= player.width/2:
            player.x = player.width/ 2
    if keyboard.F: toggle_fs()
def draw_sprites():
    screen.blit(background, (0,0))
    player.draw()
def update():
    global timer
    player_movement()
    plt.myUpdate(player)
    plt2.myUpdate(player)
    plt3.myUpdate(player)

    if keyboard.ESCAPE:
        exit()

def draw():
    screen.fill("chocolate1")
    draw_sprites()
    plt.draw()
    plt2.draw()
    plt3.draw()
    global win
    screen.blit(win, (200, 570))
    if condition:
        screen.fill("Orange")
        screen.draw.text("You died, Would you like to continue? ", (200, 100))
        screen.draw.filled_rect(button_rect, button_color)
        screen.draw.filled_rect(button_rect1, button_color)
        screen.draw.text(
            "Yes",
            center=button_rect.center,
            color="white",
            fontsize=30
        )
        screen.draw.text(
            "No",
            center=button_rect1.center,
            color="white",
            fontsize=30
        )
    if player.colliderect(winAct):
        screen.fill("Orange")
        screen.draw.text("YOU WIN!", (200, 100), fontsize=30, color="white")


def on_mouse_down(pos, button):
    global condition
    global button_color
    if button == mouse.LEFT:
        if button_rect.collidepoint(pos):
            condition = False
        if button_rect1.collidepoint(pos):
            exit()


def on_mouse_up(pos, button):
    global button_color
    if button == mouse.LEFT:
        button_color = (0, 128, 255)
pgzrun.go()