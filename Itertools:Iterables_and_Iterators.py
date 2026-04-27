from itertools import combinations
x = int(input())
s = input().split()
k = int(input())
n1 = [str(i) for i in range(1, x + 1)]
lt = list(combinations(n1, k))
slt = [str(i + 1) for i, j in enumerate(s) if j == 'a']
count = 0
for p in lt:
    for m in slt:
        if m in p:
            count += 1
            break
print(round(count / len(lt), 3))
