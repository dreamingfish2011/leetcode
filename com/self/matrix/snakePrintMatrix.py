a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
n = len(a)
for i in range(n - 1, 0, -1):
    for j in range(0, n - i):
        print(a[j][i + j])
    print("=" * 20)
for i in range(0, n):
    for j in range(0, n - i):
        print(a[i + j][j])
    print("=" * 20)
print("=" * 50)

for i in range(n + n - 1):
    for j in range(i + 1):
        k = i - j
        if k < n and k >= 0 and j < n:
            print(a[j][k])
    print("=" * 20)
