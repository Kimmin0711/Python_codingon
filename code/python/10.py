'''조건문
age = 27
if age < 20:  # 17 < 20 -> True
    print("미성년자 입니다.")
if age >= 20:
    print("성인 입니다.")

# else 문
if age < 20:  # 17 < 20 -> True
    print("미성년자 입니다.")
else:  # Flase일 때 실행
    print("성인 입니다.")

print(f"나이는 {age}(세) 입니다.")

# elif 문
age = int(input("나이를 입력하세요: "))

if age < 20:
    print("10대 입니다.")
elif age < 30:
    print("20대 입니다.")
elif age < 40:
    print("30대 입니다.")
elif age < 50:
    print("40대 입니다.")
else:
    print("50대 이상입니다.")
'''

"""실습
# if
password = (input("비밀번호를 입력하세요: "))
if password == "abc123":
    print ("비밀번호가 맞습니다.")

num = int(input("숫자를 입력하세요: "))
if num % 2 == 0: 
    print ("짝수입니다.")

# if~else
password = (input("비밀번호를 입력하세요: "))
if password == "abc123":
    print ("비밀번호가 맞습니다.")
else:
    print ("비밀번호가 틀렸습니다.")

num = int(input("숫자를 입력하세요: "))
if num % 2 == 0: 
    print ("짝수입니다.")
else:
    print ("홀수입니다.")

# elif
socre = int(input("점수를 입력하세요: "))
if socre >= 90:
    print("학점: A")
elif socre >= 80:
    print("학점: B")
elif socre >= 70:
    print("학점: C")
elif socre >= 60:
    print("학점: D")
else:
    print("학점 F")
"""

''' 중첩 조건문
# 불리언(Boolean): 참과 거짓을 나타내는 데이터 타입
# 참: True
# 거짓: False

is_login = True
role = "admin"

if is_login:
    print("로그인 상태입니다.")
    if role == "admin":
        print("관리자 권한을 갖습니다.")
    elif role == "editor":
        print("편집자 권한을 갖습니다.")
    else:
        ("일반 사용자입니다.")

else:
    print("로그인이 필요합니다.")

# 삼항연산자
age = 18
status = "성인" if age >= 20 else "미성년자"
print(status)

number = 7
result = "짝수" if number % 2 == 0 else "홀수"
print(result)

a, b = 5, 8
# a = 5
# b = 8
max_value = a if a > b else b
print(max_value)

# 중첩 삼항연산자
score = 81
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(grade)
'''

''' 조건문에서 in 연산자 활용
users = ["Sean", "Linda", "Allie", "Martin"]

username = input("Name >> ")

if username in users:
    print(f"환영합니다, {username}님!")
else:
    print("등록되지 않은 사용자입니다. 회원가입을 진행해주세요.")
'''

# 실습
# 중첩 조건문
age = int(input("나이를 숫자로 입력해주세요: "))
pay = input("결제 방법을 입력해주세요(현금 또는 카드): ")
if age < 8:
    print (f"{age}세의 요금은 무료입니다.")

elif age < 14:
    if pay == "카드":
        print (f"{age}세의 {pay}요금은 450원 입니다.")
    if pay == "현금":
        print (f"{age}세의 {pay}요금은 450원 입니다.")

elif age < 20:
    if pay == "카드":
        print (f"{age}세의 {pay}요금은 720원 입니다.")
    if pay == "현금":
        print (f"{age}세의 {pay}요금은 1000원 입니다.")

elif age < 75:
    if pay == "카드":
        print (f"{age}세의 {pay}요금은 1200원 입니다.")
    if pay == "현금":
        print (f"{age}세의 {pay}요금은 1300원 입니다.")
else:
    print (f"{age}세의 요금은 무료입니다.")

# in 연산자
fruit_dict= {
    "apple": 95,
    "banana": 105,
    "cherry": 50
}
find_fruit = input("과일을 영문으로 입력하세요: ")
if find_fruit in fruit_dict:
    print (f"{find_fruit}의 칼로리는 {fruit_dict[find_fruit]}Kcal 입니다.")
else:
    print("포함되지 않는 과일입니다.")