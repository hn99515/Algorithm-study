# Algorithm(알고리즘)
# 정의: 어떤 일을 하기 위한 명령의 집합
# 알고리즘을 공부하는 이유는 다른 코드보다 속도를 빠르게 하거나, 아주 흥미로운 문제를 풀기 위해서다.


# binary-search (이진 탐색)
# 1. 입력으로는 정렬된 원소 리스트를 받는다.
# 2. 리스트에 원하는 원소가 있으면 그 원소의 위치를 반환하고, 아니면 null 값을 반환

# 알고리즘 실행 시간 비교: 단순 탐색은 O(n) - 선형 시간 / 이진 탐색은 O(log n) - 로그 시간
# 리스트의 원소 개수가 증가하면 상대적으로 이진 탐색이 더 빨라진다.

# Big-O 표기법: 속도를 시간 단위로 세지 않으며, 연산 횟수가 어떻게 증가하는지로 측정 / 최악의 실행 시간을 나타낸다.
# Big-O 실행 시간의 종류: O(log n) > O(n) > O(n * log n) > O(n**2) > O(n!)  <속도순 나열>
# 최악의 경우에 대한 실행 시간 이외에도 평균 실행 시간을 살표보는 것도 중요함!

def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high: # 탐색 범위를 하나로 줄이지 못했으면 계속 실행하라.
        mid = (low + high) // 2 # low + high 가 짝수가 아니면 자동으로 mid값을 정수로 내림한다.
        guess = list[mid] # 리스트 크기의 딱 가운데 자리값 (추측값)

        if guess == item: # 정답(item)이 guess(추측)와 같을 때
            return mid # mid 그대로 출력
        if guess > item: # 추측한 위치가 정답 위치보다 크면
            high = mid - 1 # 최대 위치를 추측한 위치에서 -1 (정답 아닌 절반 날리기)
        else: # 추측한 위치가 정답 위치보다 작으면
            low = mid + 1 # 최소 위치를 추측한 위치에서 +1 (정답 아닌 절반 날리기)
    return None # 정답(item)이 리스트에 없으면 None 리턴

my_list = [1,3,5,7,9]
print('binary_search: ', binary_search(my_list, 5)) # 그 원소의 위치 값을 반환한다.