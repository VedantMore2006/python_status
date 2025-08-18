import math


def canno(width, height):
    can = (width * height) / 5
    print(can)
    can = math.ceil((width * height) / 5)
    print(can)


w = int(input("Width "))
h = int(input("height "))
print(f"no of cans = {canno(w, h)}")
