from collections import deque


def topological_sort(n, edges):
    # n: 정점 수, edges: 간선 리스트 (u, v) → u → v
    adj_list = [[] for _ in range(n)]
    Indegree = [0] * n

    # 그래프 구성 및 진입 차수 계산
    for u, v in edges:
        adj_list[u].append(v)
        Indegree[v] += 1

    # 진입 차수가 0인 노드를 큐에 추가
    queue = deque([i for i in range(n) if Indegree[i] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in adj_list[u]:
            Indegree[v] -= 1
            if Indegree[v] == 0:
                queue.append(v)

    if len(result) != n:
        raise ValueError("위상 정렬 불가")

    return result


# ---------------------------
# 예시
# ---------------------------

if __name__ == "__main__":
    # 정점 수 (0부터 n-1까지)
    n = 6
    # 간선 리스트
    edges = [
        (5, 2),
        (5, 0),
        (4, 0),
        (4, 1),
        (2, 3),
        (3, 1)
    ]

    order = topological_sort(n, edges)
    print("위상 정렬 결과:", order)
