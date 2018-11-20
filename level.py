import pyglet
import enemy as enemy#

def get_enemy(time,difficulty,enemy_list):
	#check level
	if difficulty == 1:		#
		if time%100 == 0:	#every 3 seconds
			enemy_list.append(enemy.Enemy_1()) #
	return enemy_list
