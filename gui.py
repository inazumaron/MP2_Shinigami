import pyglet
import resources
from pyglet.window import *

#Variables
#===========================================
game_screen = 0
key_left_press = False
key_right_press = False
key_up_press = False
key_down_press = False
key_gun_press = False
key_melee_press = False
key_dash_press = False

Player_Bullets = []
Enemy_Bullets = []
Player_melee = []
Enemy_list = []

#Set up window
game_window = pyglet.window.Window(600,800)

#Setting Image layers
group_background = pyglet.graphics.OrderedGroup(0)
group_midground = pyglet.graphics.OrderedGroup(1)
group_foreground = pyglet.graphics.OrderedGroup(2)

#Start/Continue button
spr_btn_start = pyglet.sprite.Sprite(img=resources.button_start, x=300, y=200,group=group_foreground)

#set up background
game_background = pyglet.sprite.Sprite(img=resources.cover_image,x=300,y=400,group=group_background)

#game sprites
spr_player = pyglet.sprite.Sprite(img=resources.player_image,x=300,y=50,group=group_foreground)
spr_player_bullets = []
	
#Set cursor
cursor = pyglet.window.ImageMouseCursor(resources.cursor_1, 16, 8)
#game_window.set_mouse_cursor(cursor)

@game_window.event
def on_draw():
	global game_screen, spr_player_bullets, Player_Bullets
	game_window.clear()
	if game_screen == 0:
		game_background.draw()
		spr_btn_start.draw()
	elif game_screen == 2:
		spr_player.draw()
		spr_player_bullets = []
		for b in Player_Bullets:
			if b.modifiers["homing"] and b.modifiers["explosive"]:
				spr_player_bullets.append(pyglet.sprite.Sprite(img=resources.bullet_exhoming,x=b.obj_x,y=b.obj_y,group=group_midground))
			elif b.modifiers["homing"]:
				spr_player_bullets.append(pyglet.sprite.Sprite(img=resources.bullet_homing,x=b.obj_x,y=b.obj_y,group=group_midground))
			elif b.modifiers["explosive"]:
				spr_player_bullets.append(pyglet.sprite.Sprite(img=resources.bullet_explosive,x=b.obj_x,y=b.obj_y,group=group_midground))
			elif b.modifiers["piercing"]:
				spr_player_bullets.append(pyglet.sprite.Sprite(img=resources.bullet_piercing,x=b.obj_x,y=b.obj_y,group=group_midground))
			else:
				spr_player_bullets.append(pyglet.sprite.Sprite(img=resources.bullet_player,x=b.obj_x,y=b.obj_y,group=group_midground))
		for b in spr_player_bullets:
			b.draw()

@game_window.event
def on_mouse_press(x,y,button,modifiers):
	#==================================
	#Checking if mouse is over buttons
	#==================================
	global game_screen
	if game_screen == 0:
		if abs(x-spr_btn_start.x)<50 and abs(y-spr_btn_start.y)<40:
			#Go to home screen (thou this will actually lead to game screen, just change when home is available na)
			game_screen = 2
			#----------Fix this to 1 later-----------------#
			print(game_screen)

@game_window.event
def on_key_press(symbol, modifiers):
	global key_left_press,key_right_press,key_up_press,key_down_press,key_gun_press,key_melee_press,key_dash_press
	if symbol == key.W:
		key_up_press = True
	if symbol == key.A:
		key_left_press = True
	if symbol == key.S:
		key_down_press = True
	if symbol == key.D:
		key_right_press = True
	if symbol == key.R:
		key_gun_press = True
	if symbol == key.T:
		key_melee_press = True
	if symbol == key.Y:
		key_dash_press = True

@game_window.event
def on_key_release(symbol, modifiers):
	global key_left_press,key_right_press,key_up_press,key_down_press,key_gun_press,key_melee_press,key_dash_press
	if symbol == key.W:
		key_up_press = False
	if symbol == key.A:
		key_left_press = False
	if symbol == key.S:
		key_down_press = False
	if symbol == key.D:
		key_right_press = False
	if symbol == key.R:
		key_gun_press = False
	if symbol == key.T:
		key_melee_press = False
	if symbol == key.Y:
		key_dash_press = False


def on_run():
	pyglet.app.run()

def recieve_vars(game_screen_val):
	global game_screen
	game_screen = game_screen_val

def player_move(x,y):
	global spr_player
	spr_player.x = x
	spr_player.y = y

def update_bullet_list(p_bullet,e_bullet):
	global Player_Bullets, Enemy_Bullets
	Player_Bullets = p_bullet
	Enemy_Bullets = e_bullet

def keyboard(key): #When main checks if a certain key is being checked
	global key_left_press,key_right_press,key_up_press,key_down_press,key_gun_press,key_melee_press,key_dash_press
	if key == "up":
		return key_up_press
	if key == "down":
		return key_down_press
	if key == "left":
		return key_left_press
	if key == "right":
		return key_right_press
	if key == "gun":
		return key_gun_press
	if key == "melee":
		return key_melee_press
	if key == "dash":
		return key_dash_press

def get_player_coordinates():
	global spr_player
	return [spr_player.x, spr_player.y]