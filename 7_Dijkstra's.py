# 다익스트라 알고리즘 - 그래프의 간선에 가중치를 준 '가중 그래프'에서 가장 빠른 경로를 찾고 싶을 때 사용
# 최소화를 가능하게 만들어주는 알고리즘!

# 4단계 구성
# 1. 가장 가격이 싼(혹은 시간이 적게 걸리는) 정점을 찾는다.
# 2. 이 정점의 이웃 정점들의 가격을 조사한다. 현재 가격보다 더 싼 가격이 존재하면 가격을 수정한다.
# 3. 그래프 상의 모든 정점에 대해 이러한 일을 반복한다.
# 4. 최종 경로를 계산한다.

# 너비우선탐색은 두 점 간의 최단 경로를 찾을 때, 가장 적은 수의 구간을 가지는 경로를 의미 - 균일 그래프
# 다익스트라 알고리즘은 각 구간에 대해 숫자 혹은 가중치를 줄 수 있다. 그리고 전체 가중치의 합이 가장 작은 구간을 찾는다. - 가중 그래프
# 단, 다익스트라 알고리즘은 사이클이 있는 그래프에서는 가중치가 양수일 때만 적용된다. 가중치가 음수면 사용 불가.

# 구현 예시 - 출발점 ~ 도착점까지의 최단 시간의 거리는?
graph = {} # 그래프 테이블
graph["start"] = {}
graph["start"]["a"] = 6 # 해시테이블 내 해시테이블 구조
graph["start"]["b"] = 2
print(graph["start"].keys())
print(graph["start"]["a"]) # 간선 가중치
print(graph["start"]["b"]) # 간선 가중치
print()

graph["a"] = {}
graph["a"]["finish"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5
graph["finish"] = {}

infinity = float("inf") # 무한대를 의미
costs = {} # 가격 테이블
costs["a"] = 6
costs["b"] = 2
costs["finish"] = infinity

parents = {} # 부모 테이블
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

processed = [] # 처리한 정점의 리스트

def find_lowest_cost_node():
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if node not in processed:
            if cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)