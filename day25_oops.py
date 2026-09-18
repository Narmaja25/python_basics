#Class
class Calculator:
    #class variable
    brand = 'Casio'
    def __init__(s, a, b):
        #instance variables
        s.a = a 
        s.b = b 
    #instance method
    def add(s):
        return s.a + s.b 
    #class method
    @classmethod 
    def sub(c, a, b):
        return a-b 
    #static method
    @staticmethod 
    def mul(a, b):
        return a*b
calc1 = Calculator(10,20)
calc2 = Calculator(100,200)

#searching. any type of variable or method searching from object to class
print('Searching')
print(calc1.a)       #10
print(calc2.b)       #200
print(calc1.add())   #30
print(calc2.add())   #300
print(calc1.brand)   #Casio
print(calc2.brand)   #Casio
print()

#Dynamic 
print('Python classes and objects are dynamic')
#add c variable to calc1
calc1.c = 30         
# print(Calculator.c)  #error
print(calc1.c)       #30
# print(calc2.c)       #error
#add version variable to Calculator class 
Calculator.version = 2 
print(Calculator.version)  #2
print(calc1.version)       #2
print(calc2.version)       #2
print()

#__dict__
print('__dict__')
print(Calculator.__dict__)
print(calc1.__dict__)
print(calc2.__dict__)
print()

#create varaibles: 
# Class varisbles are created with Classname.variable anywhere in program, only variable in class outside methods
# Instance variables are created with obj.variable anywhere in program
print('Creating variables')
Calculator.build = 'A'
calc1.d = 400 
calc2.e = 500 
print(Calculator.__dict__)
print(calc1.__dict__)
print(calc2.__dict__)
print() 

#update variables
# Calss variables are updated with Classname.existingvariable = value anywhere in program
# Instance variables are updated with obj.existingvariable = value anywhere in program
print('Updating variables')
Calculator.build = 'B'
calc1.d = 4000
calc2.e = 5000
print(Calculator.__dict__)
print(calc1.__dict__)
print(calc2.__dict__)
print()


#delete variables 
# Class variables are deleted with del classname.variable 
# Instance variables are deleted with del obj.variable
print('Deleting variables')
del Calculator.build
del calc1.d 
del calc2.e 
print(Calculator.__dict__)
print(calc1.__dict__)
print(calc2.__dict__)
print()

#Instance method 
print('Intance method calling: ')
print(calc1.add())                 #with object(will pass object as 1st arg)
# print(Calculator.add('rakesh'))    #with class(will not pass object)
print(Calculator.add(calc1)) 
print()

#Class method 
print('Class method calling:  ')
# print(calc1.sub())
# print(Calculator.sub())
print(calc1.sub(20,10))       #with object (will pass class as 1st arg)
print(Calculator.sub(20,10))  #with class  (will pass class as 1st arg)
print()

#Static method 
print('Static method calling')
# print(calc1.mul())
# print(Calculator.mul())
print(calc1.mul(10,20))      #with object (will not pass first arg)
print(Calculator.mul(10,20)) #with class (will not pass first arg)