# x = list(map(int, input().split()))
# x.sort()
# print(x)

# a = ['a', 'b', 'c', 'd']
# print(a[:3])

# print(f"{{name}} is age {{age}} years old")

import random

user_choice = int(input("input your choice : "))
choices = ["rock", "scissor", "paper"]
ai_choice = random.choice(choices)

if user_choice == 0 and choices.index(ai_choice) == 1:
    print("user won")
elif user_choice == 1 and choices.index(ai_choice) == 2:
    print("user won")
elif user_choice == 2 and choices.index(ai_choice) == 0:
    print("user won")
elif user_choice == 0 and choices.index(ai_choice) == 2:
    print("AI won")
elif user_choice == 1 and choices.index(ai_choice) == 0:
    print("AI won")
elif user_choice == 2 and choices.index(ai_choice) == 0:
    print("AI won")
else:
    print("tie")


