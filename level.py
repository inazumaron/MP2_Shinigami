import pyglet
import enemy as enemy#

def get_enemy(time,difficulty,enemy_list):
	#check level
	if difficulty == 1:		#
		if (time%150 == 0 or time == 10) and time <= 9900:	###comes in after 1/3 of a second then reappears every 5 seconds
			enemy_list.append(enemy.Enemy_1(time))
			enemy_list.append(enemy.Enemy_5(time))
			
		if time == 1200 or time == 3000:	###comes in after 40 seconds and after 1 min 40 secs
			enemy_list.append(enemy.Enemy_8())
			enemy_list.append(enemy.Enemy_2(time))
			
		if time == 1800 or time == 3600:	###comes in after 60 seconds and after 2 mins
			enemy_list.append(enemy.Enemy_9())
			enemy_list.append(enemy.Enemy_10())
			
		if time == 2400 or time == 4500:	###comes in after 1 min 20 secs and after 2 mins 30  secs
			enemy_list.append(enemy.Enemy_3(time))
			enemy_list.append(enemy.Enemy_4(time))

		if time >= 9900 and time % 300 == 0:		###comes in after 5 mins and reappears every 10 seconds
			enemy_list.append(enemy.Enemy_6())
			enemy_list.append(enemy.Enemy_7())	

		if time >= 10800 and time % 450 == 0:	###comes in after 6 mins and reappears every 15 seconds
			enemy_list.append(enemy.Enemy_8())
			enemy_list.append(enemy.Enemy_2(time))
			
		if time >= 12600 and time % 600 == 0:			###comes in after 7 mins and reappears every 20 seconds
			enemy_list.append(enemy.Enemy_9())
			
		if time >= 14400 and time % 900 == 0:	###comes in after 8 mins and reappears every 30
			enemy_list.append(enemy.Enemy_10())
		
	if difficulty == 2:
		if time%150 == 0 or time == 10:	###comes in after 1/3 of a second then reappears every 5 seconds
			enemy_list.append(enemy.Enemy_1(time)) #
			enemy_list.append(enemy.Enemy_3(time))
			enemy_list.append(enemy.Enemy_4(time))
			enemy_list.append(enemy.Enemy_5(time))
			
		if time >= 30 and time % 210 == 0: ###comes in after 1 second and reappears every 7 seconds
			enemy_list.append(enemy.Enemy_2(time))

		if time >= 315 and time % 300 == 0:		###comes in after 10.5 secs and reappears every 10 seconds
			enemy_list.append(enemy.Enemy_6())
			enemy_list.append(enemy.Enemy_7())	

		if time >= 600 and time % 450 == 0:	###comes in after 20 seconds and reappears every 15 seconds
			enemy_list.append(enemy.Enemy_8())			
			
		if time >= 900 and time % 600 == 0:			###comes in after 30 seconds and reappears every 20 seconds
			enemy_list.append(enemy.Enemy_9())
			enemy_list.append(enemy.Enemy_10())

	return enemy_list
