# #Constructor 
class Calculator:
    def __init__(s, a, b):    #can take any number of args
        s.a = a 
        s.b = b 
        return None          #can only return None
#implicit call
calc1 = Calculator(10,20)  #initialises values
#explicit call
# calc2 = Calculator.__init__(10,20) 
calc3 = Calculator.__init__(calc1, 100,200)  #modifies values and return None
print(calc3)     
print(calc1.a)   
print(calc1.b)  
print()


# #Destructor 
class Calculator:
    def __init__(s, a, b):
        print('Constructor')
        s.a = a 
        s.b = b 
    # def __del__(s, a, b):      #except self, no other variables 
    #     print('Destructor')
    def __del__(s, a=10, b=20):    
        print('Destructor')
        return 'rakesh'          #can return anything
calc1 = Calculator(1,2)     
calc1 = Calculator(10,20)   
explicit = calc1.__del__()   
print(explicit)


#  #objects cannot be created in constructor and destructor, infinite recursion
class Calculator:
    def __init__(s):
        print('Constructor')    
    def __del__(s):
        print('Destructor')
        Calculator() 
calc1 = Calculator() 



#private variables and methods 
class Calculator:
    brand = 'Casio'        #public 
    __version = 2          #private 
    def __init__(s, a, b):
        s.a = a            #public 
        s.__b = b          #private 
    def display(s):        
        print(brand)               #NameError: name 'brand' is not defined / not found
        print(Calculator.brand)    
        print(Calculator.version)
        print(Calculator.__version)  #Classname.__variable
        print(s.a)
        print(s.b)
        print(s.__b)                 #obj.__variable
    def __add(s):            #private method
        return s.a + s.__b  
calc1 = Calculator(10,20)
calc1.display()
print(Calculator.__version)
print(Calculator._Calculator__version)  #Classname._Classname__variable
print(calc1.a)
print(calc1.__b)
print(calc1._Calculator__b)             #obj._Classname__variable
print(calc1.add())
print(calc1.__add())
print(calc1._Calculator__add())         #obj._Classname__method()


#property methods: getter, setter and deleter 
class Person:
    def __init__(s):
        s._age = None 
    @property 
    def age(s):
        print('Property method')
        return s._age    
    @age.setter 
    def age(s, age):
        print('Setter Method')
        if age > 18:
            s._age = age 
        else:
            raise ValueError('Age must be greater than 18')
    @age.deleter 
    def age(s):
        print('Deleter Method')
        del s._age  
person1 = Person() 
print(person1.age)
person1.age = 45
print(person1.age) 

#deleter method executes only when explicitly called
del person1.age 
print()

#cannot call methods explicitly (no attribute _age)
print(person1.age(50)) #we can't call the person age Explicitly
print(person1.age())
print(person1.age())
print()

#property function
class Person:
    def __init__(self):
        self._age = None
    def get_age(self):
        print('Get age method')
        return self._age
    def set_age(self, value):
        print('Set age method')
        if value >= 0:
            self._age = value
    def delete_age(self):
        print('Delete age method')
        del self._age
    age = property(get_age, set_age, delete_age)
person1 = Person() 
print(person1.age)
person1.age = 45
print(person1.age) 
#deleter executes only when explicitly called
del person1.age 
print()
#can call methods explicitly
print(person1.set_age(50))
print(person1.get_age())
print(person1.delete_age())
print()
        
#attribute functions: getattr, setattr, hasattr
class Calculator:
    brand = 'Casio'
    def __init__(s, a, b):
        s.a = a 
        s.b = b 
calc1 = Calculator(10,20)
print(getattr(Calculator, 'brand'))
# print(getattr(Calculator, 'version'))  #error
print(getattr(calc1, 'a'))
print(getattr(calc1, 'brand'))
print(setattr(Calculator, 'version', 2))
print(getattr(Calculator, 'version'))
print(setattr(Calculator, 'version', 3))
print(getattr(Calculator, 'version'))
print(setattr(calc1, 'c', 2))
print(getattr(calc1, 'c')) 
print(hasattr(Calculator,'version'))
print(hasattr(Calculator, 'a'))
print(hasattr(calc1, 'a'))
print(hasattr(calc1, 'version'))

#Inner class 
class Car:
    class Engine:
        def sound(s):
            print('Wrooom')
engine1 = Car.Engine()
engine1.sound()
car1 = Car() 
engine2 = car1.Engine() 
engine2.sound()


#sys.getrefcount 
import sys 
l = [1,2,3,4]
a = b = c = l 
print(sys.getrefcount(l))
i = 1 
x = y = z = i 
print(sys.getrefcount(i))

# dir() function 
class Calculator:
    brand = 'Casio'
    def __init__(s, a, b):
        s.a = a 
        s.b = b 
    def add(s):
        return s.a + s.b 
print('Module:   ', dir())
print('Class:   ', dir(Calculator))
print('Object:   ', dir(Calculator(10,20)))

