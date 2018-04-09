import math
def isprime(num):
   assert isinstance(num,int)
   sqrt = int(math.sqrt(num))
   if num==1 or num ==0:
      return False
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
   sum = 0
   for i in range(boundary+1):
      if isprime(i):
         sum += i
   return sum

def solution2(boundary):
   numlist = [True] * (boundary+1)
   numlist[0] = False
   numlist[1] = False
   sqrt = int(math.sqrt(boundary))
   for i in range(2, sqrt):
      if numlist[i]:
         k = 0
         while i**2 + k*i < boundary:
            numlist[i**2 + k*i] = False
            k += 1
   return sum([i for i in range(len(numlist)) if numlist[i] is True])
print('Solution 1 result: {}'.format(solution(2_000_000)))
print('Solution 2 result: {}'.format(solution2(2_000_000)))

