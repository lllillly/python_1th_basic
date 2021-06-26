# 아스키코드
# String -> Char의 배열

text = "Hello world"

upper_cnt = 0
lower_cnt = 0

for t in text :
    if(int(ord(t)) >= 65 and int(ord(t)) <= 90) :
        upper_cnt += 1
    if(int(ord(t)) >= 97 and int(ord(t)) <= 122) :
        lower_cnt += 1

    # 대문자 : 65 ~ 90
    # 소문자 : 97 ~ 122

print(f"기준데이터 : [{text}]")
print(f"대문자의 총 개수 : {upper_cnt}")
print(f"대문자의 총 개수 : {lower_cnt}")