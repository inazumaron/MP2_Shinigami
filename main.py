import gui as gui
import pyglet
import ship as ship
import bullet as bull
import level as level
import collision as col
import random as r
import score as sc

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
ship_speed = 7
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
gun_base_damage = 10
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
melee_base_damage = 50
melee_reach = 1
melee_range = 270
melee_deflect = False
melee_midswing = False
melee_angle = 0 #rotation of sprite
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
dash_distance = 100
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
bullet_d_mod = 1
bullet_s_mod = 1
enemy_l_mod = 1
options = []
buff_list = ["axe","bullet_d","bullet_s","dash_c","dash_d","enemy_l","explosive","homing","life","piercing","shield_c","shield_l","shield_r","spear","speed","sword"]

def player_movement():
	global ship_speed,dash_distance,melee_midswing,ship_melee,ship_shield,ship_dash,dash_now,sword_now,key_left_press,key_right_press,key_up_press,key_down_press,key_gun_press,key_melee_press,key_dash_press,gun_in_cooldown,gun_cooldown,Player_Bullets,dash_time,dash_first_use
	temp = gui.get_player_coordinates()
	x = temp[0]
	y = temp[1]
	if key_left_press or key_right_press or key_up_press or key_down_press:
		temp = ship.ship_move(x,y,key_left_press,key_right_press,key_up_press,key_down_press,ship_speed)
		x = temp[0]
		y = temp[1]
		gui.player_move(x,y)
	if time_elapse % gun_cooldown == 0: 			### Rate of fire as of now
		gun_in_cooldown = True
	if key_gun_press:
		if gun_in_cooldown:
			gun_in_cooldown = False
			Player_Bullets.append(ship.ship_gun(x,y,gun_explosive,gun_homing,gun_piercing,gun_base_damage))

	if key_dash_press:
		dash_now = time_elapse
		if ship_dash:
			temp = ship.ship_dash(x,y,key_left_press,key_right_press,key_up_press,key_down_press, 0,dash_distance)
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
			melee_midswing = True
			ship_melee = False
	if time_elapse-sword_now >= melee_cooldown:
		ship_melee = True
	gui.update_ship_stat(ship_shield,ship_dash,ship_melee)

def move_bullets():
	global Player_Bullets, Enemy_Bullets, Explosion_list, bullet_d_mod, bullet_s_mod
	destroy_bullet = []
	for bullet in range(0,len(Player_Bullets)):
		Player_Bullets[bullet] = bull.bullet_action(Player_Bullets[bullet],Enemy_list,0)
		Player_Bullets[bullet].dam_mod = bullet_d_mod
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
		Enemy_Bullets[bullet].sp_mod = bullet_s_mod
		if Enemy_Bullets[bullet].destroy:
			destroy_bullet.append(Enemy_Bullets[bullet])
	for bullet in destroy_bullet:
		Enemy_Bullets.remove(bullet)

	for exp in Explosion_list:
		bull.explosion_action(exp,Enemy_list)
	gui.update_bullet_list(Player_Bullets,Enemy_Bullets,Explosion_list)

def move_enemies():
	global Enemy_list, Enemy_Bullets, time_elapse,Player_Bullets, Explosion_list, score
	temp = gui.get_player_coordinates()
	plr_point = {"x":temp[0],"y":temp[1]}
	dead_enemy = []
	for enemy in Enemy_list:
		enemy = enemy.move()
		if enemy.life <= 0:
			dead_enemy.append(enemy)
			score += enemy.points
	for enemy in Enemy_list:
		if enemy.y < -50:
			dead_enemy.append(enemy)				
	for enemy in dead_enemy:
		Enemy_list.remove(enemy)

	for enemy in Enemy_list:
		temp_bullet = enemy.shoot(time_elapse, plr_point)
		if temp_bullet != None:
			Enemy_Bullets.append(temp_bullet)

	gui.update_bullet_list(Player_Bullets,Enemy_Bullets, Explosion_list)
	gui.update_enemy_list(Enemy_list)

def upgrade():
	global time_elapse, plr_level, pause,buff_list, options, score
	if score > (plr_level**2)*(50)+100:
		pause = True
		plr_level += 1
		options = []
		for i in range(3):
			ran = r.SystemRandom()
			x = ran.randint(0,len(buff_list)-1)
			options.append(buff_list[x])
		gui.get_options(options)
		gui.paused(True)
	if pause:
		x = gui.check_option()
		if x != 0:
			pause = False
			print(options[x-1])
			level_up(options[x-1])
			gui.reset_option()

def level_up(buff):
	global bullet_d_mod,bullet_s_mod,enemy_l_mod,buff_list, melee_base_damage, dash_cooldown, dash_distance, gun_explosive, gun_homing, ship_life, gun_piercing, shield_max_life,shield_cooldown, shield_regen, melee_range, melee_cooldown, ship_speed
	if buff == "axe":
		melee_base_damage += 50
	elif buff == "bullet_d":
		bullet_d_mod *= 2
	elif buff == "bullet_s":
		bullet_s_mod /= 1.5
	elif buff == "dash_c":
		dash_cooldown == dash_cooldown//1.5
	elif buff == "dash_d":
		dash_distance *= 1.5
	elif buff == "enemy_l":
		enemy_l_mod *= 0.8
	elif buff == "explosive":
		gun_explosive = True
		buff_list.remove("explosive")
		if "piercing" in buff_list:
			buff_list.remove("piercing")
	elif buff == "homing":
		gun_homing = True
		buff_list.remove("homing")
		if "piercing" in buff_list:
			buff_list.remove("piercing")
	elif buff == "life":
		ship_life += 2
	elif buff == "piercing":
		gun_piercing = True
		buff_list.remove("piercing")
		if "homing" in buff_list:
			buff_list.remove("homing")
		if "explosive" in buff_list:
			buff_list.remove("explosive")
	elif buff == "shield_c":
		shield_cooldown /= 2
	elif buff == "shield_l":
		shield_max_life += 20
	elif buff == "shield_r":
		shield_regen *= 1.5
	elif buff == "spear":
		melee_range *= 2
	elif buff == "speed":
		ship_speed *= 1.5
	elif buff == "sword":
		melee_cooldown /= 2
def melee_handler():
	global melee_midswing, melee_reach, melee_range, melee_base_damage, melee_angle, Enemy_list
	if melee_midswing:
		temp = gui.get_player_coordinates()
		x = temp[0]
		y = temp[1]
		if melee_angle < melee_range:
			melee_angle += melee_range/15
		else:
			melee_midswing = False
			melee_angle = 0
		gui.update_sword(x, y, melee_angle, melee_reach)
		bull.melee_action(melee_base_damage, melee_reach, Enemy_list, x, y, melee_angle)

def bullet_collision():
	global score,time_elapse,Enemy_Bullets, shield_life, ship_life, shield_cooldown, shield_broke, shield_regen
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
	gui.update_life(shield_life, ship_life)
	if ship_life <= 0:
		gui.game_over(score,time_elapse)
<<<<<<< HEAD
		sc.add_score(time_elapse,score)
=======
		sc.add_score(score)
>>>>>>> 0ea248cd2325bd22d4840455da76482aa8b79f64

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
			melee_handler()

pyglet.clock.schedule_interval(check_input,1/30)

#==========================================================================================#
#								GUI calling, variables and functions					   #

gui.on_run() 	

gui.recieve_vars(game_screen)
