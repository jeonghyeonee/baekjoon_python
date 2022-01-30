import heapq
import sys

input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    x = int(input())

    if x == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))