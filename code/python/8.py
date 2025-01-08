# 딕셔너리(dictionary)

# 빈 딕셔너리 생성
# dict1 = {}
dict1 = dict()
print(dict1)

# 딕셔너리 생성
dict1 = {
    "name" : "홍길동" ,
    "age" : 20,
    "city" : "Seoul",
    "hobby" : ["런닝", "등산", "헬스"]
}
print(dict1)

dict2 = dict(name="홍길동", age="21")
print(dict2)

#값 접근하기
print(dict1["name"])
print(dict1["age"])
print(dict1["hobby"][2])

# 값 수정
dict1["age"] = 30
print(dict1)

# 요소 추가
dict1["birtday"] = "19900101"
print(dict1)

# 키 삭제
del dict1["birtday"]
print(dict1)

# 딕셔너리 메서드
fruits = {
    "apple": "사과",
    "banana": "바나나"
}
print(fruits.get("apple"))
print(fruits.get("peach"))
# 존재하지 않는 키로 get 하는 경우 'None' 반환
print(fruits.get("peach", "복숭아"))
# None 대신 복숭아로 출력
print(fruits)
# 기본값을 설정할 뿐, 딕셔너리 요소 추가x

#여러 요소 추가
fruits.update({
    "grapes": "포도",
    "melon": "멜론"
})
print(fruits)
print(fruits.keys())
print(fruits.values())
print(fruits.items())

# 요소 모두 지우기
fruits.clear()
print(fruits)

# 실습. 성적관리
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 95
}
students["David"] = 80
students["Alice"] = 88
del students ["Bob"]
print(students)