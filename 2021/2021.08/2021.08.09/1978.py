n = int(input())
a = list(map(int, input().split()))

count = 0

for i in a:
    cnt = 0
    for j in range(1, i+1):
        if i%j == 0:
            cnt += 1
    if cnt == 2:
        count += 1
print(count)