# list = [4, 3, 2, 5, 6]
#print elements in list with for each loop
numbers = [4, 3, 2, 5, 6,]
print(numbers)
print()
print()

#print elements in list with index based for loop
for x in range(len(numbers)):
    print(numbers[x])
#skip printing even numbers in list
numbers = [4, 3, 2, 5, 6,]
for x in numbers:
    if x % 2 ==0:
        continue
        print(x, end=' ')
        print()
        print()
        
#skip printing odd numbers in list
#when number 2 comes stop printing  
for x in numbers:
    if x % 2==1:
        continue
        print(x, end=' ')
#when number 2 comes stop printing 
for x in numbers:
    if x ==2:
        break
    print(x)
 
#when first odd number comes stop printing
for x in numbers:
    if x % 2==1:
        break
        print(x)
#print numbers from 1 to 10, when all numbers are printed, print 'All numbers printed'
#print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All numbers printed'
#print numbers from 10 to 1, when 5 comes stop printing, when all numbers are print, print 'All numbers printed'
for x in range(1,11):
    print(x)
else:
    print('all numbers are printed')

#print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All numbers printed'
for x in range(1,11):
    if x % 2 ==0:
        continue
    print(x)
else:
    print('All numbers printed')

numbers: list[int] = [4, 3, 2, 5, 6]
for x in numbers: # it is not Iterable object
    print(x)
#print numbers from 10 to 1, when 5 comes stop printing, when all numbers are print, print 'All numbers printed'
for x in range(10, 0, -1):
    if x == 5:
        break
    print(x)
    for x in range(len(numbers)):
        print(numbers)
        
#skip printing even numbers in list
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
#skip printing odd numbers in list    
for i in range(10): # skip printing odd numbers in list
    if i % 3 == 0:
        continue
    print(i)
#when number 2 comes stop printing  
for i in range(1 ,5):
    if i % 3 == 0:
        print(i)
#when first odd number comes stop printing        
for i in range(1 ,4):
    if i % 4 == 0:
        print(i)
        
    
else:
    print('All numbers printed')