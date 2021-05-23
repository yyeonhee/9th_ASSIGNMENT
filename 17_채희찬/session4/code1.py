change = 1000-int(input())   # 거스름돈
coinCount = 0   # 동전 개수

# 500엔 체크
if change >= 500:   # 입력이 1000엔 미만이기 때문에 while이 아닌 if로 체크한다.
    coinCount += 1
    change -= 500

# 100엔 체크
while change >= 100:
    coinCount += 1
    change -= 100

# 50엔 체크
while change >= 50:
    coinCount += 1
    change -= 50

# 10엔 체크
while change >= 10:
    coinCount += 1
    change -= 10

# 5엔 체크
while change >= 5:
    coinCount += 1
    change -= 5

# 1엔 체크
while change >= 1:
    coinCount += 1
    change -= 1

# 동전 개수 출력
print(coinCount)