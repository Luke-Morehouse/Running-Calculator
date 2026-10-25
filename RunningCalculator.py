import math;
distanceKm = 0;
time = "25:00.00";

'''This function takes in the distance ran and time in MM:ss.mmm format 
 returns the pace per km '''
def pacePerKilometer(distanceKm, time):
    timeSeconds = convertTimeToSeconds(time)
    paceSecPerKm = timeSeconds/distanceKm
    minutes = int(paceSecPerKm // 60)
    seconds = paceSecPerKm % 60
    secStr = f"{seconds:06.3f}".rstrip("0").rstrip(".")
    print(f"Pace: {minutes}:{secStr} min/km")

def pacePerMile(distanceMi, time):
    timeSeconds = convertTimeToSeconds(time)
    paceSecPerMi = timeSeconds/distanceMi
    minutes = int(paceSecPerMi // 60)
    seconds = paceSecPerMi % 60
    secStr = f"{seconds:06.3f}".rstrip("0").rstrip(".")
    print(f"Pace: {minutes}:{secStr} min/mi")
    
#This function takes in a time in MM:ss:mmm format and turns it into seconds
def convertTimeToSeconds(time):
    #Breaks the time up at the colon and saves it to 2 different variables
    minutesStr, rest = time.split(":")
    secondsFloat = float(rest)
    timeSeconds = (int(minutesStr) * 60) + secondsFloat
    return timeSeconds

print("Welcome to the running calculator, made by Luke Morehouse")
userInput = input("What would you like to chose, your options are: Calculate Pace \n")  
if userInput.lower() == "calculate pace": 
    distanceUnit = input("Would you like your pace per kilometer or per mile? \n")
    if (distanceUnit.lower() == "miles") or (distanceUnit.lower() == "mi") or (distanceUnit.lower() == "mile"):
        try:
            userDistance= float(input("Enter your distance in miles: "))
            userTime = str(input("Enter your time in the form mm:ss.MM "))
            pacePerMile(userDistance, userTime)
        except ValueError:
            print("Make sure your input is a valid number")