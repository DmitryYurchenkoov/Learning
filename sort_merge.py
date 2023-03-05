# Сортировка слиянием
# Для реализации данной сортировки длина массивов должна быть +- одиннаковая
# Это лишь алгоритм
import random

def merge(A:list, B:list):
    C=[0]*(len(A)+len(B))
    i = 0
    k = 0
    n = 0
    while i < len(A) and k<len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i+=1
        n+=1
    while k < len(B):
        C[n] = B[k]
        k+=1
        n+=1
    return C

#Сама сортировка
def merge_sort(A):
    if len(A)<= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)] #Срез
    R = [A[i] for i in range(middle, -1)]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]
    print(C)


arr = [1, 3, 8, 2]
merge_sort(arr)


