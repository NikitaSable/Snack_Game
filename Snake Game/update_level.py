from turtle import Turtle
from scoreboard import ScoreBoard

score = ScoreBoard()
block1_position = [(-180, 80), (-180, 100), (-180, 120), (-180, 140), (-180, 160), (-180, 180), (-180, 200)]
block2_position = [(180, -80), (180, -100), (180, -120), (180, -140), (180, -160), (180, -180), (180, -200)]
block3_position = [(-60, -80), (-80, -80), (-100, -80), (-120, -80), (-140,-80), (-160, -80), (-180,-80)]
block4_position = [(60, 80), (80, 80), (100, 80), (120, 80), (140,80), (160, 80), (180,80)]

class UpdateLevel(ScoreBoard):

    def __init__(self):
        super().__init__()
        # self.segment = []
        # self.create_snake()
        # self.move()
        # self.head = self.segment[0]

    def leve1(self):
        for i in block1_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i)

    def leve2(self):
        for i in block2_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i)

    def leve3(self):
        for i in block3_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i)

    def leve4(self):
        for i in block4_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i)

