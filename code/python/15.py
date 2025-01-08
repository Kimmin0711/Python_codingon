# 함수
# 1. 매개변수x, 리턴값x
def say_hello():  # 함수 정의
    print("Hello, World")


say_hello()  # 함수 호출

# 2. 매개변수o, 리턴값x
# 매개변수 1개
def print_greeting(name):  # 함수 정의
    print(f"Hello, {name}")

print_greeting("Allie")  # 함수 호출
print_greeting("Martin")

# 매개변수 2개
def gugudan(dan, end):  # 함수 정의
    print(f"{dan}단")
    for i in range(1, end):
        print(f"{dan}x{i}={dan*i}")
    
gugudan(7, 15)  # 함수 호출
gugudan(4, 19)

# 매개변수x, 리턴값o
def mul_numbers():  # 함수 정의
    print("곱셈을 시작합니다.")
    return 10*5

result = mul_numbers()  # 함수 호출
print(result)

# 4. 매개변수o, 리턴값o
def add_numbers(x, y):
    print("덧셈을 시작합니다.")
    return x+y

result2 = add_numbers(40, 50)
print(result2)

# 다양한 타일을 return 하는 함수
# 1. list 타입을 반환하는 함수
# ex. 제한값(limit) 미만의 짝수를 출력하는 함수
def print_even_numbers(limit):
    return [i for i in range(0, limit) if i % 2 == 0]

print(print_even_numbers(10))

# 2. 딕셔너리 타입을 반환하는 함수
def print_user_info(name, grade):
    return{'user_name': name, 'user_grade': grade}

print(print_user_info('Alice', 2))
print(print_user_info('Bob', 4))

# 3. Set 타일을 반환하는 함수
# print(set("Hello"))  # {'e', 'H', 'l', 'o'}
# 문자열을 set 타입으로 변환 => 고유한 문자들만 남긴다.
def print_unique_char(word):
    return set(word)

print(print_unique_char("Hi, My name is Min"))

# 4. 튜플 타입을 반환하는 함수
# ex. 두 숫자의 합과 곱을 동시 반환 => (합, 곱)
def calculate_sum_and_product(a, b):
    return(a+b, a*b)

print(calculate_sum_and_product(3, 5))
print(calculate_sum_and_product(7, 2))


# Collection (컬렉션)
# 혼합 컬렉션
# ex. 딕셔너리 안에 리스트가 있는 예시
def split_numbers(numbers):
    even_nums = [n for n in numbers if n%2 == 0]
    odd_nums = [n for n in numbers if n%2 != 0]
    
    # 반환값(딕셔너리)
    return {"odd": odd_nums, "even":even_nums}

# {"odd": [1, 3, 5, 7, 9], "even": [2, 4, 6, 8, 10]}
print(split_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# 매개변수로 리스트를 받는 함수
# ex. 각 요소를 두배로 만드는 함수
def double(nums):
    return [i * 2 for i in nums]

print(double(([1, 2, 3, 4])))

# ex. 각 요소를 문자열로 변환하는 함수
def to_string(nums):
    return [str(i) for i in nums]

print(to_string([8, 16, 24]))

# 실습
# 두 수(2, 2)를 매개변수 전달하여 서로 a같으면 곱하고, 다르면 더하기
x = int(input("첫번째 수를 입력하세요: "))
y = int(input("두번째 수를 입력하세요: "))
def sum(x, y):
    if x == y:
        return (f"결과(곱): {x*y}")
    else:
        return (f"결과(합): {x+y}")
print(sum(x, y))

# 주문 상품 가격이 20.0 미만이면 배송비2.5 포함, 아니면 포함x
def parcel_items(item, price):
    if price > 20000:
        return(f"{item}의 가격: {price}원")
    else:
        return(f"{item}의 가격: {price+2500}원")
print(parcel_items("상품 1", 30000))
print(parcel_items("상품 2", 15000))