# 수 N개가 주어졌을때 i번째 수에서 j번째 수까지의 합
# 구간합 구하는 공식 : i~j까지의 합 =  S[j] - S[i-1]  마지막인덱스까지의 합 - 시작인덱스-1까지의 합
import sys
input = sys.stdin.readline
suNo,quizNo = map(int,input().split())
numbers = list(map(int,input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    print('i',i)
    temp=temp+i
    print('temp',temp)
    prefix_sum.append(temp)
    print('대상배열 초본',prefix_sum)
print('대상배열 최종',prefix_sum)


for i in range(quizNo):
    s,e = map(int,input().split())
    print(prefix_sum[e]-prefix_sum[s-1])




