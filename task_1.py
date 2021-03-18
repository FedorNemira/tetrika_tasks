


def task(array): 

  for i in range(len(array)-1):

    if array[i] != array[i+1]:
      return i+1

    else:
      continue

  return f'array:{array} have a similar elements'

  
  
print(task('111111111111111111111111111111111111111111k111121')) 

print(task('1111111111111111111111555')) 

print(task('aaaaaaaabbbbbb')) 


#Сложность O(n)