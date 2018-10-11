#:kivy 1.0.9

< PongBall >:
size: 50, 50
canvas:
Ellipse:
pos: self.pos
size: self.size

< PongPaddle >:
size: 25, 200
canvas:
Rectangle:
pos: self.pos
size: self.size

< PongGame >:
ball: pong_ball
player1: player_left
player2: player_right

canvas:
Rectangle:
pos: self.center_x - 5, 0
size: 10, self.height

Label:
font_size: 70
center_x: root.width / 4
top: root.top - 50
text: str(root.player1.score)

Label:
font_size: 70
center_x: root.width * 3 / 4
top: root.top - 50
text: str(root.player2.score)

PongBall:
id: pong_ball
center: self.parent.center

PongPaddle:
id: player_left
x: root.x
center_y: root.center_y

PongPaddle:
id: player_right
x: root.width - self.width
center_y: root.center_y
