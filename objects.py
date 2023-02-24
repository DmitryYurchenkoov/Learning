objects = [1, 2, 1, 2, 3, 1, 4, 8, 9, 10, 3, -1]
ans = 0
for i in objects:
    if objects.count(i) > 1:
        ans += 1

print(ans)