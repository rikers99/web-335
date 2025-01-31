"""Author: Steve  Culmer 
Date: 31-01-2025
File name: <path>
Description: This program manages a weekly schedule for a Lemonade stand """

#List of running the Lemonade Stand 
tasks= ["Buy Lemons","Make Lemonade", "sell lemonade", "count earning", "Clean up"]

#List of days in a week
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday"]

#Printing all tasks 
print("Lemonade Stand Tasks: ")
for task in tasks:
    print(f"- {task}")
    
#Assigning tasks to days 

print("\nWeekly Schedule: ")
for i, day in enumerate(days):
    if day in ["Sunday", "Saturday"]:
        print(f"{day}: Day off, time to rest! ")
    else:
        print(f"{day}: {tasks[i % len(tasks)]}")