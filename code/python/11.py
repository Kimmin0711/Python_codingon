''' while 반복문
i = 5
while i > 0:
    print("반복문 연습", i)
    i -= 1
print("종료")

# 합계구하기
num = 1
total = 0
while num <= 10:
    total += num
    num += 1
print(f"1부터 10까지의 합은 {total}입니다.")

# 입력값 받기
user_input = ""
while user_input != "종료":
    user_input = input("종료하려면 '종료'를 입력하세요: ")
    print(f"입력한 값: {user_input}")
print("프로그램이 종료되었습니다.")
'''

'''break 문
# 예시. 숫자를 입력받아서 0이 입력되면 종료.
while True:
    num = int(input("숫자를 입력(0 입력시 종료): "))

    if num == 0:
        print("프로그램 종료")
        break
    print(f"입력한 숫자는 {num}입니다.")

# continue 문
# 예시. 숫자 입력받고 짝수만 출력하고 홀수는 건너뛰기
while True:
    num = int(input("숫자를 입력(음수 입력시 종료): "))

    if num < 0:
        print("프로그램 종료")
        break
    if num % 2 != 0:
        continue  # 홀수는 건너뛰고, 다시 입력
    print(f"입력한 짝수는 {num}입니다.")
    '''

# 실습
# while 문
while True:
    number = input("양수를 입력하세요('종료' 입력 시 프로그램 종료): ")

    if number == "종료":
        print("프로그램 종료")
        break
    
    if int(number) < 0:
        print("양수만 입력하세요.")
        continue

    if int(number) == 0:
        continue

    if int(number) > 0:
        num = 1
        total = 0
        while num <= int(number):
            total += num
            num += 1
    print(f"1부터 {number}까지의 합은 {total}입니다.")