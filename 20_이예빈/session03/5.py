# 연속된 O의 개수 == 문제

# result="OOXXOXXOOO"
result=input("OX퀴즈의 결과 입력 >> ")
sum=0
cnt=0

for i in result:
    if(i=='O'):
        cnt+=1
        sum+=cnt
    else:
        cnt=0

print(f"총점은 {sum}")