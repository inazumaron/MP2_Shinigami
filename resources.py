import pyglet


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
pyglet.resource.path = ['resc']
pyglet.resource.reindex()

# Load the three main resources and get them to draw centered
cover_image = pyglet.resource.image("cover_1.jpg")
center_image(cover_image)

button_start = pyglet.resource.image("start.png")
center_image(button_start)

button_continue = pyglet.resource.image("continue.png")
center_image(button_continue)

cursor_1 = pyglet.resource.image("cursor.png")
center_image(cursor_1)

player_image = pyglet.resource.image("player_small.png")
center_image(player_image)

bullet_enemy = pyglet.resource.image("bullet_e.png")
center_image(bullet_enemy)
bullet_player = pyglet.resource.image("bullet_p.png")
center_image(bullet_player)
bullet_homing = pyglet.resource.image("bullet_h.png")
center_image(bullet_homing)
bullet_explosive = pyglet.resource.image("bullet_x.png")
center_image(bullet_explosive)
bullet_piercing = pyglet.resource.image("bullet_i.png")
center_image(bullet_piercing)
bullet_exhoming = pyglet.resource.image("bullet_he.png")
center_image(bullet_exhoming)

enemy_1_image = pyglet.resource.image("enemy_small.png")
center_image(enemy_1_image)

bg_image = pyglet.resource.image("bg_1.png")
center_image(bg_image)

dot_red = pyglet.resource.image("red_dot.png")
center_image(dot_red)
dot_blue = pyglet.resource.image("blue_dot.png")
center_image(dot_blue)