n, m = map(int, input().split())

s = []

def backtracking(num):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(num, n+1):
        if i not in s:
            s.append(i)
            backtracking(i+1)
            s.pop()

backtracking(1)