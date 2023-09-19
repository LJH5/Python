# 1 ≤ m, n ≤ 40,000, 1 ≤ x ≤ m, 1 ≤ y ≤ n
# x' = x + 1 m < x이면 x' = 1
# <x':y'>
# <n, m>은 마지막
def check():
    k = x
    while k <= m * n:
        print(k, y)
        if (k - y) % n == 0:
            return k
        k += m
    return -1


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())

    print(check())



'''
m = 7, n = 12 일때
    
1 1 8  3 10 5  12 7     | 1 1  8         (15 % 12) (22 % 12) 
2 2 9  4 11 6  1  8     | 2 2  9         (16 % 12) (23 % 12)
3 3 10 5 12 7  2  9     | 3 3  10        (17 % 12) (24 % 12) 31 38 45 
4 4 11 6 1  8  3  10    | 4 4  11        (18 % 12) (25 % 12)
5 5 12 7 2  9  4        | 5 5  12        (19 % 12) (26 % 12)
6 6 1  8 3  10 5        | 6 6  (13 % 12) (20 % 12) ...
7 7 2  9 4  11 6        | 7 7  (14 % 12) (21 % 12)

1 2 3 4 5 6 7 8 9 10 11 12

x % 12 = 9

(x - 9) % 12 = 0 


옆으로 1칸 이동하면 idx는 |n - m|만큼 이동
<3:9>가 되려면 몇칸을 이동해야 하는 가?
x = 3, y = 9

15칸 이동하는 것은 3칸 이동하는 것과 같음
<3:9>는 index가 9에서 3으로 가야함
즉 (9 + 5 * a) % 12 = 3
a = 6

답은 x + m * a = 45

'''