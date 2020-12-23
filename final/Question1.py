#Question1
import random
def probrandval():
    Start = 1
    Stop = 9
    n = int(input("Enter size of list: "))
    k = 0
    j= 0
    listsum = 0
    listsum2 = 0
    randomlist = random.sample(range(Start, Stop), n)
    randomlist2 = random.sample(range(Start, Stop), n)



    for i in range(len(randomlist)):
        listsum += randomlist[i]

    for i in range(len(randomlist)):
        randomlist[i] = randomlist[i] / listsum

    for i in range(len(randomlist)):
        k += randomlist[i]



    for i in range(len(randomlist2)):
        listsum2 += randomlist2[i]

    for i in range(len(randomlist2)):
        randomlist2[i] = randomlist2[i] / listsum2

    for i in range(len(randomlist2)):
        j += randomlist2[i]

    print(k)
    print(j)



print(probrandval())
