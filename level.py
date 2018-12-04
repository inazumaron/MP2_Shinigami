import pyglet
import enemy as enemy

def get_enemy(time,difficulty,enemy_list):
	#check level
	if difficulty == 1:		
		if time%150 == 0 or time == 10:	###Enemies come in after 1/3 of a second then reappears every 5 seconds
			enemy_list.append(enemy.Enemy_1(time)) 
			enemy_list.append(enemy.Enemy_3(time))
			enemy_list.append(enemy.Enemy_4(time))
			enemy_list.append(enemy.Enemy_5(time))

		if time >= 3600 and time % 300 == 0:		###Enemies come in after 2 minutes and reappears every 10 seconds
			enemy_list.append(enemy.Enemy_6())
			enemy_list.append(enemy.Enemy_7())	

		if time >= 5400 and time % 450 == 0:	###Enemies come in after 30 seconds and reappears every 15 seconds
			enemy_list.append(enemy.Enemy_8())			
			
		if time >= 7200 and time % 600 == 0:			###Enemies come in after 40 seconds and reappears every 20 seconds
			enemy_list.append(enemy.Enemy_9())
			enemy_list.append(enemy.Enemy_10())
		
	if difficulty == 2:
		if time%150 == 0 or time == 10:	###Enemies come in after 1/3 of a second then reappears every 5 seconds
			enemy_list.append(enemy.Enemy_1(time)) 
			enemy_list.append(enemy.Enemy_3(time))
			enemy_list.append(enemy.Enemy_4(time))
			enemy_list.append(enemy.Enemy_5(time))
			
		if time >= 30 and time % 210 == 0: ###Enemies come in after 1 second and reappears every 7 seconds
			enemy_list.append(enemy.Enemy_2(time))

		if time >= 315 and time % 300 == 0:		###Enemies come in after 10.5 secs and reappears every 10 seconds
			enemy_list.append(enemy.Enemy_6())
			enemy_list.append(enemy.Enemy_7())	

		if time >= 600 and time % 450 == 0:	###Enemies come in after 20 seconds and reappears every 15 seconds
			enemy_list.append(enemy.Enemy_8())			
			
		if time >= 900 and time % 600 == 0:			###Enemies come in after 30 seconds and reappears every 20 seconds
			enemy_list.append(enemy.Enemy_9())
			enemy_list.append(enemy.Enemy_10())

	return enemy_list
