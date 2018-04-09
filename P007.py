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
   
def solution(input):
   count = 0
   cur = 2
   while count < input:
      if isprime(cur):
         count += 1
      cur += 1
   return cur -1
  
  
print('Solution 1 result: {}'.format(solution(10001)))