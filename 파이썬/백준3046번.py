'''첫번째 숫자 A와 평균 S를 입력받아 (A+B)/2=S에서 B를 구하는 문제'''

A, S = map(int,input().split())

B = S*2-A

print(B)