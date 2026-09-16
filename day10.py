list = [4, 3, 2, 5]
for x in list:    #for x in [4, 3, 2, 5]
    print(x)       #4 3 2 5 
    for x in range(len(list)): # for x in range(4)  #0 1 2 3 4
    
        print(x, list[x]) #0 3

#print elements in list with for each loop
my_list = [4, 3, 2, 5]
for x in my_list:
    print(x)

#print elements in list with index based for loop
for i in range(len(my_list)):
    print(i, my_list[i])

#print elements in list with while loop
i = 0
while i < len(my_list):
    print(i, my_list[i])
    i += 1

#skip printing even numbers in list
for x in my_list:
    if x % 2 == 0:
        continue
    print(x)

#skip printing odd numbers in list
for x in my_list:
    if x % 2 != 0:
        continue
    print(x)

#when number 2 comes stop printing  
for x in my_list:
    if x == 2:
        break
    print(x)

#when first odd number comes stop printing
for x in my_list:
    if x % 2 != 0:
        break
    print(x)

#print numbers from 1 to 10, when all numbers are printed, print 'All numbers printed'
for i in range(1, 11):
    print(i)
else:
        print('All numbers printed')

#print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All numbers printed'
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
else:
    print('All numbers printed')

#print numbers from 10 to 1, when 5 comes stop printing, when all numbers are print, print 'All numbers printed'
for i in range(10, 0, -1):
    if i == 5:
        break
    print(i)
else:
    print('All numbers printed')
