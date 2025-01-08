'''
# 이중 for문
for i in range(5):
    print(f'외부 반복문의 i 값: {i}')

    for j in range(3):
        print(f'내부 반복문의 j 값: {j}')
    
    print("-------------------")

# 이차원 리스트와 이중 for문
maxtix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 요소 (elem 변수)의 합계 구하기
total_sum = 0
for row in maxtix:
    # print(f'외부 반복문의 row: {row}')

    for elem in row:
        # print(f'내부 반복문의 elem: {elem}')
        total_sum += elem
    # 1번 시점: 내부 반복문이 종료될 때
    print(f"중간 합계: {total_sum}")
# 2번 시점: 외부 반복문이 종료될 때
print(f'전체 합계: {total_sum}')

# 짝수만 출력하기
maxtix2 = [
    [4, 21, 77],
    [60, 17, 98],
    [2, 74, 33]
]
print("짝수만 출력:", end = " ")
for row in maxtix2:
    for elem in row:
        if elem %2 == 0:
            print(elem, end=",")
'''

# 실습
# 이중 for문 구구단 만들기
for i in range(2,10):
    print(f"[{i}단]")
    for j in range(1,10):
        print(f"{i}x{j}={i*j}")

# 별찍기
for i in range(3):  #세로 (0,n)경우 0 생략가능
    print("")
    for j in range(5):  #가로
        print("*", end ="")
print("\n===============")

# 별찍기2
for i in range(4):
    print("")
    for j in range(i+1):
        print("*", end="")
print("\n===============")

# 별찍기3
for i in range(5):
    print("")
    for j in range(5-i):
        print("*", end="")
print("\n===============")

# 별찍기4
for i in range(4):
    print("")
    for j in range(3-i):
        print(" ", end="")
    for k in range(i*2+1):
        print("*", end="")
print("\n===============")

# 별찍기5
for i in range(3):
    print("")
    for j in range(2-i):
        print(" ", end = "")
    for k in range(i*2+1):
        print("*", end="")
for i in range(2):
    print("")
    for j in range(1+i):
        print(" ", end = "")
    for k in range(3-i*2):
        print("*", end="")