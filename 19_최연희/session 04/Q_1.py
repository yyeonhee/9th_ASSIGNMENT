list = [500,100,50,10,5,1]
money = int(input())
price = 1000
result = price - money

# 거스름돈 개수
count = 0

# 리스트에 있는 잔돈의 개수만큼 반복문 실행
for i in list:
    count += result // i
    result %= i

print(count)