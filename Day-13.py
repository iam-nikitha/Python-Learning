
Control Statments : These are the statements which makes the programming flow to be possible .They control the entire flow if the program

when to execute ,what to execute,how to execute

1.Conditional Statements ---> if,elif,else
2.Jumping Statements--> break,continue,pass,
assert ,try,except,finally
3.Repetition statements --> for,while

#conditional Statments -->Statemnts reply on the conditions

# syntax if : 
if <condition>:
  statments(s)

  
#data = False
data = True
if data:
    print("Welcome to Codegnan")
    print("This is PFS-VSP-007")
print("Guys are good but they will come late")


#mark = 25
mark = int(input("enter the value:"))
marks = [12,14,16,25]
if mark in marks:
    print("marks sucessfully fetched")
    print(f'marks are {mark}')
print(f'its done for today')
 
stock = int(input("enter the value:"))
total_stock = 100
if stock >0 and stock < total_stock:
    print(f"You can order the item")
    print(f"item selected and placed into cart")
    print(f"item ordered")

#Usage of else:
# syntax -->
#if condition :
    #statments
#else:
    #staments

stock = int(input("enter the value:"))
total_stock = 100
if stock >0 and stock < total_stock:
    print(f"You can order the item")
    print(f"item selected and placed into cart")
    print(f"item ordered")
else:
    print(f'Invalid Entry')

#task:

ALOG:
Accept the input from user
age > 0:
    make the eligility case as age >= 18:
         age is granted
    age is not matching eligiblity:
          inform number of years to wait
otherwise inform enter valid age

Dry Run:
age --> 19 -->result --> 19>=18 and 19>0
age --> 12 -->result --> 18-12 --> 6
age --> -12 --> result --> Enter valid age 
    

age = int(input("Enter the age :"))
if age > 0 :
    if age >=18:
        print("eligible to vote")
    else:
        print(f'you have to wait {18 - age} years')
else:
    print(f'enter valid age')

#if -elif -else--> we wanted to map multiple conditions

age = int(input("Enter the age :"))
if age >0 and age >=18 and age<=100:
    print('you are eligible to vote')
elif age >0 and age <18:
    print(f'you have to wait {18 - age} years')
else:
    print('invalid')



#task -->placemenet Eligibilty
print("==========PLACEMENT ELIGIBILTY CHECKER=============")
name = input("Enter the Student name:")
attendance = float(input("Enter the Attendence of the Student"))
technical_score = float(input("Enter the Technical Score of the Student"))
mock_interview = float(input("Enter the Mock Interview Score of the Student"))
projects = int(input("Enter the number of projects"))

avg_score = (technical_score + mock_interview)/2
if attendance >=75 and avg_score>=75 and projects>2:
    print(f'Result : Student is Placement Ready he/she falls in Hotlist')
elif attendance >=60 and avg_score>=60 and projects>1:
    print(f'Result : Student needs more preparation--->Improvement Stage')
else:
    print(f'Result : Student is in Foundation Stage--> Needs Pratice Session')

 

    
    
    



