# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое
# число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность
# чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
x = int(input())
digit_arr = []
count = 1
count_while = 1
for b in range(1, x+1):
    if len(digit_arr) == x:
        break
    elif x == 1:
        print(1)
        break
    while count_while != 0:
        if len(digit_arr) == x:
            print(*digit_arr)
            break
        digit_arr.append(b)
        count_while -= 1
    count_while = count + 1
    count += 1

print(len(digit_arr))














