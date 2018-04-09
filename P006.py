import math

def solution(boundary):
   sum = 0
   sumofsquare = 0
   for i in range(1, boundary+1):
      sum += i
      sumofsquare += int(math.pow(i, 2))
   return int(math.pow(sum, 2)) - sumofsquare
   
print('Solution 1 result: {}'.format(solution(100)))