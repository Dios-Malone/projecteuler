import math

def solution():
   for c in range(500, 1, -1):
      for a in range(1, 500):
         b = 1000 - c - a 
         if a + b + c == 1000 and a**2 + b**2 == c**2 and a != b and b!=c:
            print("a={}, b={}, c={}".format(a,b,c))
            return a*b*c
               
print('Solution 1 result: {}'.format(solution()))
   