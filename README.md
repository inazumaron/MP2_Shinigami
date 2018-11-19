# MP2_Shinigami
A simple bullet hell game

Things to do:
=======Within framework already========
-better/smoother movement   (check at ship.py, ship_move)
-add dash (check at ship.py, ship_dash)
-add bullet cooldown (check at ship.py, ship_gun)

-add homing feature to bullet (check bullet.py, bullet_action)
-destroy bullet if in contact (check bullet.pu, add to bullet_action)
      -set self.destroy = True to destroy
      -for piercing=true, destroy only if outside screen

-add more enemies (check enemy.py, make more classes)
      - give simple ai, on their movement pattern when called
      -at main, still cant be called yet
      
-level algorithm (cant be done w/o more enemies)
      -spawns more enemies as level progresses
      -(still havent done much yet regarding this)
      
-add home page for gui (at gui.py, @game_window.event, def on_draw...)
      -add a setting if game_screen == 1: it will draw a home screen
      -should include a play button, continue button, and leaderboard
          -(add a xml file with names and scores to be read)
          -the buttons may not have graphics, im just gonna supply that, unless you take initiative
          
-Add virtual enviroment (idk how yet)          
