# 내장 함수
numbers = [10, 20, 30, 40]
print(sum(numbers))

scores = {
    "국어": 83,
    "수학": 95,
    "영어": 90
}
print(scores.values())
total_score = sum(scores.values())
print(total_score)

print(max(numbers))
print(min(numbers))

print(max(scores.values()))
print(min(scores.values()))

names = ["Alice", "Bob", "Charlie", "Lily"]
scores = [85, 90, 95, 100, 105]
zipped = list(zip(names, scores))
zipped2 = dict(zip(names, scores))
print(zipped)
print(zipped2)
# 짝이 안 맞는 값은 버리고 출력
