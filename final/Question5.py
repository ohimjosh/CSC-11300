import math
#Question5
x1 = int(input("Point 1, Enter x: "))
y1 = int(input("Point 1, Enter y: "))

x2 = int(input("Point 2, Enter x: "))
y2 = int(input("Point 2, Enter y: "))

x3 = int(input("Point 3, Enter x: "))
y3 = int(input("Point 3, Enter y: "))

def righttriangle():
    s1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    s2 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
    s3 = math.sqrt((x3-x1)**2 + (y3-y1)**2)

    print(s1, s2, s3)
    a2 = s1**2
    b2 = s2**2
    c2 = s3**2

    if ((a2+b2) == c2 or (c2+b2) == a2 or(c2+a2) == b2):
        print("Points entered create a right triangle")
        return True
    else:
        print("Points entered do not create a right triangle")
        return False


print(righttriangle())

def equilateraltriangle():
    s1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    s2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    s3 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

    if (s1 == s2 == s3):
        print("Points entered create a equilateral triangle")
        return True
    else:
        print("Points entered do not create a equilateral triangle")
        return False

print(equilateraltriangle())