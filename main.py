import gui as gui
import pyglet
import ship as ship
import bullet as bull
import level as level
import collision as col
import random as r

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
shield_life = 50
shield_regen = .1
shield_cooldown = 90
shield_broke = 0
shield_max_life = 50
'''
        shiled_regen - rate of of shield recovery if not broken
        shield_cooldwon - rate before shield reactivate when broken
'''
#=====================================
#Initializing variables for gun
#=====================================
gun_cooldown = 10
gun_in_cooldown = True #check if can fire
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
melee_cooldown = 60
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
dash_cooldown = 150		###5 secs
dash_range = 5
dash_invulnerable = False
dash_time = 0
dash_first_use = True
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
Explosion_list = []
#======================================
#Game stats (When in game/changable via options)
#======================================
time_elapse = 0
difficulty = 1
score = 0
pause = False
plr_level = 1
dash_now = 0
sword_now = 0
#======================================
options = []
buff_list = ["axe","dash_c","dash_d","explosive","homing","life","piercing","shield_l","shield_r","spear","speed","sword"]

def player_movement():
	global ship_melee,ship_shield,ship_dash,dash_now,sword_now,key_left_press,key_right_press,key_up_press,key_down_press,key_gun_press,key_melee_press,key_dash_press,gun_in_cooldown,gun_cooldown,Player_Bullets,dash_time,dash_first_use
	temp = gui.get_player_coordinates()
	x = temp[0]
	y = temp[1]
	if key_left_press or key_right_press or key_up_press or key_down_press:
		temp = ship.ship_move(x,y,key_left_press,key_right_press,key_up_press,key_down_press)
		x = temp[0]
		y = temp[1]
		gui.player_move(x,y)
	if time_elapse % gun_cooldown == 0: 			### Rate of fire as of now
		gun_in_cooldown = True
	if key_gun_press:
		if gun_in_cooldown:
			gun_in_cooldown = False
			Player_Bullets.append(ship.ship_gun(x,y,False))

	if key_dash_press:
		dash_now = time_elapse
		if ship_dash:
			temp = ship.ship_dash(x,y,key_left_press,key_right_press,key_up_press,key_down_press, 0)
			x = temp[0]
			y = temp[1]
			gui.player_move(x,y)
			dash_first_use = False
			ship_dash = False
	if time_elapse-dash_now >= dash_cooldown or dash_first_use:
		ship_dash = True

	if key_melee_press:
		sword_now = time_elapse
		if ship_melee:
			#do something
			ship_melee = False
	if time_elapse-sword_now >= melee_cooldown:
		ship_melee = True
	gui.update_ship_stat(ship_shield,ship_dash,ship_melee)

def move_bullets():
	global Player_Bullets, Enemy_Bullets, Explosion_list
	destroy_bullet = []
	for bullet in range(0,len(Player_Bullets)):
		Player_Bullets[bullet] = bull.bullet_action(Player_Bullets[bullet],Enemy_list,0)
		if Player_Bullets[bullet].destroy:
			destroy_bullet.append(Player_Bullets[bullet])
	for bullet in destroy_bullet:
		if bullet.modifiers["explosive"]:
			temp_exp = bull.explosion()
			temp_exp.x = bullet.obj_x
			temp_exp.y = bullet.obj_y
			Explosion_list.append(temp_exp)
		Player_Bullets.remove(bullet)
	destroy_bullet = []
	for bullet in range(0,len(Enemy_Bullets)):
		Enemy_Bullets[bullet] = bull.bullet_action_no_collision(Enemy_Bullets[bullet])
		if Enemy_Bullets[bullet].destroy:
			destroy_bullet.append(Enemy_Bullets[bullet])
	for bullet in destroy_bullet:
		Enemy_Bullets.remove(bullet)

	for exp in Explosion_list:
		bull.explosion_action(exp,Enemy_list)
	gui.update_bullet_list(Player_Bullets,Enemy_Bullets,Explosion_list)

def move_enemies():
	global Enemy_list, Enemy_Bullets, time_elapse,Player_Bullets, Explosion_list
	temp = gui.get_player_coordinates()
	plr_point = {"x":temp[0],"y":temp[1]}
	dead_enemy = []
	for enemy in Enemy_list:
		enemy = enemy.move()
		if enemy.life <= 0:
			dead_enemy.append(enemy)
	for enemy in Enemy_list:
		if enemy.y < -50:
			dead_enemy.append(enemy)				
	for enemy in dead_enemy:
		Enemy_list.remove(enemy)

	for enemy in Enemy_list:
		temp_bullet = enemy.shoot(time_elapse, plr_point)
		if temp_bullet != None:
			Enemy_Bullets.append(temp_bullet)
			gui.change_dot(False)

	gui.update_bullet_list(Player_Bullets,Enemy_Bullets, Explosion_list)
	gui.update_enemy_list(Enemy_list)

def upgrade():
	global time_elapse, plr_level, pause,buff_list, options
	if time_elapse//100 == plr_level:
		pause = True
		plr_level += 1
		options = []
		for i in range(3):
			ran = r.SystemRandom()
			x = ran.randint(0,len(buff_list)-1)
			options.append(buff_list[x])
			buff_list.remove(options[-1])
		gui.get_options(options)
		gui.paused(True)
	if pause:
		x = gui.check_option()
		if x != 0:
			pause = False
			print(options[x-1])
			gui.reset_option()


def bullet_collision():
	global Enemy_Bullets, shield_life, ship_life, shield_cooldown, shield_broke, shield_regen
	temp = gui.get_player_coordinates()
	x = temp[0]
	y = temp[1]
	if shield_life < shield_max_life and shield_broke <= 0:
		shield_life += shield_regen
	if shield_broke >0:
		shield_broke -= 1
	for b in Enemy_Bullets:
		if col.get_distance(x,y,b.obj_x,b.obj_y) < 40:
			if shield_life > 0:
				shield_life -= b.damage
				if shield_life <= 0:
					shield_broke = shield_cooldown
			else:
				ship_life -= 1
				print(ship_life)
			b.destroy = True

#==========================================================================================#
#									Input Check											   #
#==========================================================================================#

def check_input(dt):
	global pause,Enemy_list,time_elapse,key_left_press,key_right_press,key_up_press,key_down_press,key_gun_press,key_melee_press,key_dash_press
	key_left_press = gui.keyboard("left")
	key_right_press = gui.keyboard("right")
	key_up_press = gui.keyboard("up")
	key_down_press = gui.keyboard("down")
	key_melee_press = gui.keyboard("melee")
	key_dash_press = gui.keyboard("dash")
	key_gun_press = gui.keyboard("gun")
	#===============================updating time related variables
	if gui.game_start():
		if pause == False:
			time_elapse += 1
		else:
			time_elapse += 0
	else:
		time_elapse = 0
	#===============================checking other things
	if gui.game_start():
		upgrade()
		if pause == False:
			player_movement()
			move_bullets()
			move_enemies()
			Enemy_list = level.get_enemy(time_elapse,1,Enemy_list)
			bullet_collision()

pyglet.clock.schedule_interval(check_input,1/30)

#==========================================================================================#
#								GUI calling, variables and functions					   #

gui.on_run() 	

gui.recieve_vars(game_screen)
