#Question 4
import random
class Matrix():
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[random.randint(0, 100) for x in range(cols)] for y in range(rows)]


b = Matrix(4,5)

print(b.matrix)

