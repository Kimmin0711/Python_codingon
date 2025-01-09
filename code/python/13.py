# 리스트 내포
# : 파이썬에서 리스트를 간결하게 생성하는 문법
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)

squares2 = [n**2 for n in range(1, 6)]
print(squares2)

# 조건문과 함께 사용
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)


# 실습
# 구구단 만들기
quiet = int(input("몇단을 출력할까요?: "))
answer = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    answer = quiet*num
    print(f"{quiet}x{num}=", answer)

# 정수 합 계산
# 1부터 사용자가 입력한 수까지 홀수의 합 구하기
num = int(input("어디까지 계산할까요?: "))
plus = 0
for i in range(1, num+1, 2):
    plus += i
print(f"1부터 {num}까지의 홀수의 합: {plus}")

# 평균값 구하기
students = {
    "student1": [83, 92, 88],
    "student2": [90, 79, 86],
    "student3": [88, 86, 94]
}
kr = 0
en = 0
mt = 0

for i in students.values():
    kr += i[0]    
    en += i[1]    
    mt += i[2]    
print(f"국어의 평균값은 {kr/3:.0f}점, \
      영어의 평균값은 {en/3:.0f}점, \
      수학의 평균값은 {mt/3:.0f}점 입니다.")
# :.0f -> f는 소수점 숫자를 의미, .n 은 소수점 n째 자리까지 표시하도록 지정