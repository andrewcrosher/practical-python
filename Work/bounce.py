# bounce.py
#
# Exercise 1.5
height = 100
bounceRatio = 0.6
bounceN = 1

while bounceN < 11:
    height = height * bounceRatio
    print(bounceN, round(height,4))
    bounceN = bounceN + 1