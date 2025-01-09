# 내장함수

# abs(정수): 절댓값 구하는 내장함수
print(abs(-77))
print(abs(0))
print(abs(23))

# 만약에, abs() 내장함수가 없었다면
def my_abs(n):
    if n < 0:  # 음수라면 양수로 변환
        return -n
    else:   # 0 혹은 양수이니 그대로 변환
        return n

# pow(x, y): x^y 을 구하는 내장함수
print(pow(10, 2))
print(pow(2,10))
print(pow(3, 4))

# map()
def square(x):  # 각 요소마다 적용하고 싶은 함수
    return x**3

numbers = [2, 4, 6, 8, 10]

print(list(map(square, numbers)))  # [8, 64, 216, 512, 1000]
# <map object at 0x000001F8194A14E0> <- list 제외하면 뜨는 값

# filter(): 주어진 조건을 만족하는 요소만 필터링하여 반환
def even_number(x):
    return x % 2 == 0

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter(even_number, numbers2))  # <filter object at 0x000001AC8E991930>
print(list(filter(even_number, numbers2)))  # [2, 4, 6, 8, 10]

# 실습
# 1~30까지의 자연수 중 배수와 배수의 개수를 계산하는 함수
def even_number(n):
    return n % 3 == 0
square = [n for n in range(1, 31)]
count = len((list(filter(even_number, square))))  # len 이용하여 요소 개수 구함
print("3의 배수의 개수:", count)