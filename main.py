import gui as gui
import pyglet
import ship as ship
import bullet as bull

#=====================================
#Initializing variables for player input
#======================================
key_left_press = False
key_right_press = False
key_up_press = False
key_down_press = False
key_gun_press = False
key_melee_press = False
key_dash_press = False
#=====================================
#Initializing variables for ship stats
#=====================================
ship_life = 3
ship_shield = True
ship_gun = True
ship_melee = True
ship_dash = True
'''
        ship_shield/gun/melee/dash
            if true: can be used, else cant use
'''
#=====================================
#Initializing variables for shield
#=====================================
shield_life = 10
shield_regen = 1
shield_cooldown = 10
'''
        shiled_regen - rate of of shield recovery if not broken
        shield_cooldwon - rate before shield reactivate when broken
'''
#=====================================
#Initializing variables for gun
#=====================================
gun_cooldown = 0.1
gun_base_damage = 1
gun_homing = False
gun_piercing = False
gun_multiple = False
gun_laser = False
gun_explosive = False
gun_explosive_damage = gun_base_damage/2
#=====================================
#Initializing variables for melee
#=====================================
melee_cooldown = 1
melee_base_damage = 10
melee_reach = 1
melee_range = 180
melee_deflect = False
'''
        melee_reach - how far out the weapon reach
        melee_range - 180 (whole front of ship), 360 (all around the ship)
'''
#=====================================
#Initializing variables for dash
#=====================================
dash_cooldown = 1
dash_range = 5
dash_invulnerable = False
#=====================================
#Initializing variables for misc
#=====================================
score_leaderboard = dict()
##score_leaderboard = get_leaderboard()
##save_state = get_save()
game_screen = 0
'''
0 - Start screen
1 - Home screen
2 - game screen
3 - game over screen
'''
#======================================
#Object holders (lists that hold classes)
#======================================
Player_Bullets = []
Enemy_Bullets = []
Player_melee = []
Enemy_list = []

def player_movement():
	global key_left_press,key_right_press,key_up_press,key_down_press,key_gun_press,key_melee_press,key_dash_press
	temp = gui.get_player_coordinates()
	x = temp[0]
	y = temp[1]
	if key_left_press or key_right_press or key_up_press or key_down_press:
		temp = ship.ship_move(x,y,key_left_press,key_right_press,key_up_press,key_down_press)
		x = temp[0]
		y = temp[1]
		gui.player_move(x,y)
	if key_gun_press:
		temp = ship.ship_move(x,y,key_left_press,key_right_press,key_up_press,key_down_press)
		x = temp[0]
		y = temp[1]
		Player_Bullets.append(ship.ship_gun(x,y,False))

def move_bullets():
	global Player_Bullets, Enemy_Bullets
	for bullet in range(0,len(Player_Bullets)):
		Player_Bullets[bullet] = bull.bullet_action(Player_Bullets[bullet],Enemy_list)
	for bullet in range(0,len(Enemy_Bullets)):
		Enemy_Bullets[bullet] = bull.bullet_action(Enemy_Bullets[bullet],gui.get_player_coordinates())
	gui.update_bullet_list(Player_Bullets,Enemy_Bullets)

#==========================================================================================#
#									Input Check											   #
#==========================================================================================#

def check_input(dt):
	global key_left_press,key_right_press,key_up_press,key_down_press,key_gun_press,key_melee_press,key_dash_press
	key_left_press = gui.keyboard("left")
	key_right_press = gui.keyboard("right")
	key_up_press = gui.keyboard("up")
	key_down_press = gui.keyboard("down")
	key_melee_press = gui.keyboard("melee")
	key_dash_press = gui.keyboard("dash")
	key_gun_press = gui.keyboard("gun")
	#===============================checking other things
	player_movement()
	move_bullets()

pyglet.clock.schedule_interval(check_input,1/30)

#==========================================================================================#
#								GUI calling, variables and functions					   #

gui.on_run() 	

gui.recieve_vars(game_screen)