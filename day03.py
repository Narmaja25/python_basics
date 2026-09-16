#Arithmetic Operators (+, -, *, **, /, //, %)
#+
a = 2+2
print(a)
b = [1,2,3,] + [4,5,6,]   #this method is concatenation(union) of two lists
print(b)
#-e
a = 4-3
print(a)
b = {1,2,3} - {1,3}
print(b)
#*
a = 5*2
print(a)
#**
a = 2**10
print(a)
#/
a = 5/2
print(a)
#//   #floor division or integer
a = 10//2
print(a)
#%
a = 10%5
print(a)

#Relation operators (==, !=, >, >=, <, <=)
a = 5 == 6
print(a)
b= 5!= 6
print(b)
c = 5>7
print(c)
d = 5>= 7
print(d)
e = 5<7
print(e)
f = 5<= 7
print(f)

#logical operators (and, or, not)
a  = 1 and 1 and 'Prasad'
print(a)
b = 0 or 1 or 'Prasad'
print(b)
c = not False
print(c)

#Assignment operators (=, +=, -=, *=, /=, %=, //=, **=)
a = 500   #a = a*20
a*= 20
print(a) 

#Identity operators (is, is not)
a = 6
b =6
print(a is b)

#Membership operators (in, not in)
a = 'P' in 'Prasad'
print(a)
# 