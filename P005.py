import math

def isprime(num):
   assert isinstance(num,int)
   sqrt = int(math.sqrt(num))
   if num==2:
      return True
   elif num%2==0:
      return False
   else:
      for n in range(3, sqrt+1, 2):
         if num%n==0:
            return False
   return True
         
def solution(boundary):
   result = 1
   for num in range(2, boundary+1):
      if isprime(num):
         e = 2
         while math.pow(num, e) <= boundary:
            e += 1
         e -= 1
         result *= int(math.pow(num, e))
   return result
   
print('Solution 1 result: {}'.format(solution(20)))