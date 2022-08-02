'''세 정수를 입력받은 다음, 나머지들을 출력하는 프로그램'''

A,B,C = map(int,input().split())

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
