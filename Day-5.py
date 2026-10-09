'''Operators ---> operators help us to perform operations between operands
1.Arithmetic---->+,-,*,/(float),**,//(quotient(integer value)),%(reminder)
2.Assigment operators-->It hepls us to assign,update(increment),decrement values
#=(assigning),+= (Addition and assign),-=(Subtraction&assign),*=(Multiplication & Assign)
/=,//=,**=,%=

data = 20
print(data)
print(type(data))

stock = data
print(stock)

#Increment the value of stock
stock = stock + 5 #20+5 -->stock+=5
print(stock)#25
data-=2 # 20-2=18
print(data)
data *= 2 #36
print(data)
data /=2 #18.0
print(data)
data//=2 #9-->18/2
print(data) #---> 9/2
data%=2 #1.0
print(data)

#comparision operators(relational Opearators)--->it performs comparision between the operands and
#results in boolean(true/false)--->conditions
#==,!=,<,<=,>,>=
name = 'nikitha'
attendance = 75
print(attendance>=80)#False
print(attendance==80)#False
print(attendance<=80)#true
print(attendance<80)#true
print(attendance>80)#false
print(attendance!=80)#true

#Logical operators ---> and ,or,not
#and : it needs all conditions to be satisfied(two or more)
#or :it needs any one condition to be satified, only used for numbers
#not : opposite to existing ,can used for everything
max_marks = 80
vinay_marks = 75
max_att = 75
vinay_att = 70
vinay_marks+=10
#certificate = vinay_marks >= max_marks and vinay_att>= max_att
#print(certificate)#False
chance =  vinay_marks >= max_marks or vinay_att>= max_att
print(chance)#true
data = []
print(not(data))# --> gives true
data = [1,2,3]
print(not(data)) #---> gives false as data exists
#comparison and logical operators returns result in boolean
#membership operators --> in,not in
#check for the exisiting in a sequence (str,list,set,tuple,dict)
names = ['nikitha','deepthi','gowthami','mamatha']
name = 'ajay'
print(name in names) # returns false
print(name not in names) #returns True
print('12' in '121') # true
print(12 in 121) # TypeError: argument of type 'int' is not iterable
print('ajay' in 'ajay') # returns True as we checking type as string
print(['ajay'] in ['ajay']) # returns false as it is a list
#identity Operators --> it is speicfically refers to the object memory location
#id --->is,is not
#if a and b has same values for integers only it  stored same memory location
a = 15 # python points to same memory location when values as same
b = 15
print(a==b)#true
print(id(a))
print(id(b))
c = a
print(id(a))
print(c is a) # memory location of a and c are same so it gives to true
e = [1,2,3,4] # e and f are not referencing to same object
f = [1,2,3,4]
print(e==f) # True
print(id(e))
print(id(f))
# as we have taken two lists eventhroug with similar values identity is false
print(e is f) # false
c = e
print(id(c))
print(c is e) # true as we directly assing same object
a = (1,2,3)
b = (1,2,3)
print(id(a))
print(id(b))
print(a is b) 
#when we check with the Interpreter mode and scripting mode above tuples result changes '''
#Logical,membership,identity,Comparision(relational) -- always return boolean
#bitwise operators --->it is used only for integers, performs bitwise operations
#&(bitwise and) |(bitwise or) ^(bitwise ex or)
# an integer will be converted binary format and performs bitwise operation following integer to binary conversion
print(7&3)#3
print(7|3)#7
print(7^3)#4
#shift operators
print(7<<1)#14
print(7>>1)#3










