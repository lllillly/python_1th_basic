# 문제 1
s = "hello"
t = "python"
print(f"{s}! {t}")

# 문제 2
movie_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "럭키", "배트맨"]

movie_rank.remove("럭키")
print(f"{movie_rank}")

# 문제 3
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "GO", "C#"]

langs = lang1 + lang2

print(langs)

# 문제 4
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "간장치킨", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(len(cook))

# 문제 5
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)


# 문제 6
for i in range(4):
    result = i * 10

    if result == 0:
        print("+++++")
    else:
        print(result)

# 문제 7
year = list(range(2002, 2050, 4))
print(year)

for i in range(2002, 2050, 4):
    print(i)

# 문제 8
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

# 문제 9
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}

print(inventory)

# 문제 10
icecream = {"탱크보이": 1200, "폴라포": 1200, "빵빠레": 1800, "월드콘": 1500, "메로나": 1000}

result = sum(icecream.values())

print(result)
