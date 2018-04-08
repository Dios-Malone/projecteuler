import math

def largest_p_num(boundary):
   dig_array = list(str(boundary))
   length = len(dig_array)
   mid = (length+1)//2
   is_reduced = False
   for i in range(mid):
      if dig_array[i] > dig_array[-i-1] and not is_reduced:
         for k in range(1, mid):
            if dig_array[mid-k] == '0':
               dig_array[mid-k] = '9'
            else:
               dig_array[mid-k] = str(int(dig_array[mid-k])-1)
               is_reduced = True
               break
      dig_array[-i-1] = dig_array[i]
   return int(''.join(dig_array))
   
   
def listfactorpairs(num):
   factors = []
   sqrt = int(math.sqrt(num))
   for i in range(100, sqrt+1):
      if num%i==0:
         factor2 = num//i
         if factor2 > 99 and factor2 < 1000:
            factors.append((i, factor2))
   return factors
   
   
   
def solution(boundary):
   factorpairs = None
   p = boundary + 1
   p = largest_p_num(boundary)
   while not factorpairs and p > 9999:
      p = largest_p_num(p-1)
      factorpairs = listfactorpairs(p)
   if factorpairs:
      print(factorpairs)
      return p
   else:
      return None

print('Solution 1 result: {}'.format(solution(999*999)))
      
   
         
          