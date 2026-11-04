#usage of for with conditional Statments

#Notification Checker
#notifications = [0,0,0,0] #0-->read i-->unread
#notifications = [0,0,1,0,1]
#notifications = [0,0,1,1,0,0]
notifications = [0,0,1,1,0,0]
for notification in notifications:
    #you need to map a condition
    if notification == 1:
        print(f'Unread Notification')
    
else:
    print("All Notification are caught")
#break : it terminate the loop

#searching scenario same above program to be tranformed -->
#if target is found
notifications = [0,0,1,1,0,0]
for notification in notifications:
    #you need to map a condition
    if notification == 1:
        print(f'Unread Notification')
        break #it exists early ,the else block will be skipped
else:
    print("All Notification are caught")


#searching in a list
#you want to handle the "item not found " case

fruits = ["apple","banana","kiwi","cheeries"]
item = input("Which fruit u want:").lower()
for fruit in fruits:
    if item == fruit:
        print(f"You got your desired {item}")
        break
else:
    print(f"Could not found {item} in the fruits")

fruits = ["apple","banana","kiwi","cheeries"]
item = input("Which fruit u want:").lower()
for fruit in fruits:
    if item == fruit:
        print(f"You got your desired {item}")
        continue
else:
    print(f"Could not found {item} in the fruits")
       
notifications = list(map(int,input("Enter the values:").split(',')))
for notification in notifications:
    #you need to map a condition
    if notification == 1:
        print(f'Unread Notification')
        continue
    
else:
    print("All Notification are caught")

notifications = list(map(int,input("Enter the values:").split(',')))
for notification in notifications:
    #you need to map a condition
    if notification == 1:
        pass
        #print(f'Unread Notification')
        #break
    
else:
    print("All Notification are caught")


#while --> Loops --> it is mainly used when we reply condition it will be completely executed until the condition is satisfied
#while <condition>:
    #statments(s)...
#while True:
    #print("Yes") it runs an infinite loop we need to keyboard interrupt

#initalizer with which we need to initalize
i = 0
while i<=10:
    #print(i)
    i+=1 # increment
    print(i)

#get the counter from 10 to 1
i = 10
while i>=1:
    print(i)
    i -=1#decrement


i = 0
while i<=10:
    print(10-i)
    i +=1#decrement
    
       

