factorial = int(input("숫자를 입력하세요 >>"))
f = 1
for n in range(factorial):
    f *= n+1

print(f)