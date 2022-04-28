# Hash Table(해시 테이블) - 해시 함수와 배열을 합친 자료구조! 
# 해시 함수는 문자열(str)을 받아서 숫자를 반환하는 함수다.
# 해시 함수는 문자열에 대해 숫자를 할당(mapping)한다.
# 배열과 리스트는 직접 메모리를 할당하지만, 해시 테이블은 해시 함수를 사용해서 어디에 원소를 저장할지 결정

# 장점
# 1. 무엇보다 속도가 빠르다
# 2. 어떤 것과 다른 것 사이의 관계를 모형화할 수 있다.
# 3. 중복을 막을 수 있다.
# 4. 서버에게 작업을 시키지 않고 자료를 캐싱할 수 있다.
# key & value 를 가진다 = key에 대해 value(값)을 할당한다.

book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book)
print(book["avocado"])

# 사용 예시 - 전화번호부, 인터넷 주소창 검색(IP 주소로 할당한 후 검색), 투표소에서 투표한 사람 확인(중복 확인), 웹사이트 캐시로 활용
# 해시 테이블 쓰면 좋은 경우 - 어떤 것을 다른 것과 연관시키고자 할 때 & 무언가를 찾아보고자 할 때

phone_book = {}

phone_book["jenny"] = 12345678
phone_book["emergency"] = 119

print(phone_book)
print(phone_book["jenny"])

# 해시 함수의 특성
# 1. 일관성: 같은 이름에 대해서는 항상 같은 인덱스를 할당
# 2. 다른 단어를 넣으면 다른 숫자가 나온다 (다른 문자열에 다른 인덱스를 할당)
# 3. 배열이 얼마나 큰지 알고 있어야 하며, 유효한 인덱스만 반환해야 한다.
# 4. 좋은 해시 함수는 키를 해시 테이블 전체에 고르게 할당해야 한다.
# 5. 만약 연결 리스트가 길어지면 해시 테이블의 속도도 느려진다. 반대로 좋은 해시 함수는 충돌을 최소화한다.

voted = {}

def check_voter(name):
    if voted.get(name):
        print("돌려 보내세요!")
    else:
        voted[name] = True
        print("투표 하세요!")

check_voter("tom")
check_voter("mike")
check_voter("mike")


# 해시 테이블의 성능 - Big-O 표기
# 평균 - 탐색: O(1), 삽입: O(1), 삭제: O(1)
# 최악 - 탐색: O(n), 삽입: O(n), 삭제: O(n)
# 충돌을 피하려면 낮은 사용률 & 좋은 해시 함수가 필요!

# 웹사이트 캐시
cache = {}
get_data_from_server = {}

def get_page(url):
    if cache.get(url): # 캐시에 url 데이터 있어?
        return cache[url] # 바로 데이터 보내줘~
    else:
        data = get_data_from_server(url) # 서버에서 url 데이터 가져와!
        cache[url] = data # 캐시에 처음으로 데이터를 저장
        return data