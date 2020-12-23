#Question 7
class EmptySet(Exception):
    def __init__(self,string):
        print(string)


def cartesian():
    first = input("Enter first set: ")
    second = input("Enter second set: ")

    productset = [str(i)+str(j) for i in first for j in second]

    if (len(first) == 0):
        raise Exception('First set is empty, terminating program...')
        sys.exit()
    elif (len(second) == 0):
        raise Exception('Second set is empty, terminating program...')
        sys.exit()


    print(productset)

print(cartesian())