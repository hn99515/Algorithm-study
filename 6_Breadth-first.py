# 너비 우선 탐색 (BFS, Breadth-First Search) - 두 항목 간의 최단 경로를 찾을 수 있음
# 그래프를 대상으로 하는 다른 종류의 탐색 알고리즘

# 사용 예시
# 1. 체커 게임에서 가장 적은 수로 승리할 수 있는 방법을 계산하는 인공지능
# 2. 맞춤법 검사기 - 실제 단어에서 가장 적은 개수의 글자를 고쳐서 올바른 단어를 만드는 방법을 찾는다.
# 3. 여러분의 네트워크에서 가장 가까운 의사 선생님을 찾기

# 그래프(graph)란 연결의 집합을 모형화한 것
# 그래프는 정점(node)과 간선(edge)으로 이루어져 있다.
# 정점은 여러 개의 다른 정점과 이어질 수 있으며, 이렇게 이어진 정점을 이웃(neighbor)이라고 한다.
# 정점과의 관계를 표현하기 위해서 해시 테이블을 사용

from collections import deque
graph = {}

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person, "is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

# 너비 우선 탐색 알고리즘의 질문 유형
# 1. 출발지와 목표지점까지의 경로가 존재하는가?
# 2. 출발지에서 목표지점으로 가는 최단 경로는 무엇인가? - 목록에 더해진 순서대로 탐색 시작

# 큐 (Queue) - 대기열
# 큐는 큐 안의 원소에 임의로 접근할 수 없다.
# 삽입과 제거, 2가지 연산을 할 수 있다 - 목록에 먼저 추가된 사람들을 먼저 꺼내서 탐색
# 선입선출(FIFO) 자료구조