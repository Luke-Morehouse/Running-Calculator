import math;
conversionFactor = 1.609344

def formatSeconds(totalSeconds):
    """Turn seconds into M:SS or M:SS.mmm, trimming unneeded trailing zeros."""
    totalMs = round(totalSeconds * 1000)
    minutes, ms = divmod(totalMs, 60000)
    seconds = ms / 1000
    secStr = f"{seconds:06.3f}".rstrip("0").rstrip(".")
    return f"{minutes}:{secStr}"

def pacePerKilometer(distanceKm, time):
    """Print the average pace in min/km for a run of the given distance and time."""
    timeSeconds = convertTimeToSeconds(time)
    paceSecPerKm = timeSeconds/distanceKm
    print(f"Pace: {formatSeconds(paceSecPerKm)} min/km")

def pacePerMile(distanceMi, time):
    """Print the average pace in min/mi for a run of the given distance and time."""
    timeSeconds = convertTimeToSeconds(time)
    paceSecPerMi = timeSeconds/distanceMi
    print(f"Pace: {formatSeconds(paceSecPerMi)} min/mi")
    

def convertTimeToSeconds(time):
    #This function takes in a time in MM:ss.mmm format and turns it into seconds
    minutesStr, rest = time.split(":")
    secondsFloat = float(rest)
    timeSeconds = (int(minutesStr) * 60) + secondsFloat
    return timeSeconds

def convertMiToKm(distanceMi):
    return  distanceMi * conversionFactor
    
def convertKmToMi(distanceKm):
    return distanceKm / conversionFactor

def getPace():
    while True:
        userPace = input("Enter your pace in the form MM:SS: ").strip()
        try:
            seconds = convertTimeToSeconds(userPace)
            if seconds > 0:
                return seconds 
            print("Pace must be greater than 0. ")
        except ValueError:
            print("Pace must look like 5:00 or 4:51")

def getDistance():
    while True:
        try:
            distance = float(input("What is the distance? "))
            if distance > 0: 
                return distance
            else:
                print("Distance must be greater than 0.")
        except ValueError:
            print("Make sure your distance is a number.")

def getTime():
    """Keep asking until the user enters a valid time in MM:SS.mmm format."""
    while True:
        userTime = input("Enter your time in the form MM:SS.mmm: ").strip()
        try:
            seconds = convertTimeToSeconds(userTime)
            if seconds > 0:
                return userTime
            print("Time must be greater than 0.")
        except ValueError:
            print("Time must look like 25:30 or 25:30.5")

def calculatePace():
    while True:
        distanceUnit = input("Would you like your pace per kilometer or per mile? \n> ")
        if (distanceUnit.lower() in ("miles", "mile", "mi")):
            while True:
                    userDistance= getDistance()
                    userTime = getTime()
                    pacePerMile(userDistance, userTime)
                    break
            break
        elif (distanceUnit.lower() in ("kilometers", "kilometer", "km")):
            while True:
                    userDistance = getDistance()
                    userTime = getTime()
                    pacePerKilometer(userDistance, userTime)
                    break
            break
        else:
            print("Make sure you chose either miles or kilometers")
            
def calculateTime():
    print("Given the distance and pace, find your finishing time")
    while True:
        distanceUnit = input("Would you like to enter your pace and distance per kilometer or per mile? \n> ")
        if (distanceUnit.lower() in ("miles", "mile", "mi")):
                    userDistance= getDistance()
                    userPace = getPace()
                    time = formatSeconds(userDistance * userPace)
                    print(f"Your time is {time}")
                    break 
        elif (distanceUnit.lower() in ("kilometers", "kilometer", "km")):
                    userDistance = getDistance()
                    userPace = getPace()
                    time = formatSeconds(userDistance * userPace)
                    print(f"Your time is {time}")
                    break
        else:
            print("Make sure you chose either miles or kilometers")

def calculateDistance():
    print("Given the time and pace, find your finishing distance")
    while True:
        distanceUnit = input("Would you like to enter your pace and time and get back your distance in miles or kilometers? ")
        if (distanceUnit.lower() in ("miles", "mile", "mi")):
            userPace = getPace()
            userTime = getTime()
            userTimeSeconds = convertTimeToSeconds(userTime)
            distance = round(userTimeSeconds/userPace, 2)
            print(f"Your distance is {distance} miles.")
            break
        elif (distanceUnit.lower() in ("kilometers", "kilometer", "km")):
            userPace = getPace()
            userTime = getTime()
            userTimeSeconds = convertTimeToSeconds(userTime)
            distance = round(userTimeSeconds/userPace, 2)
            print(f"Your distance is {distance} kilometers.")
            break
        else:
            print("Make sure you enter either miles or kilometers.")

def distanceConverter():
    while True:
        try:
            distanceUnit = input("What would you like to convert \n 1. Miles to kilometers \n 2. Kilometers to miles? \n 3. Back \n > ").strip()
            if distanceUnit in ("1", "1."):
                distance = getDistance()
                print(f"{distance} miles is {round(convertMiToKm(distance), 3)} kilometers.")
                break
            elif distanceUnit in ("2", "2."):
                distance = getDistance()
                print(f"{distance} kilometers is {round(convertKmToMi(distance), 3)} miles.")
                break
            elif distanceUnit in ("3", "3."):
                break
            else: 
                print("Invalid Choice, please try again")
        except ValueError:
            print("Make sure your distance is a valid number")
    

def main():
    print("Welcome to the running calculator, made by Luke Morehouse \n")
    while True:
        print("Chose the number of one of the options below \n")
        print("1. Calculate Pace")
        print("2. Calculate Time")
        print("3. Calculate Distance")
        print("4. Convert Distances")
        print("5. Quit")
        userInput = input("> ").strip()
        if userInput in ("1", "1."):
            calculatePace()
        elif userInput in ("2", "2."):
            calculateTime()
        elif userInput in ("3","3."):
            calculateDistance()
        elif userInput in ("4", "4."):
            distanceConverter()
        elif userInput in ("5", "5."):
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again")
        
main()