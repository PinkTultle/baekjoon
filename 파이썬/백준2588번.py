'''세 자릿수의 곱셈에서 세자리 자연수가 주어질때 연산과정에서 나오는 값들을 출력하시오'''


A = int(input())
B = int(input())

B_1 = B%10
B_10 = (B/10)%10
B_100 = B/100


print(A * B_1)
print(A * int(B_10))
print(A * int(B_100))
print(A*B)