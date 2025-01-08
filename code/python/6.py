# 튜플, Tuple
t1 = (1,)  # 요소가 1개인 튜플은 반드시 쉼표 사용!
print(t1)
not_tuple = (1)
print(not_tuple)  # 쉼표 사용 안했을 시 정수로 나옴

t2 = (1, 2, 3, 4, 5, 3, 3, 3)  # 괄호를 사용해 튜플 선언
print(t2)

t3 = 1, 2, 3  # 괄호 생략 가능
print(t3)

t4 = ("a", "b", "c", ("안녕", "잘가"))  # 문자값 가능. 튜플안에 튜플 가능
print(t4)

print(t1[0])
print(t2.count(3))
print(t3.index(2))
print(t4[3][0])
print(t4[:2])

print("d" in t4)  # False: d라는 요소가 t4에 있나요?
print(2 in t2)  # True

# t4[0] = "x"
# TypeError: 'tuple' object does not support item assignment