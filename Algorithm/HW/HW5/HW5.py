# 피보나치 수열
def fib(n):
    if n <= 2:
        return 1
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


# 행렬 경로 문제
def matrix_path(m):
    n = len(m) - 1
    c = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            c[i][j] = m[i][j] + max(c[i - 1][j], c[i][j - 1])
    return c[n][n]

# ---------------------------
# 예시
# ---------------------------

if __name__ == "__main__":
    print("Fibonacci fib(10):", fib(10))

    matrix = [
        [0, 0, 0, 0, 0],
        [0, 6, 7, 12, 5],
        [0, 5, 3, 11, 18],
        [0, 7, 17, 3, 3],
        [0, 8, 10, 14, 9]
    ]
    print("Matrix Path (4x4):", matrix_path(matrix))
