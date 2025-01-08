'''
song = input("너의 최애 노래는? ")

a = input("1 + 1 = ")
print(a)  # 2
#" 2" 문자열의 타입을 "숫자형(정수형)" 으로 변환 필요
# => "형 변환"
print(a*2)  # 22 <= "2" * 2
'''

# 형변환 (type casting, type conversion)
# 1. 정수형으로 변환
print(int("10"))  # 문자열 "10" 을 정수로 변환
print(int(10.9))  # 실수 10.9를 정수로 변환(소수점 이하 버림)

# 2. 실수형으로 변환
print(float("11.2"))  # 문자열 "11.2" 를 실수로 변환
print(float(10))  # 정수 10을 실수로 변환

'''3. 형변환 안되는 예시
print(int("name"))  # 숫자 기호가 아닌 문자열을 변환하러 할 때
print(int("11.2"))  # 실수 문자열을 정수로 변환하려 할 때
'''

b =2  # 정수형
print(b * 10)  # 20
print(str(b) * 10)  # "2"*10 = 2222222222
print(str(b) + "입니다.")
#print(b + "입니다.")  # int와 str은 더해줄 수 없다는 에러 뜸

# str 활용 예시
math_score = 90
eng_score = 85
total_score = math_score + eng_score
avg_score = total_score / 2

print("합계: " + str(total_score))
print("평균: " + str(avg_score))


#실습
# 1번
name = input("이름을 입력하세요.: ")
age = input("나이를 입력하세요.: ")
print(f"안녕하세요! " + str(name)+ "님 " + "(" + str(age)+ "세" + ")")

# 2번
name = input("이름을 입력하세요.: ")
born = input("태어난 년도를 입력하세요.: ")
year = input("올해 년도를 입력하세요.: ")
age = int(year) - int(born) + 1
print(f"올해는" + str(year) + "년, " + str(name) + "님의 나이는" + str(age) + "세 입니다.")