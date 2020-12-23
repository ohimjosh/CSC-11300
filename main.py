import math
import os

'''
#question 1
def divosorsum(num):

    result = 1
    for i in range(2, (num)):

        if (num % i == 0):
            result = result + i
    return (result)


def test():
    while True:
        try:
            num = int(input("Enter value: "))
        except Exception as e:
            print("Invalid input")
        else:
            if (divosorsum(num) == num):
                print(num, "is perfect number.")
                if input("Do you have more numbers to input? (yes or no) ") != 'yes':
                    break
            else:
                print(num, "is not perfect number.")



test()
'''
'''
def isperfect(num):
    if(num<0):
        raise Exception("")
    if(divSum(num) == num):
        print(num,'is perfect number')
    else:
        print(num,'is not a perfect number')

#Testing


def main():
    num = int(input("Enter value for n: "))
    while(True):
        try:
            isperfect(num)
            break
        except Exception as ex:
            print("Invalid input")
            num = int(input("Enter value for n: "))

main()

'''




'''
#question 2
def isprime():
    start = int(input('Enter start number: '))
    end = int(input('Enter end number: '))

    f = open("primes.txt", "w")
    f.close()

    for i in range(start, end):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                print(i)
                with open("primes.txt", "a") as f:
                    f.write(str(i))
                f.close()

print(isprime())
'''

'''
#question 3

done = False
while not done:
    try:

        print('Please enter 3 points to create a triangle')
        print('Enter point 1')
        x1 = int(input('x coordinate: '))
        y1 = int(input('y coordinate: '))

        print('Enter point 2')
        x2 = int(input('x coordinate: '))
        y2 = int(input('y coordinate: '))

        print('Enter point 3')
        x3 = int(input('x coordinate: '))
        y3 = int(input('y coordinate: '))


        a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        b = math.sqrt((x3-x2)**2 + (y3-y2)**2)
        c = math.sqrt((x3-x1)**2 + (y3-y1)**2)

        if a+b > c and b+c > a and c+a > b:
            print('({},{}), ({},{}) and ({},{}) form a triangle'.format(x1, y1, x2, y2, x3, y3))
        else:
            print('({},{}), ({},{}) and ({},{}) DO NOT form a triangle'.format(x1, y1, x2, y2, x3, y3))

        ans = input('Create another triangle? yes or no : ')
        if ans.lower() != "yes":
            done = True
    except ValueError:
        print('Invalid input!')

'''
'''
#question 6
A = 'Greetings'
k = 3

for i in (range(len(A) + 1)):
    if i >= k:
        print (A[:len(A)- i + k])

'''

'''
#question 4
def quoteread(file_quote):
        with open("quotes2.txt", "w", encoding='utf-8') as fileTwo:
            for line in fileOne:
                fileTwo.write(line.lstrip('\n'))


fileOne = open("quotes.txt", "r", encoding='utf-8')
print(quoteread(fileOne))
'''
'''

#question 5
def quotelineprime(file_quote):
    with open("quotes2.txt", "w", encoding='utf-8') as filetwo:

        for line in fileone:
            filetwo.write(line.lstrip("\n"))

def quotelinenonprime(file_quote):
    with open("quotes2.txt", "w", encoding='utf-8') as filetwo:

        for line in fileone:
            filetwo.write(line.strip("\n"))


fileone = open("quotes.txt", "r", encoding='utf-8')
print(quotelinenonprime(fileone))

'''
#question 5


file = open("quotes.txt", "r",  encoding='utf-8')
Counter = 0

Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print("This is the number of lines in the file", Counter)


def isPrime(n):

    if (n <= 1):
        return False

    for i in range(2, n):
        if (n % i == 0):
            return False

    return True




if isPrime(Counter):
    print("Prime number of lines in text file. ")
    print("Clearing all new line characters... ")
    with open("quotes.txt", "r", encoding='utf-8') as in_file:
        with open("quotes2.txt", "w", encoding='utf-8') as out_file:
            for line in in_file:
                out_file.write(line.lstrip("\n"))


else:
    print("Does not have prime number of lines in text file. ")
    print("Clearing all new line characters and adding tab space...  ")
    with open('quotes.txt', "r", encoding='utf-8') as in_file:
        with open("quotes2.txt", "w", encoding='utf-8') as out_file:
            for line in in_file:
                out_file.write(line.replace("\n", "\t"))


