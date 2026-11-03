1.#Write a python program to Display "Best Seller" if the product sales are greater thab 1000
product_sales = int(input("Enter the Product sales:"))
if product_sales > 1000:
    print("Best Seller")
else:
    print("No Output")

#2.Zepto Delivery 
rain = bool(input())
if rain :
    print("Extra Rain Charges Applied")
else:
    print('No Output')

#3 Delivery Charge Calculation

order_value = int(input("Enter the order value:"))
if order_value <=99:
    
    print(f"Final Bill Amount:{order_value+30}")
else:
    print(f"Final Bill Amount:{order_value}")

#plan according on budget
Budget = int(input("Enter the Budget:"))
if Budget>10000:
    print("Plan: Trip")
elif Budget>5000:
    print("Plan: Resort Stay")
elif Budget >3000:
    print("Plan: Movie and Dinner")
elif Budget >1000:
    print("Plan: Cafe and Shopping")
elif Budget > 500:
    print("Plan: Street Food and Park Visit")
else:
    print("Plan: Stay Home")

#Repetition Statments(Loops) --> Loops helps us in automating repetitive tasks --> for ,while
#usage of for:--> It is used mainly to iterate within in lists ,strings


Syntax:
for <temp> in collection/range:
     Statments(s).....
     ....

#marks = [25,20,21,19,10,12]
#marks can be dynamic
marks = list(map(int,input().split(",")))
for i in marks:
    print(i)#it traverses within the loop

marks = list(map(int,input("Enter the marks:").split(",")))
total = 0
for mark in marks:
    total = mark+total #total+=mark
    print(total)
print(f'Total Marks are:{total}')
print(f'Average Marks are:{total/len(marks)}')
#string which access each character
subject = input("Enter the subject:")
for i in subject:
    print(i)

detials = {'ids':[123,123,125],
           'marks':[25,20,21]}
for data in detials:
    #print(data)#indexed through keys
    print(detials[data])
for data in detials.values():
    print(data)
for key,value in detials.items():
    print(key,value)


    
