#Question 3
#Python program
import string
def encrypt():
    with open("file1", "r", encoding='utf-8') as myfile:
        line = myfile.read()
        temp = ''.join([word for word in line if word.isalnum() or word.isspace()])

        lower = list(string.ascii_lowercase)
        upper = list(string.ascii_uppercase)
        num = [0,1,2,3,4,5,6,7,8,9]
        encryptstr = []

        for i in temp:
            if (i.isspace() == True):
                encryptstr.append(i)

            elif (i in string.ascii_lowercase):
                x = (lower.index(i) - 1) % 26
                encryptstr.append(lower[x])


            elif (i in string.ascii_uppercase):
                x = (upper.index(i) + 1) % 26
                encryptstr.append(upper[x])

            elif (int(i) in num):
                x = (num.index(int(i)) - 1) % 10
                encryptstr.append(num[x])


        s = ""
        for i in encryptstr:
            s+=str(i)
        print(s)
    with open("encrypted.txt", "w", encoding='utf-8') as myfile:
        myfile.write(s)


def decrypt():
    with open("encrypted.txt", "r", encoding='utf-8') as myfile:
        line = myfile.read()
        temp = ''.join([word for word in line if word.isalnum() or word.isspace()])

        lower = list(string.ascii_lowercase)
        upper = list(string.ascii_uppercase)
        num = [0,1,2,3,4,5,6,7,8,9]
        encryptstr = []

        for i in temp:
            if (i.isspace() == True):
                encryptstr.append(i)

            elif (i in string.ascii_lowercase):
                x = (lower.index(i) + 1) % 26
                encryptstr.append(lower[x])


            elif (i in string.ascii_uppercase):
                x = (upper.index(i) - 1) % 26
                encryptstr.append(upper[x])

            elif (int(i) in num):
                x = (num.index(int(i)) + 1) % 10
                encryptstr.append(num[x])

        s = ""
        for i in encryptstr:
            s+=str(i)
        print(s)

    with open("decrypted.txt", "w", encoding='utf-8') as myfile:
        myfile.write(s)


print(encrypt())
print(decrypt())