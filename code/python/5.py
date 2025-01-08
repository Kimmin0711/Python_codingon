'''# 이차원 리스트
matrix = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
]
print(matrix)
print(matrix[0])  # 첫번째 행
print(matrix[1])  # 두번째 행
print(matrix[2])  # 세번째 행

print(matrix[0][0])
print(matrix[1][2])

# 요소 추가
matrix[1] = matrix[1] + [99]
print(matrix)

# 행 추가
matrix = matrix + [[10, 11, 12]]
print(matrix)

# 요소 수정
matrix[0][0] = 100
matrix[1][1] = 5000
print(matrix)

# 행 삭제
del matrix[2]
print(matrix)

# 행 개수
rows = len(matrix)
print(rows)
'''

'''# 이차원 메서드
matrix = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
]

# 요소 추가
matrix[0].append(10)
print(matrix)

# 행 추가
matrix.append([10, 11, 12])
print(matrix)

# 요소 삽입
matrix[1].insert(1, 100)
print(matrix)

# 행 삽입
matrix.insert(2, ["안녕", "반가워", "어서와"])
print(matrix)

# 리스트 확장
matrix[0].extend([11, 12])
print(matrix)
'''

#퀴즈. 3차원 리스트에서 인덱싱을 이용해 아이스크림 문자열 만들기
words = [
    [["마", "크"], ["구", "이"]],
    [["피", "아"], ["림", "차"]],
    [["스", "사"], ["나", "가"]],
]
value = words[1][0][1] + words[0][1][1] + words[2][0][0] + words[0][0][1] + words[1][1][0]
print(value)