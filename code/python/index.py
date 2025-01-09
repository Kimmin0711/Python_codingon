# 조건 1. 사용자는 소비자, 주인 두가지 종류로 입력받기(번호or값)
# 그 외의 값은 잘못된 값으로 출력[0]

# 조건 2. 소비자일 때 마시고 싶은 음료 입력받기[0]
# 조건 2-1. 값이 있으면 값을 제거, 없으면 없음 출력[0]

# 조건 3. 주인일 때 추가, 삭제, 두 가지 종류 입력 받기(조건 1과 같게)[0]
# 조건 3-1. 추가일 때 추가할 음료수 입력받고 값을 추가 후, 같은 값끼리 연결되게 출력[0]
# 조건 3-2. 삭제일 때 삭제할 음료수 입력받고 값이 있으면 제거, 없으면 없음 출력[0]

vending_machine = [
    '게토레이' , '게토레이', 
    '레쓰비', '레쓰비',
    '생수', '생수',
    '이프로'
    ]
'''
while True:
    print(f"남은 음료수: {vending_machine}")

    user = input("사용자 종류를 입력하세요:\n1. 소비자\n2. 주인\n")

    if user == "1" or user == "소비자":
        drink = input("마시고 싶은 음료?: ")
        if drink in vending_machine:
            print(f"{drink} 드릴게요.")
            vending_machine.remove(drink)
        else:
            print(f"{drink}는(은) 없어요.")
    elif user == "2" or user == "주인":
        work = input("할 일 선택: \n1. 추가\n2. 삭제\n")
        if work == "1" or work == "추가":
            print(f"남은 음료수: {vending_machine}")
            plus = input("추가 할 음료수? ")
            vending_machine.append(plus)
            vending_machine.sort()
            print("추가 완료")
        elif work == "2" or work == "삭제":
            print(f"남은 음료수: {vending_machine}")
            minus = input("삭제 할 음료수? ")
            if drink in vending_machine:
                vending_machine.remove(minus)
                print("삭제 완료")
            else:
                print("없음.")
    else:
        print("\n>>잘못된 값입니다.")
'''

# check_machine 남은 음료수 확인하는 함수
def check_machine():
    return (f"남은 음료수: {vending_machine}")

# is_drink 음료수가 있는지 확인하는 함수
def is_drink(drink):
    if drink in vending_machine:
        return (f"{drink} 드릴게요.")
    else:
        return(f"{drink} 없어요.")

# add_drink 음료수를 추가하는 함수
def add_drink(plus):
    vending_machine.append(plus)
    vending_machine.sort()
    return (f"{plus} 추가 완료")

# remove_drink 음료수를 제거하는 함수
def remove_drink(minus):
    if minus in vending_machine:
        vending_machine.remove(minus)
        print("삭제 완료")

print(check_machine())

user = input("사용자 종류를 입력하세요:\n1. 소비자\n2. 주인\n")
if user == "1" or user == "소비자":
    print(is_drink(input("마시고 싶은 음료: ")))

elif user == "2" or user == "주인":
    work = input("할 일 선택: \n1. 추가\n2. 삭제\n")
    if work == "1" or work == "추가":
        print(check_machine())
        print(add_drink(input("추가 할 음료: ")))
    elif work == "2" or work == "삭제":
        print(check_machine())
        print(remove_drink(input("제거 할 음료: ")))
else:
    print("잘못된 값입니다.")