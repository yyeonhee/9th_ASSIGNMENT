list=[]
sum=0
for i in range(7):
    print(i, end="")
    n=int(input("번째 상품 가격: "))
    sum+=n
    list.append(n)
print(list)

price=int(input("가지고 있는 돈을 입력하세요 >> "))
if price<sum:
    print("돈이 모자랍니다. ", end="")

i=0
while(True):
    price-=list[i]
    if(price<0):
        break
    i+=1
print(f"{i}개의 상품을 샀습니다.")