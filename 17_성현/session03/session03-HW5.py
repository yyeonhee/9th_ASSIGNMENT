'''
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''
problem = {}
problemst = 0
correctnum = 0
plusscore = 2
score = 0
problemcount = int(input())
for problemnum in range(problemcount):
    problem[problemnum] = input()
while(correctnum!=problemcount):
    for correct in str(problem[correctnum]):
        if(correct=='O' and problemst==1):
            score+=plusscore
            plusscore+=1 
            problemst=1
            print(score)
        elif(correct=='O' and problemst==0):
            score+=1
            problemst=1
            print(score)
        elif(correct=='X'):
            problemst=0
            plusscore=2
            print(score)
    print(score)
    score=0
    correctnum+=1 