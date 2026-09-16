#String Methods (String is immutable)

a='Narmaja'
print(a)
b='Narmaja'
print(b)
c='''Nar
  ma
 ja'''
print(c) 

#delete
a=' Narmaja ' 
print(a.strip())
print(a.lstrip())
print(a.rstrip())

#update # replace
a=('Narmaja is a hard worker', 'Narmaja is smart', 'Narmaja is a Monster') #error: 'tuple' object has no attribute 'replace'
print(a)
#b=a.replace('Narmaja','Monster',1)
#print(b)
#b=a.replace('Narmaja','Monster',1)
#c=b.lower()
#print('lower: ',c)
#d=b.upper()
print('upper: ',d) #name error: name 'd' is not defined,if not specified it will replace all occurences
e=b.swapcase()
print('swapcase: ',e)
f=b.title()
print('title: ',f)
g=b.capitalize()
print('capitalize: ',g)

#Read
a='Prasadkumar'
print(a.count('a'))
print(a.index('r'))
print(a.index('d',4))
print(a.index('a', 3 ,10))
print(a.rindex('d'))
print(a.rindex('m', 8))
print(a.rindex('a',3 ,10))

#find 
a='Prasadkumar'
print(a.count('a'))
print(a.find('p'))
print(a.find('d',4))
print(a.find('w', 3 ,10))
print(a.rfind('n'))
print(a.rfind('m', 8))
print(a.rfind('q',3 ,10))
# other 
a='s'
b=' a'
print(a.isspace())
print(b.isspace())

a='abcD'
print(a.isalpha())
b='prasad1'
print(b.isalpha())
c='pras@d'
print(c.isalpha())
a='2002'
print(a.isdigit())
b='02a'
print(b.isdigit())
a='abc123'
print(a.isalnum())
b='abc#12'
print(b.isalnum())
a='123$'
print(a.islower())
b='23%ua'
print(b.islower()) #if no uppercase and atleast one lowercase return true else false

a='23@u'
print(a.isupper())
b='23@A'
print(b.isupper()) #if no lowercase and atleastnone uppercase returns true else false

#split
a='Prasad'
print(a.split('n'))
b= '  '
print(b.split(' '))

# join
a='%'
print(a.join(a))
d={'3':1, '2':1, '1':1}
print(a.join(d))
#