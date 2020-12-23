import math
import os

#question 1
minutes = input("How many minutes do you want to convert to milliseconds ")
minutesnum = float(minutes)
milliseconds = minutesnum * 60000
print(milliseconds)

#question 2
a = 1
b = 2
c = 1

delta = (b**2) - (4*a*c)


x1 = (-b + math.sqrt(delta))/(2*a)

x2 = (-b - math.sqrt(delta))/(2*a)

print(x1)
print(x2)

#question3

midterm = input("What is your midterm grade? ")
d_midterm = float(midterm)
midterm_weight = float(40/100)
midterm1 = midterm_weight * d_midterm




final = input("What is your final grade? ")
d_final = float(final)
final_weight = float(60/100)
final1 = final_weight * d_final

finalgrade = (midterm1 + final1)/2

print(finalgrade)

#question 4
print(help(os))

#question 5

a = input("What is a ")
b = input("What is b ")
c = input("What is c ")

a_float = float(a)
b_float = float(b)
c_float = float(c)

s = (a_float + b_float + c_float) / 2

s1 = float(s)

area = math.sqrt(s1*(s1-a_float)*(s1-b_float)*(s1-c_float))

print(float(area))

#question 6

length_cube = input("What is length of cube ")
n = int(length_cube)
volume = math.pow(n,3)
cube = float(volume)

volume_sphere = 4/3 * math.pi * math.pow(n,3)

sphere = float(volume_sphere)

fit = sphere / cube

print(fit)















#question 7





