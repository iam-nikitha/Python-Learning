'''#Variable length arguments --> We can give any number of positional arguments
#arguments we use(*args),captures excess positional arguments and pack them in tuple

def sample(*a):
    """Usage of arbitary argumenta"""
    print(a)
    print(type(a))
sample()
sample(1,2)
sample('Nikitha','Betch')
sample(12,3,4,5)

#In above we used '*' to pack the values into a tuple
a,b,c = 2,4,-6
print(a,b,c)
a,*b,c = 2,3,4,5,6,7,8,-12
print(a,b,c)
#in this case all vaules are stored into list in case of function it store b values as tuple
#a,*b,*c = 2,3,4,5,6,7,8,-12#multiple expression are not allowed
#print(a,b,c)
a,*b,c=(2,3,4),(6,65),12,12
print(a)
print(b)
print(c)
#find the sum of variables
def add(*a):
    """Usage of variable Length Arguments"""
    #print(a)
    #print(type(a))
    result = 0
    for value in a:
        #if type(value) in (int,float):#menbership operator
        if type(value) == int or type(value) == float: #logical and comparison
            result += value
    #print(result)
    return result
#add()
#print(add(1,2,3,4))
#print(add(1,2,4,6,7,-98,12))
#print(add(1,2,4,-2,'codegnan',2,12,'nikitha'))
d = list(map(int,input().split()))
print(d)
print(add(*d))# we need to use * to unpack the values from the tuple

#we will use above usage of variable lenght arguments from ordering
def order_pizza(size,*toppings):
    """ Usage of * args"""
    print(f'size of  Pizza is {size}')
    print(f'Toppings:{toppings}')
    for topping in toppings:
          print(f'topping added:{topping}')
order_pizza("Large","Onions","Panner","Capsicum","Olives","Mushroom")

# Keyword variable length arguments : Any number of of keyword Arguments
#data is stored in dictionary we use **kwargs..
def sample(**a):
    """Usage of **kwargs"""
    print(a)
    print(type(a))
sample()
sample(name = "Nikitha",batch ="PFS-VSP-007",place = "Vizag",branch="ECE",course ="PFS")
'''
def order_pizza(size,*toppings,**details):
    """ Usage of * args"""
    print(f'size of  Pizza is {size}')
    print(f'Toppings:{toppings}')
    for topping in toppings:
          print(f'topping added:{topping}')
    for key,value in details.items():
        print(f'{key} :{value}')
order_pizza("Large","Onions","Panner","Capsicum","Olives","Mushroom",name = "Nikitha",bill=200,delivery = False,tips=50)

    

