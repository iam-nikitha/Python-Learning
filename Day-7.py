'''#Sequences ---> Strings ,Lists,tuples,sets,Frozensets,Dictionaries
#String --> A string is a group of characters,It is immutable,ordered,Indexed Colelction.
#We can denote it in single,double,triple quotes
data = '' #empty string
print(type(data))#<class 'str'>
print(len(data))

#operations ---> Concenation Repetition indexed slicing
#Concatation --> combinig multiple strings
sub1 = "Python"
sub2 = "Mysql"
#print(sub1+sub2)
print(f'{sub1},{sub2}')
print(sub1 + " <-> " +sub2)

#repetation : String can be repeated any number of items with a valid int
print('*')
print("*" * 10)
name = "Nikitha" ; place = "vizag"
print(f'{name * 10}')
print(f'----->{name} is in -----> {place}')

#Membership ----> in,not in
print("jay" in "Ajay")#True
print("Jay" in "Ajay") # false

#Indexing --> use to access the elements one by one
#it starts at 0 and ends at len(obj) -1
c = 'Fullstack'
#traversing the elements --> Postive Indexing
#print(len(c))#9
#print(c[7])
#print(c[9])#IndexError: string index out of range
#Negative indexing --> starts from back it is denoted as -1 to len(obj)
print(c[-1])
print(c[0])

#Slicing: extracting a part of string,[Start:END] start is included,end is excluded
s = 'codegnan'
print(s[:])#codegnan
print(s[0:])#codegnan
print(s[0:4])#code
print(s[4:8])#gnan
print(s[4:21])# even if its ending number is not there it will give upto where it was defined
print(s[2:5])#deg
print(s[5:])#nan
print(s[:5])#codeg
print(s[24:])#returns empty
print(s[5:1])#returns empty

#c[s] = 'niki' #strings are immutable 

name = 'codegnan'
print(name[-1:])
print(name[-5:-1])
print(name[:-1])
print(name[:-6])
print(name[-1:-5]) # empty because it gives -1 is > -2
print(name[-2:])
print(name[:-2])

#striding -->[start:end:step] #step -1 # step cannot be zero
name = 'codegnan'
print(name[::0]) #returns value error
print(name[::1]) # complete string
print(name[::2]) # skips alternate after frist one character #cdga
print(name[::3]) # skips two character after first #cea

place = "Visakhapatnam"
#print(place[:4])
#print(place[7:1])
print(place[1:-1:1])
print(place[8::1])
#what if we give -1 in step 
print(place[::-1])#this helps to return in reverse order
print(place[::-2])
#print(place[1:4:-2])
print(place[-9:-5:-2])
#built-in fuctions -->type(),len(),min(),max(),ord(),chr(),sorted()
p = 'admin123'
print(len(p))
print(min(p))
print(max(p)) # follows ascii values
print(ord('A'))
print(chr(122))
print(sorted(p)) 

#Task: Pratice string operations
#concatention

a = '10'
b = '20'
print(a+b)#1020

a = 'python'
b = 10
#print(a+b)#TypeError: can only concatenate str (not "int") to str
print(a+str(b))#python10
print(a + ' ' + str(b)) #python 10
print(a + ',' + str(b))#python,10 

a = 'Hi'
print(a*2) # HiHi
print((a+' ')*2) #Hi Hi

a = '5'
print(a * 2 +'3')#553 

a = ''
b = 'python'
print(a+b) #python --> empty string does not add character

#indexing 

s = 'python'
print(len(s)) #6
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])
print(s[7])#IndexError: string index out of range
#negTIVE --> accessing from last
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])
#print(s[-7])#IndexError: string index out of range

s_1 = 'computer'
print(s_1[1+3]) # 1+3 = 4 s[4] = u

s_2 = 'developer'
print(s_2[-2-2]) #-4 = s[-4] #0

s_3 = 'ABCDEFG'
i = 2
print(s_3[i+2]) # s[4] -->E

s_4 = 'python'
print(s_4[-1*2]) #-1*2 =-2 s[-2] = 0

s_5 = 'abcdefghij'
print(s_5[len(s_5) -5]) #10-5 = 5 is f

s_6 = 'notebook'
print(s_6[-len(s_6)+3])

s = 'python'
print(s[True]) # y

s = 'python'
print(s[False]) #p

s = 'abc'
print(s[-0])#a


#slicing

s = 'python'
print(s[1:4])#YTH

print(s[:4])#start from the beginning
print(s[2:]) # go to the end
print(s[3:3]) #both indices are same #empty string
print(s[4:2]) #start is greater than stop #empty string
print(s[:3]) # missing start defaults to index 0
print(s[2:])# missing stop defaults to the end
print(s[:]) # gives all characters
print(s[2:6]) #stop equals the string length
print(s[6:6]) #empty string
print(s[8:10]) #both indices exceed the string length
print(s[1:len(s)])#ython
print(s[-5:-2]) # yth
print(s[-2:-5]) #start is greater than stop #empty string
print(s[-5:4])
print(s[-4:5])
print('h')
print(s[-4:-4]) #both strat = stop --->empty string
print(s[-3:-1])#ho
print(s[5:-3])#empty
print(s[-10:3]) #an excessively negative start is treated as beginning of the string
print(s[-6:6]) #python

'''
s = 'python'
print(s[::1])#s=0,e=last,no skipping
print(s[::2]) #skip every 2 nd character only one char skip
print(s[1::2])#yhn
print(s[1::3])#yo
print(s[2::2])#to
print(s[0:5:2])#pto
print(s[0:4:3])#ph
print(s[1:5:2])#yh
print(s[0:6:4])#po
print(s[3:3:1])#emptystring
print(s[0:100:2]) #pto
print(s[::-1]) #reverse order
print(s[::-2]) # nhy
print(s[1:5:-1]) #if start is less than stop in negative step then empty space
print(s[-5:5:2])
print(s[-2:2:-1])#0h
print(s[4:-2:-1]) #empty string
print(s[1:-1:1]) #ytho































