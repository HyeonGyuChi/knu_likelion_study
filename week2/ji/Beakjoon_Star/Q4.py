''' By HyeonGyu
BAEKJOON STAR / 백준 별찍기
https://www.acmicpc.net/workbook/view/20

Q4
*****
 ****
  ***
   **
    *
'''

num = int(input())

for i in range(1, num+1) :

    for k in range(1, i) :
        print(" ", end ="")

    for j in range(i, num+1) :
        print("*", end = "")

    print()

''' O(n)'''
for i in range(num, 0, -1) :
    print(' '* (num - i), end = '')
    print('*' * i)