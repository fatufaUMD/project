import re 
import pandas
import numpy
chart = {"Workers": ["Vikram", "Tulio",  "Michael", "Jeraldo"], "Emails": ["vikramj25@gmail.com", "tuliov564@yahoo.com", "bigmike#78@outlook.com", "jeraldoj84@gmail.com"]}#amaked up keys and values for chart
workerChart = pandas.DataFrame.from_dict(chart)
print(workerChart) #establishes a chart to help inform user
raffleList = [] #mutable list, yields results after program
emailList = {"Vikram": "vikramj25@gmail.com", "Tulio": "tuliov564@yahoo.com", "Michael": "bigmike#78@outlook.com", "Jeraldo": "jeraldoj84@gmail.com"}#keys and values for the program
print("Let's see who among these employees is elligible to enter the raffle")
emailType = input("What email type would you prefer?")
if not re.match("^@", emailType):#checks to see if what the user entered is a kind of email.
        for emailEntry in range(3): #checks 4 times, gives up afterwards
             emailType = input("Please enter the proper url, @ included")
             if re.match("^@", emailType):
                break
             break
for name, email in emailList.items():
       if re.search(str(emailType), str(email)):#Goes through the dictionary, checks to see if the input matches the values
        print("{} qualifies".format(name))#Jots down valid employees
        raffleList.append(name)#Adjusts the list
       else:
        print("{} doesn't qualify".format(name))

print("The employee(s) named {} is/are part of the raffle".format(raffleList))#Results





              