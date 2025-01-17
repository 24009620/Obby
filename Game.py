from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

map = Entity(model="Cube", scale=10, collider="mesh", color=hsv(120,.100,.50), y = 20)
map2= Entity(model="Cube", scale=5, collider="mesh", color=hsv(60,.100,.50), y = 21.5)

Ob1 = Entity(model="Sphere", Scale = 50, collider="mesh", color=hsv(200,.100,.10), y= 26)

Ob2 = Entity(model="sphere", scale = 1, collider="mesh", color=hsv(0, .10, .600), y = 27, x = 3)

Ob3 = Entity(model="sphere", scale = 1, collider="mesh", color=hsv(100, .10, .30), y = 28, x = 3, z =  3)

Ob4 = Entity(model="Cube", scale = 1, collider="mesh", color=hsv(0, .0, .10), y = 28.5, x = 5, z = 6)

player = FirstPersonController(y=1000)
player.speed = 5
player.jump_height = 2
player.gravity = 0.5


app.run()