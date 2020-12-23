import random


# Question6

def matrixrule():
    rowA = random.randint(1, 10)
    colA = random.randint(1, 10)
    matrixA = []
    matrixB = []

    rowB = random.randint(1, 10)
    colB = random.randint(1, 10)

    matrixA.append(rowA)
    matrixA.append(colA)

    matrixB.append(rowB)
    matrixB.append(colB)

    print("Matrix A dimensions:", matrixA)
    print("Matrix B dimensions:", matrixB)

    completematrixA = [[random.randrange(1, 10) for x in range(colA)] for y in range(rowA)]
    completematrixB = [[random.randrange(1, 10) for x in range(colB)] for y in range(rowB)]
    print(completematrixA)
    print(completematrixB)

    if colA == rowB:
        print("We can multiply the two lists as matrices")
    else:
        print("We cannot multiply the two lists as matrices")


print(matrixrule())