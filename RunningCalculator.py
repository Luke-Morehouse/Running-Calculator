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
    """This function takes in a time in MM:ss.mmm format and turns it into seconds"""
    minutesStr, rest = time.split(":")
    secondsFloat = float(rest)
    timeSeconds = (int(minutesStr) * 60) + secondsFloat
    return timeSeconds

def convertMiToKm(distanceMi):
    """This function takes in the distance in miles and turns it into kilometers"""
    return  distanceMi * conversionFactor
    
def convertKmToMi(distanceKm):
    """This function takes in the distance in kilometers and turns it into miles"""
    return distanceKm / conversionFactor

def getPace(unit):
    """This function asks the user for their pace in the form MM:SS.mmm and makes sure it is valid before returning it"""
    while True:
        userPace = input(f"Enter your pace per {unit} in the form MM:SS: ").strip()
        try:
            seconds = convertTimeToSeconds(userPace)
            if seconds > 0:
                return seconds
            print("Pace must be greater than 0.")
        except ValueError:
            print("Pace must look like 5:00 or 4:51")

def getDistance():
    """This function asks the user for their distance and makes sure it is valid before returning it"""
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
    """This function asks if the user wants the pace per kilometer or mile and uses the distance and 
    time to return the pace"""
    while True:
        distanceUnit = input("Would you like your pace per kilometer or per mile? \n> ")
        if (distanceUnit.lower() in ("miles", "mile", "mi")):
            userDistance= getDistance()
            userTime = getTime()
            pacePerMile(userDistance, userTime)
            break
        elif (distanceUnit.lower() in ("kilometers", "kilometer", "km")):
            userDistance = getDistance()
            userTime = getTime()
            pacePerKilometer(userDistance, userTime)
            break
        else:
            print("Make sure you chose either miles or kilometers")
            
def calculateTime():
    """This function uses the distance and pace to return their total time"""
    while True:
        distanceUnit = input("Would you like to enter your pace and distance per kilometer or per mile? \n> ")
        if (distanceUnit.lower() in ("miles", "mile", "mi")):
            userDistance= getDistance()
            userPace = getPace("mile")
            time = formatSeconds(userDistance * userPace)
            print(f"Your time is {time}")
            break 
        elif (distanceUnit.lower() in ("kilometers", "kilometer", "km")):
            userDistance = getDistance()
            userPace = getPace("kilometer")
            time = formatSeconds(userDistance * userPace)
            print(f"Your time is {time}")
            break
        else:
            print("Make sure you chose either miles or kilometers")

def calculateDistance():
    """This function uses the pace and time to return their total distance ran"""
    while True:
        distanceUnit = input("Would you like to enter your pace and time and get back your distance in miles or kilometers? ")
        if (distanceUnit.lower() in ("miles", "mile", "mi")):
            userPace = getPace("mile")
            userTime = getTime()
            userTimeSeconds = convertTimeToSeconds(userTime)
            distance = round(userTimeSeconds/userPace, 2)
            print(f"Your distance is {distance} miles.")
            break
        elif (distanceUnit.lower() in ("kilometers", "kilometer", "km")):
            userPace = getPace("kilometer")
            userTime = getTime()
            userTimeSeconds = convertTimeToSeconds(userTime)
            distance = round(userTimeSeconds/userPace, 2)
            print(f"Your distance is {distance} kilometers.")
            break
        else:
            print("Make sure you enter either miles or kilometers.")

def distanceConverter():
    """This function takes a distance in miles or kilometers and converts it into the other one"""
    while True:
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

def PrTracker():
    while True: 
        try:
            userChoice = input("Would you like to \n 1. View PRs \n 2. Save a new PR \n > ").strip()
            if userChoice in ("1.", "1"):
                pass 
            elif userChoice in ("2.","2"):
                pass 
            else:
                print("Make sure you chose either 1 or 2")
        except ValueError:
            print("Make sure your choise is a valid number.")
def main():
    print("Welcome to the running calculator, made by Luke Morehouse \n")
    while True:
        print("Chose the number of one of the options below \n")
        print("1. Calculate Pace")
        print("2. Calculate Time")
        print("3. Calculate Distance")
        print("4. Convert Distances")
        print("5. PR Tracker")
        print("6. Quit")
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
            PrTracker()
        elif userInput in ("6", "6."):
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again")
        
main()