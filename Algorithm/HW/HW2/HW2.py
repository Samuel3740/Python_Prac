import random
from timeit import default_timer as timer

def partition(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

def qsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        qsort(A, p, q - 1)
        qsort(A, q + 1, r)

def test(A):
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            return False
    return True

# test
x = random.sample(range(10000), 100)
start = timer()
qsort(x, 0, len(x) - 1)
print(timer() - start)
print(x)
print(test(x))