# Running Calculator

A command line tool written in Python that solves for pace, time, or distance in kilometers or miles

## Features 

- Solving for pace, time, or distance given the other two values 
- Supports both miles and kilometers
- Accepts time in MM:SS.mmm format 
- PR Tracker that saves personal records to a separate file on the device 

## Requirements 

- Python 3.12.11

# How to Run

```bash
git clone https://github.com/luke-morehouse/running-calculator
cd running-calculator
python runningCalculator.py
```

# Example 

```
Chose the number of one of the options below

1. Calculate Pace
2. Calculate Time
3. Calculate Distance
4. Convert Distances
5. PR Tracker
6. Quit
> 1
Would you like your pace per kilometer or per mile?
> mile
What is the distance? 5
Enter your time in the form MM:SS.mmm: 25:00.00
Pace: 5:00 min/mi
```

# What I Learned 
- Increased my knowledge of f strings 
- It is easier and less code to use the in function and a list instead of using or, ex: if distance in ("miles", "mi" "mile")
- Increased my knowledge of writing to a file and how to do it safely without creating errors 
- Learned how to format time given seconds to make it in to MM:SS.mmm
