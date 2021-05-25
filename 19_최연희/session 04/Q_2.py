# 빈 리스트 생성
example =[]
num = 0

for i in range(5):
    # 임의의 리스트 k생성
    k = []
    for j in range(5):
        k.append(j+num)
    num += 5
    # 임의 리스트 k를 맨 처음에 생성한 빈 리스트에 추가해줌
    example.append(k)

# 첫번째, 세번째 열을 출력하기 위함
print([[i[1], i[3]] for i in example])