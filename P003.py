import math
def isprime(i):
   assert isinstance(i,int)
   sqrt = int(math.sqrt(i))
   if num==2:
      return True
   elif i%2==0:
      return False
   else:
      for n in range(3, sqrt+1, 2):
         if i%n==0:
            return False
   return True

def listfactors(num):
   assert isinstance(num,int)
   sqrt = int(math.sqrt(num))
   factors = []
   for i in range(1, sqrt+1):
      if num%i==0:
         factors.append(i)
         factors.append(num//i)
   return factors
   
def solution(input):
   factors = listfactors(input)
   factors.sort(reverse=True)
   for num in factors:
      if isprime(num):
         return num
print('Solution 1 result: {}'.format(solution(600851475143)))