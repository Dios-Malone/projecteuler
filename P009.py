import math

def solution():
   for c in range(500, 1, -1):
      for a in range(500):
         for b in range(500):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
               print("a={}, b={}, c={}".format(a,b,c))
               return a*b*c
               
print('Solution 1 result: {}'.format(solution()))
   