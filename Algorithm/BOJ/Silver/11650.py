# 좌표 정렬하기
import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort(key=lambda x: (x[0], x[1]))

for point in points:
    print(*point)