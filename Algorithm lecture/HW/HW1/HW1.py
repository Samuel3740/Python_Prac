import random
from timeit import default_timer as timer

def insertion_sort(A):
    for i in range(1, len(A)):  # 두 번째 원소부터 시작
        loc = i - 1
        new_item = A[i]  # 현재 정렬할 원소 저장

        while loc >= 0 and new_item < A[loc]:  # 현재 원소가 앞의 원소보다 작다면
            A[loc + 1] = A[loc]  # 앞의 원소를 한 칸 뒤로 이동
            loc -= 1  # 비교 대상 한 칸 앞으로 이동

        A[loc + 1] = new_item  # 적절한 위치에 현재 원소 삽입

def test(A):
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:  # 앞 원소가 뒷 원소보다 크다면 정렬되지 않음
            return False
    return True

# 실행 예제
A = [5, 1, 8, 7, 2]
print("정렬 전:", A)
insertion_sort(A)
print("정렬 후:", A)
print("정렬 결과:", test(A))  # True 출력
