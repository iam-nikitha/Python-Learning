name = "NIKITHA" # name is variable ,Nikitha is the data\value
age = 22
place = "vizag"
print(name) 
print(age)
email_id = "nikitha@gmail.com" # snake-case convention (multiple words) we use underscores to make a meaningful variable name
print(email_id)
branch_7 = 7 # we can use number in naming varible but it cannot be used at begining of variable name
print(branch_7)
#True = 45 # as true is a keywords we cannot use to name a variable
#print(True)
#comments --> It will make users understand what it is conveying
#Single Line Commet --> #
#Mutli line Commet --> we can use triple quotes (DOC String)
#Multi Variable Assignment: make sure to pass same number of values otherwise it rasises a value error
name,email_id,mobile,gender = "NIKITHA","Nikitha@gmail.com",6305938614,"female"
print(name,mobile)
#python by default follows Implicit type (user need not to specify data type of variable)
name = 'nikitha';age = 22;place = "vizag"
print(name,age,place)
#deletion --> del -keyword to permenantly delete the value from memory
del age,name
del place
print(place)
print(name)
print(age)
#swaping of variables
a,b=15,25
print(a)
print(b)
a,b = b,a # value of a will become b
print(a)
print(b)
c = a # reassigning the exisiting to value to new variable
print(c)
#Literals --> these are constants such as numbers(int,float,complex) VALUES WHICH ASSIGNED TO VARIABLE
price = 32.5
print(price)
taste = "bad"
print(taste)
age = 22
print(age)
print(type(price)) # it returns the type of object
print(type(age))
print(type(taste))
#Identifiers --> names given to variables,function,classes,objects,modules
#Punctuators -->[]--> LIST,()-->TUPLES,{}--> dictionaries,sets. stores a group of data
#operators - +,-,*,**,/,//,%
a =5
b = 3
print(a/b) # it gives a float value
print(a//b)# it gives  quotient 
print(a%b)# it gives remaninder'''
#Raju purcharsed with price 1000 discount = 15% how much he has pay
price = 1000
discount = 0.15
final_price = price-(price * discount)
print(final_price)
# vijya went to hostel for dinner his bill is 2500 gst applicable is 5% and he get discount 5% how he has to pay
bill = 2500
after_discount = bill-(bill*0.05)
gst_applied = after_discount * 0.05
final_price = after_discount + gst_applied
print(final_price) 



