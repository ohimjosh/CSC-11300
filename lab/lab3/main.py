# Josh Miranda Lab 3
import random

'''
#Question 1
def comparetxt(somefile):
    list=[]
    with open(somefile, "r", encoding='utf-8') as myfile:
        data=myfile.read().splitlines()
        list.append(data)
    new=[]
    for i in range(len(list)):
        new = new + list[i]
    return new

def main():
    a = comparetxt('a.txt')
    b = comparetxt('b.txt')

    for i in a:
        for j in b:
            if (i == j):
                a1 = a.index(i) + 1
                b1 = b.index(j) + 1

    print("Line", a1, "in a.txt matches with", b1, "in b.txt")

print(main())


'''


'''
#Question 2

def randomxy():
    letters = ["X", "Y"]

    with open("quotes.txt", "w", encoding='utf-8') as file:
        for i in range(1000):
            file.write(random.choice(letters) + "\n")


def show():
    XX = YY = 0
    with open("quotes.txt", "r", encoding='utf-8') as somefile:

        for line in somefile:
            line = line.replace("\n", "")
            if (line[-2:] == "XX"):
                XX += 1
            elif (line[-2:] == "YY"):
                YY += 1

        print("Lines ending with XX: ", XX)
        print("Lines ending with YY: ", YY)

        ratio = (XX + YY) / 1000
        print("Ratio: ", ratio)

print(randomxy())
print(show())


'''
#Question 3
I = [1,2.09,3,4,5,6,'a',8,9,10.14,11,'b']
J = {1,2,7}


def twod():
    twod = np.array(I).reshape(-1,2)
    print(twod)

twod()