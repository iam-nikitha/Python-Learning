'''#Input Formatting /Output Formatting
#input Formatting - Input()
#usage of input()
#we can pass any type of object as input ---> result is in only string
name = input('Enter the name:')
print(name)
#Enter the name:1234
#1234
print(type(name))
#<class 'str'>
#integer Input ---> int()---> if u mismatch value ---> Value Error
roll_number = int(input('Enter the Roll Number:'))
print(roll_number)
print(type(roll_number)) 

#Enter the Roll Number:43
#43
#<class 'int'>

#Float Input---> we can pass either integer or decimal value ---> it takes as float
marks = float(input('Enter the marks:'))
print(marks)
print(type(marks)) 
#Group of Strings (Group values as strings)
#space seperated values
#if we enter the value with comas it treat as elements as one string
#if we enter the values with space in between them it returns as list
#names = input().split() #no need of prompt competive coding platforms
names =input('Enter the names:').split()
print(names)
#Comma seperated
names =input('Enter the names:').split(',')
print(names)
print(type(names))
#Enter the names:nikitha,harika,pratyu
#['nikitha', 'harika', 'pratyu']
#<class 'list'>
#multiple values (more than one)strings # make sure to match the arguments
name,batch = input('enter the detials:').split()#---> result is always string
print(name)
print(batch)
#output
#enter the detials:nikitha pfs7
#nikitha
#pfs7

#Multiple integer values

#order_id,cost = int(input().split()) ---> type error
order_id,cost = map(int,input().split())
print(order_id)
print(cost)
#flaot
python_marks,sql_marks,ss_marks,aptitude_marks = map(float,input().split())
print(python_marks)
print(sql_marks)
print(ss_marks)
print(aptitude_marks)

#group of integers,flaot values
#without list it gives as <map object at 0x000002948F8E2710>
stu_marks = list(map(int,input('enter the marks').split(',')))#[45, 67, 98, 34]
print(stu_marks)
#float

discounts = list(map(float,input().split(',')))
print(discounts)

#accept the cost of selling the product from user and also the orginal cost of the product and determine the profit/loss amount for the user
original_amount = float(input('enter the cost:'))
selling_amount = float(input('enter the selling cost:'))
#profit = (selling_amount - original_amount)
#print(profit)#500
loss = (original_amount - selling_amount)
print(loss)

#set of integers
#set of float values --replace int with float
ids = set(map(int,input().split(',')))
print(ids)
print(type(ids))
#passing list() as input using eval()
list_data = eval(input('Enter the values:'))
print(list_data)
print(len(list_data))
tuple_data = eval(input('Enter the values:'))
print(tuple_data)
print(len(tuple_data))
set_data = eval(input('Enter the values:'))
print(set_data)
print(len(set_data))
#passing dict data using eval
stu_detials = eval(input('enter the detials:'))
print(stu_detials)

#Output Formatting --->Print()
a,b,c = map(str,input().split())
#print(a,b,c,sep='---')#nikitha---vizag---23
#print(a,b,c,sep=':')#nikitha:vizag:23
#end is specifically telling how to end the statement
print(a,b,c,sep='-',end='\t')#after this statemnt ends it give tabs space and then print next line statment
print('nikitha reddy',end = '\n')
print(35,45,67)
print('harika','nikitha',end=' ')
print('reddy')

#1)using commas in print()
name ='codegnan';branch = 'Vizag';batch = 'PFS-VSP-007'
print(name,'is in',branch)
print(batch,'belongs to',branch,'branch')  

#2)Using %(modulus) formating -->old Style C programming
# %d --> integers ,%f--> float,%s ---> string
age = 32
price = 54.562
place = 'vizag'
print('age = %d | Price = %f | Place = %s'%(age,price,place))
print('price is %.f'%price)# in this case complete decimal part is wipped off
print('price is %.2f'%price)# rounding off two decimals. '''

#3) usage of string formatting ---> Str,format()
name = 'Nikitha';place = 'Vizag';age = 22;
print('My name is {} from {} and my age is {}'.format(name,place,age))
a,b = 2,45
print("{1},{0}".format(a,b))
print("value of a is {} and value of b is {}".format(a,b))
#output
#My name is Nikitha from Vizag and my age is 22
#45,2
#value of a is 2 and value of b is 45

#f-string notation --->python 3.9+ versions
print(f'My name is {name}') #My name is Nikitha
#make sure to denote the variables only in curly braces
print(f'value of a is {a} and value of b is {b}')
#value of a is 2 and value of b is 45










