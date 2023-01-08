# import turtle as t

# t.shape("turtle")
# t.color("green")
# for i in range(80):
#     t.forward(10)
#     t.left(360/80)


# t.exitonclick()

# import turtle as t

# t.shape("turtle")
# t.color("green")

# for i in range(50, 499, 50):
#    for j in range(2, 4, 1):
#        t.forward(i)
#        t.right(90)
# t.forward(450)
# t.exitonclick()

# import turtle as t

# t.shape("turtle")
# t.color("green")

# for i in range(5):
#     t.forward(200)
#     t.right(144)

# t.exitonclick()

import turtle as t
import random

t.shape("turtle")
t.width(5)
t.speed(25)
t.hideturtle()
t.color("green")

x = ["red", "orange", "yellow", "green", "blue"]

for j in range(1000000000000):
    t.color(random.choice(x))
    t.left(random.randrange(1, 361))
    t.forward(100)

t.exitonclick
