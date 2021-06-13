buy = int(input())      # 구매 금액
n = 1000 - buy          # 거스름돈

list = [500, 100, 50, 10, 5, 1]     # 거스름돈으로 줄 동전 리스트(최소로 줘야 하기 때문에 금액이 큰 순서대로 정렬.)
count = 0                           # 거스름돈으로 줄 동전 개수

for i in list:
    count = count + ( n // i )          # 거스름돈을 리스트에 있는 동전(가장 큰 순서)으로 나눈 (소수점을 제외한)몫을 동전 개수(count)에 적립한다.
    n = n % i                           # 거스름돈을 리스트에 있는 동전(가장 큰 순서)으로 나눈 나머지 값으로 바꾸고, 이 과정을 리스트에 있는 모든 동전을 거칠 때까지 반복한다

print(count)            # 거슬러 줘야 하는 동전의 개수 출력