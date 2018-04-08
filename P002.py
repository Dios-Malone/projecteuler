def solution(boundary):
   i1 = 1
   i2 = 2
   sum = 0
   while i2 <= boundary:
      if i2%2==0:
         sum += i2
      i0 = i1
      i1 = i2
      i2 = i0 + i1
   return sum
   
print('Solution 1 result: {}'.format(solution(4000000)))