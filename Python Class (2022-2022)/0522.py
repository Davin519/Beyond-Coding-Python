# x = list(map(int, input().split()))
# n = int(input())

# x.remove(n)

# print(x)

# x = {"apple":100, "melon":200, "cherry":300}
# x["melon"] = 500
# x.pop("cherry")
# print(x)


# import turtle as t
# t.shape("turtle")
# t.color("white")
# t.bgcolor("skyblue")
# t.speed(20)
# t.begin_fill()
# t.circle(150)
# t.end_fill()
# t.right(180)
# t.color("white")
# t.speed(20)
# t.begin_fill()
# t.circle(200)
# t.end_fill()
# t.right(180)
# t.color("orange")
# t.begin_fill()
# t.circle(30)
# t.end_fill()
# t.penup()
# t.right(-90)
# t.forward(150)
# t.right(90)
# t.forward(100)
# t.left(90)
# t.pendown
# t.color("black")
# t.begin_fill()
# t.circle(30)
# t.end_fill()
# t.left(82.5)
# t.forward(150)
# t.color("black")
# t.begin_fill()
# t.circle(30)
# t.end_fill()

# t.exitonclick()

import turtle as t
import random

window = t.Screen()
p = t.Turtle()
p.shape("circle")
p.color("yellow")
window.bgcolor("black")

def go_right():
    print(p.pos())
    print(p.xcor())
    print(p.ycor())
    p.forward(100)
    print("go right")

def go_left():
    print(p.pos())
    print(p.xcor())
    print(p.ycor())
    p.forward(-100)
    print("go left")

def go_up():
    print(p.pos())
    print(p.xcor())
    print(p.ycor())
    p.sety(p.ycor() + 100)
    print("go right")

def go_down():
    print(p.pos())
    print(p.xcor())
    print(p.ycor())
    p.sety(p.ycor() - 100)
    print("go left")

def change_color():
    colors = ["red", "orange", "yellow", "green", "blue", "skyblue", "navy", "purple", "white"]
    p.color(random.choice(colors))


t.onkeypress(go_right, "d")
t.onkeypress(go_left, "a")
t.onkeypress(go_up, "w")
t.onkeypress(go_down, "s")
t.onkeypress(change_color, "c")
t.listen()

t.exitonclick()