n, m = map(int, input().split())

num = list(map(int, input().split()))

s = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if num[i] + num[j] + num[k] > m:
                continue
            else:
                s = max(s, num[i] + num[j] + num[k])

print(s)