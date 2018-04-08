
def multiple_of_3or5(boundary):
   sum = 0
   for i in range(boundary):
      if i%3==0 or i%5==0:
         sum += i
   return sum
   
print('Solution 1 result: {}'.format(multiple_of_3or5(1000)))


def solution2(boundary):
   return sumof_multipleof(3, boundary) + sumof_multipleof(5, boundary) - sumof_multipleof(3*5, boundary)

def sumof_multipleof(num, boundary):
   max_multiple = boundary - 1
   while max_multiple % num != 0:
      max_multiple -= 1
   num_of_items = max_multiple // num
   return (num + max_multiple) * num_of_items // 2
print('Solution 2 result: {}'.format(solution2(1000)))