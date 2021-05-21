put=int(input("상품 가격: "))
exchange=1000-put

coin500 = exchange//500
exchange = exchange % 500
coin100 = exchange//100
exchange = exchange % 100
coin50 = exchange//50
exchange = exchange % 50
coin10 = exchange//10
exchange = exchange % 10
coin5 = exchange//5
exchange = exchange % 5
coin1 = exchange//1
exchange = exchange % 1

sum = coin500+coin100+coin50+coin10+coin5+coin1

print(sum)