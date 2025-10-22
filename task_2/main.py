#Кешко Маргарита
import random
matrix =[-3,-5,-2,12,0,15,4,7,2]#задали числа для матрицы
rows = random.randint(4,8)#строки
cols = random.randint(4,8)#столбцы
matrix = [[random.choice(matrix) for _ in range(cols)] for _ in range(rows)]#генерацция кол-во столбцов
for rows in matrix:
    print('|', end=" ")
    for num in rows:
        print (f"{num} ",end=" ")
    print ("|")#создание матрицы
nesum = sum(num for rows in matrix for num in rows if num <0 )#
print(f"сумма отрицательных значений: {nesum}")#

       
