'''Datatypes --> It will tell us how ti define the data
types :
Numeric datatypes: INT,FLOAT,COMPLEX
Boolean type: True/flase
None type: none
Sequences types : strings,lists,frozensets,sets,mapping(dictionaries)
#numeric datatype --> quantities,ids,order ids,stock,age -->int
age = 32
print(age)
print(type(age))
stock = 35
print(type(stock))
batch_rank = 1
print(batch_rank)
# flaot values --->salaries,price,percentage calculations,temp
salary = 40000.00
print(salary)
print(type(salary))
#complex--> real and imaginary values --> scitific calculations,signal processing
#data = 3+5i we cannot define with i it raises syntax error
#data = 3+j5 it defines name error ..j refers to default imaginary letter
data = 3+5j
print(data)
print(type(data))
#boolean --> true/false: used for validations
access = True
print(type(access))
result = False
print(type(result))
#Nonetype --->None :0,False,"",[],{},(),set()
branch_rank = None
print(type(branch_rank))
#typeConversion: Converting one datatype into another datatype
#explicit conversion
rank = 5
print(type(rank))
b= float() # 0.0
b= float(rank) #5.00
print(b)
print(type(b))
c = complex() # 0j
c = complex(rank)# 5+0j
print(c)
d = bool()#false
print(d)
d = bool(rank)# bool(value) is true ,bool(empty_value) is false
print(d)
#int() -->0
#bool(['']) -->true
#bool(None)-->false
#bool([])--> false
#bool([0]) --> true
#bool(' ')--> True
#flaot --> integer,complex,boolean
salary = 5500.25
print(salary)
print(type(salary))
a = int(salary)
print(a)
print(type(a))
b = complex(salary)
print(b)
print(type(b))
c = bool(salary)
print(c)
print(type(c))
#complex --> int,float,bool
signal = 5+6j
print(signal)
#a = int(signal)
#print(a)#TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#b=float(signal)
#print(b) #TypeError: float() argument must be a string or a real number, not 'complex'
c = bool(signal)
print(c)
# boolean ---> int,float,complex:True-->1,false-->0
a = True
b = int(a)
print(b)#1
c = float(a)
print(c) # 1.0
d = complex(a)
print(d) # 1+0j
print(bool(a))#True
e =int(float(bool(5))) # 1
print(e)
f = bool(float(int(35)))#true
print(f)
c = True+35+3.5+(6+5j) # true becomes 1
print(c)#(45.5+5j)
#a =None+True+1 #TypeError: unsupported operand type(s) for +: 'NoneType' and 'bool'
#print(a)
#sequence Types --->strings,lists,frozensets,sets,mapping(dictionaries)
#strings -->group of characters
#quotations --->single,double,triple quotes
name = 'Nikitha'
place = 'vizag'
print(name)
print(place)
# strings are immutable,ordered,indexed,collectiom
print(len(name))#-->7 #returns the number of items in a collection
print(len(place))#ans = 5
print(len('qwerty')) # 6
print(len('kandrapu nikitha')) # space is also a character it is counted has indexed
#a = '' --> len -->0
#a= ' ' --> len(a) --> 1
#string cannot be converted into int,float,complex it rasises a value error but string can be used with bool
course = 'Python'
#print(int(course))#ValueError: invalid literal for int() with base 10: 'Python'
#print(float(course))#ValueError: could not convert string to float: 'Python'
#print(complex(course))#ValueError: complex() arg is a malformed string
print(bool(course))#true'''
# int can be converted into numeric string
data = 56
b = str(data)#converted to str
print(b)
mileage = 13.5
c = str(mileage)
print(c)
d = str(3+5j)
print(d)
e = str(True)
print(e)






