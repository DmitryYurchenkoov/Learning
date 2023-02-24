

lst = [2, 4, 3]

def modify_list(l:list):
    B = [int(i/2) for i in l if i % 2 == 0]
    l.clear()

    for x in B:
        l.append(x)



modify_list(lst)

print(lst)

