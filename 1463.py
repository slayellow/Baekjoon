# 0 ~ 99999
N = int(input())
count = 0
result = [[0]*3 for i in range(100000)]

for i, res in enumerate(result):
    if i == 0 or i == 1:
        continue
    else:
        if i % 3 == 0:
            res[2] = int(i/3)
        if i % 2 == 0:
            res[1] = int(i/2)
        res[0] = i - 1
