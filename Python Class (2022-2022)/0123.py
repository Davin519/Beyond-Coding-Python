# x = 10
# if x > 5:
#      print("x is greater than 5")
# elif x < 5:
#     print('x is less than 5')
# else:
#     print('x is equal to 5')
x = int(input())
y = int(input())
z = int(input())

if (x > y) and (x > z):
   largest = x
elif (y > x) and (y > z):
   largest = y
else:
   largest = z
 
print("The largest number is",largest)
