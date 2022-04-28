# recursion (재귀) - 함수가 자기 자신을 호출하는 것을 의미
# 재귀는 풀이를 더 명확하게 해준다. 다만, 성능이 더 나아지는 것은 아니다.
# 반복문이 더 성능이 좋은 경우가 많다.

# 큰 상자 속 작은 상자들 안에 들어있는 열쇠 찾는 2가지 방법
from numpy import empty

def look_for_key(main_box): # 메인 박스 - 반복문 형태
    pile = main_box.make_a_pile_to_look_through() # 내부를 확인할 상자 파일
    while pile is not empty: # while 반복문을 사용 - 파일이 비어있지 않은 한 반복문 계속
        box = pile.grab_a_box() # 박스 하나 선택
        for item in box:
            if item.is_a_box(): # 선택한 박스 내 박스가 또 있다면
                pile.append(item) # 파일에 박스 보내자
            elif item.is_a_key(): # 그렇지 않고 키를 찾았다면
                print('열쇠를 찾았어요!')

def look_for_key(box): # 재귀를 사용한 형태
    for item in box: # 박스를 하나씩 item 으로~
        if item.is_a_box(): # 선택한 박스 내 박스가 또 있다면
            look_for_key(item) # 재귀를 통해, 함수가 자기 자신을 호출하여 반복할 수 있게 유도
        elif item.is_a_key(): # 그렇지 않고 키를 찾았다면
            print('열쇠를 찾았어요!')

# 재귀 함수를 만들 때는 언제 재귀를 멈출지 알려줘야 한다.
# 그래서 재귀 함수는 <기본단계>와 <재귀단계>라는 두 부분으로 나뉜다.
# 재귀 단계: 함수가 자기 자신을 호출하는 부분
# 기본 단계: 함수가 자기 자신을 다시 호출하지 않는 경우, 즉 무한 반복으로 빠져들지 않게 하는 부분
def countdown(i):
    print (i)
    if i <= 1: # 기본 단계
        return
    else: # 재귀 단계
        countdown(i-1) # 함수 자기 자신을 불러서 사용

# stack (호출 스택) - 아주 단순한 자료구조
# push: 가장 위에 새 항목을 추가한다. + pop: 가장 위의 항목을 떼어내고 읽는다.
# 장점: 확인해야 할 것을 일일이 추적하지 않아도 되므로 편리함 (스택이 대신 하니까!)
# 단점: 모든 정보를 가져야 하므로 메모리를 많이 소비 = 함수 호출을 할 때마다 메모리를 사용함
# 어떤 함수를 호출하여 완전히 실행을 완료하기 전이라도 그 함수를 잠시 멈추고 다른 함수를 호출할 수 있다.

def greet(name): # 함수를 호출할 때마다 컴퓨터는 호출에 사용된 변수의 값을 저장한다.
    print('Hello, ' + name + '!')
    greet2(name) # 함수를 호출했기에 컴퓨터는 또 다른 메모리 상자를 할당한다.
    print('getting ready to say bye...')
    bye() # 함수를 호출했기에 컴퓨터는 또 다른 메모리 상자를 할당한다.

def greet2(name):
    print('How are you, ' + name + '?') # 함수 호출 상태에서 반환하여 돌아간다. (stack 에서 greet2 함수를 pop하고 greet 함수로 다시 돌아간다는 의미)

def bye():
    print('Ok, bye!') # 함수 호출 상태에서 반환하여 돌아간다. (stack 에서 bye 함수를 pop하고 greet 함수로 다시 돌아간다는 의미)

# 재귀 함수도 호출 스택을 사용한다.
# factorial function 예시
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
        
# fact 함수에 대한 각각의 호출이 자기만의 x값의 사본을 가지고 있다는 사실!
# 서로 다른 함수 호출에 대한 x값에 접근할 수 없다.