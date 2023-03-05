##Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
##Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
##В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.


massives = [[int(i) for i in input().split()]]
b = input()
while b != 'end':
    massives.append([int(i) for i in b.split()])
    b = input()
count = 0
for arr in massives:
    if count > 0:
        print(end='\n')
    for el in arr:
        schet = massives[massives.index(arr) - 1][arr.index(el)] + massives[(massives.index(arr) + 1) % len(massives)][arr.index(el)] + massives[massives.index(arr)][arr.index(el) - 1]
        + massives[massives.index(arr)][(arr.index(el) + 1) % len(massives[massives.index(arr)])]
        count += 1
        print(schet, end=" ")

