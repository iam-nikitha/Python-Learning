'''# String Methods --> Case Conversions,Replacing,Finding,White trailing spaces,Testing methods,alignment methods
#case conversions ---> upper(),lower(),title(),capitalize(),swapcase()
data = 'Codegnan'
print(type(data))
#print(dir(data))
#upper() --> converts object to uppercase
#print(data.upper())
e = data.upper()
print(e)
#converts object to lowercase - lower()
f = data.lower()
print(f) 
#capitalize() --> it will capital the first letter in the word
print('codegnan vizag'.capitalize()) #Codegnan vizag
#title() --->it will capitalize every first letter in each word
print('codegnan vizag'.title()) #Codegnan Vizag

#testing methods --> which will give the result as boolean(True/False)
#isupper(),islower(),isalnum(),isdigit(),isalpha(),startswith(),endswith(),

print('Codegnan'.isupper()) #false
print('codegnan'.islower()) #true
print('admin123'.isupper()) #false
print('123ADMIN'.isupper())#True
print('d13g'.islower())#True
print('coDEgnan'.swapcase())#COdeGNAN
print('admin123'.isalpha()) #returns only when all are alphabets
print('admin123'.isalnum()) # returns true for an digits and letters
print('1234'.isdigit()) #true when it it digits
print('Python'.istitle()) #true
print('Python aptitude'.istitle()) #false as 2nd word begining is not capital 
print('Python'.startswith('P'))
data = 'Python Apititude'
print(data.startswith("P"))
print(data[7:].startswith("A"))
print(data.startswith("A",7))
print(data.endswith("e"))
print(data.endswith('n',0,6)) # letter ,start,stop
print(data.endswith('t',0,3))
print('12.34'.isnumeric())#it doesnt consider decimal and negative
print('½'.isnumeric()) #true
print('²'.isnumeric()) # true
print('123'.isnumeric())#true
print('-4.5'.isnumeric()) # false

#finding and Searching methods --> find(),index(),count()

data = 'Codegnan is Vizag'
print(data.find('a')) # 6 first occerence index
print(data.find('a',7)) # next occurences index
print(data.rfind('a')) # returns last occerence index of that letter
#find() will return -1 if the given object is not present 
print(data.index('a')) # returns the index of the character
print(data.index('V'))
print(data.index('x'))#ValueError: substring not found
print('qwerty'.index('wert'))# returns the substring first char index
data = 'Codegnan is Vizag'
print(data.count('n')) #2
#count() will return total number of occurences
print(data.count('t'))#0
print(data.count())#TypeError: count() takes at least 1 argument (0 given)

#split(),join(),strip(),lstrip(),rstrip(),zfill()
#split() returns the list of substrings from the string using seperator
a = 'python aptitude softskills Mysql'
b = a.split()# by default space is treated
print(b)#['python', 'aptitude', 'softskills', 'Mysql']
a = 'python,aptitude,softskills.Mysql'
c=a.split(',')
print(c)#['python', 'aptitude', 'softskills.Mysql']

#join()
print('code'.join ('gnan')) # concatenates every object with given iteratable
print(' '.join('Nikitha')) # N i k i t h a
print('*'.join('Codegnan')) #C*o*d*e*g*n*a*n

#White space and Triming Methods ---->srtip(),lstrip(),rstrip()
a = 'Nikitha '
print(len(a))#8
a = a.strip()
print(a)#7
print(len(a))
b = 'nikitha reddy  '
b =b.rstrip()
print(b)
c = ' Nikitha reddy'
print(c)
c = c.lstrip()'''

#Alignment Methods---> zfill---> it add zeros from left

print('python'.zfill(10))
print('codegnan'.zfill(1)) #make sure to pass width > len(obj)
print('nikitha'.center(10,'*')) #*nikitha**
print('python'.ljust(10,'*'))#python**** # returns the leftjustified string with fillchar
print('python'.rjust(10,'*'))#****python #returns the rightjustified string with fillchar




 




