# for 문
# range 함수
for i in range(5):  # 0부터 5미만까지지
    print(i, end=" ")
print()  # print() 지우면 다 한줄로 출력

for i in range(2, 7):  # 2부터 7미만까지지
    print(i, end=" ")
print()

for i in range(11, 20, 2):  # 11부터 20미만까지 2씩 뛰어넘기기
    print(i, end=" ")
print()

for i in range(10, 0,-3):  # 10부터 0까지 3씩 뛰어넘기
    print(i, end=" ")
print()

# 리스트와 for 문
fruits = ["사과", "바나나", "포도", "체리"]
for fruit in fruits:
    print(fruit, end="|")

# 합계구하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
total = 0
for num in numbers:
    total += num
    print("현재 total >>", total)
print(f"합계는 {total}입니다.")

# 조건문과 함께 사용
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
print()

# 딕셔너리와 for 문
my_dic = {
    "name": "홍길동",
    "address": "서울시 은평구",
    "gender": "남성",
    "hobby": ["런닝", "헬스", "낚시"]
}
# key값만 순회
for i in my_dic:
    print(i, end=" ")
print()

# 명사적으로 key값만 순회회
for i in my_dic.keys():
    print(i, end:=" ")
print()

# values값만 순회
print(my_dic.values())
for i in my_dic.values():
    print(i, end=",")
print()

# key, value 함께 순회
for key, value in my_dic.items():
    print(f"{key}: {value}")