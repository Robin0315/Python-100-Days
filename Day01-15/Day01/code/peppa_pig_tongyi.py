from turtle import *

# 设置一些常量，以提高代码的可读性和可维护性
STARTING_ANGLE = -30
STEP_ANGLE = 3
NOSE_RADIUS = 5
EYE_DISTANCE = 20
EYE_RADIUS = 5
NOSE_COLOR = (255, 155, 192)
EYE_COLOR = (160, 82, 45)

def move_to(x, y):
    """将海龟移动到指定的坐标"""
    penup()
    goto(x, y)
    pendown()

def draw_nose(x, y):
    """画鼻子"""
    global a
    penup()
    goto(x, y)
    pendown()
    setheading(STARTING_ANGLE)
    begin_fill()

    a = 0.4
    for _ in range(120):
        if 0 <= _ < 30 or 60 <= _ < 90:
            a += 0.08
        else:
            a -= 0.08
        
        left(STEP_ANGLE)
        forward(a)

    end_fill()
    penup()
    setheading(90)
    forward(EYE_DISTANCE // 2)  # 使用整除保证距离是整数，避免小数点精度问题
    setheading(0)
    draw_eyes()

def draw_eyes():
    """画眼睛"""
    for _ in range(2):
        penup()
        setheading(10)
        forward(EYE_RADIUS)
        pendown()
        pencolor(NOSE_COLOR)
        begin_fill()
        circle(EYE_RADIUS)
        color(EYE_COLOR)
        end_fill()
        penup()
        setheading(0)
        forward(EYE_DISTANCE)
        pendown()

# 初始化海龟和屏幕
t = Turtle()
screen = Screen()

# 绘制鼻子和眼睛
draw_nose(0, 0)

# 结束
screen.exitonclick()
