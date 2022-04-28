# 탐욕 알고리즘 - 각각의 단계에서 최적의 수를 찾아내면 된다. 국소 최적해를 통해 최종적으로 전역 최적해를 구하는 방법
# 너비 우선 탐색, 다익스트라 알고리즘은 탐욕 알고리즘이다.

# 빠른 알고리즘 해법이 존재하지 않는 NP-완전 문제일 때 사용
# 시간을 낭비하지 않도록 문제 해결이 불가능한지 파악
# NP-완전 문제에 대해 간략한 해법을 빨리 구할 수 있는 근사 알고리즘이 탐욕 알고리즘
# 분명히 올바른 답을 내놓지는 못하지만 정답에 상당히 가까운 답이기도 하다.

# 근사 알고리즘의 성능 판단 기준 
# 1. 얼마나 빠른가
# 2. 최적해에 얼마나 가까운가

# 탐욕 알고리즘의 실행 속도는 O(n**2) 시간

# 집합의 형태로 자료를 보관하면 합집합, 교집합, 차집합 등 연산을 통해 다양한 방식으로 표현할 수 있다.
# 전국구에 방송할 수 있는 최소의 방송국 찾기
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {} # 선택된 방송국 목록 - 해시 테이블
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set() # 방문할 방송국의 목록을 저장할 집합

while states_needed: # 없어질 때까지 반복
    best_station = None
    states_coverd = set() # 방송되지 않은 주 중에서 해당 방송국이 커버하는 주의 집합

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station # 방송해야하는 주 & 방송국이 커버하는 주
        if len(covered) > len(states_coverd): # 커버하는 주가 더 많다면
            best_station = station
            states_coverd = covered
        
    final_stations.add(best_station) # 방송국 목록에는 추가
    states_needed -= states_coverd # 방송이 필요한 주에서는 삭제

print(final_stations)


# NP-완전 문제
# 1. 집합 커버링 문제를 풀기 위해서는 가능한 모든 집합을 계산해야 한다.
# 2. 외판원 문제 - 팩토리얼 함수 사용해야 하는데, 도시의 수가 많을 경우 정확한 해답을 구하는 게 어려워짐
# 공통점 - 모든 가능한 경우를 다 따져서 최단/최소를 구해야 한다는 것

# NP-완전 문제인지 알 수 있는 방법은? 없다. 다만 참고사항은 있다.
# 1. 항목이 적을 때는 알고리즘이 빠른데, 항목이 늘어나면서 갑자기 느려진다.
# 2. "X의 모든 조합"이라고 하면 보통 NP-완전 문제
# 3. 더 작은 하위 문제로 변환할 수 없어서 "X의 가능한 모든 버전"을 계산해야 한다면 아마 NP-완전 문제
# 4. 문제가 수열을 포함하고 풀기가 어려우면 NP-완전 문제
# 5. 문제에 집합이 있고 풀기가 어려우면 NP-완전 문제
# 6. 집합 커버링 문제나 외판원 문제로 재정의할 수 있다면, NP-완전 문제