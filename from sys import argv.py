from sys import argv
weekday = {
    "monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "sunday": 7
}

weekday = argv[1:]

for x in weekday:
    if(weekday == 1):
        print("Monday")

    elif(weekday == 2):
        print("Tuesday")

    elif(weekday == 3): 
        print("Wednesday")

    elif(weekday == 4):
        print("Thursday")
      
    elif(weekday == 5):
        print("Friday") 
    
    elif(weekday == 6):
        print("Saturday")
    
    elif (weekday == 7):
        print("Sunday") 
    
    else:
        print("Invalid input")