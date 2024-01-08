# Lilia Skumatova
# CPSC 231
# Homework Assignment 2
from turtlesetup_plot import *

# Asks how many points the user want's to plot
numOfPoints = int(input("How many points do you want to plot?"))
# empty variables created to be global and used and changed in any loop
xCoordinate = []  # Empty list for the years
yCoordinate = []  # Empty list for birth rates
tempXCoordinate = 0
tempYCoordinate = 0
endBirthRate = 0
startBirthRate = 0
interpolate = 0
indexForInterpolation = 1


# Function to draw a square marker around points of the graph
def drawMarker(xOfPoint, yOfPoint):
    t.up()
    t.goto(xOfPoint + 0.25, yOfPoint - 0.01)
    t.down()
    t.goto(xOfPoint + 0.25, yOfPoint + 0.01)
    t.goto(xOfPoint - 0.25, yOfPoint + 0.01)
    t.goto(xOfPoint - 0.25, yOfPoint - 0.01)
    t.goto(xOfPoint + 0.25, yOfPoint - 0.01)
    t.up()
    t.goto(xOfPoint, yOfPoint)
    t.down()


# errorOccurred function is used to print our error and exit the program on click when a mistake is made
def errorOccurred():
    print("Error.")
    screen.exitonclick()
    quit()  # Stops the program from running


if numOfPoints > 0:  # checks if input is bigger than 0
    for x in range(numOfPoints):  # loops through to the number of points
        # Asks for the x coordinate as many times as the for loop iterates based on user's input
        print("What is the x coordinate of data point", str(x + 1) + "?")
        tempXCoordinate = int(input())
        # checks if index is at 0
        # if at 0 then there is nothing in list yet
        if x == 0:
            # Only checks if the year is between 1910 and 2022 as there is nothing in list
            if 1910 <= tempXCoordinate <= 2022:
                xCoordinate.append(tempXCoordinate)
            else:
                errorOccurred()
        # used for when index is bigger than zero
        elif x > 0:
            # Checks if the year is between 1910 and 2022 and if the entered year is in chronological order
            if 1910 <= tempXCoordinate <= 2022 and tempXCoordinate > xCoordinate[x - 1]:
                xCoordinate.append(tempXCoordinate)
            else:
                errorOccurred()
        # Asks user for the birth rate
        print("What is the y coordinate of data point", str(x + 1) + "?")
        # Rounds birth rate to two decimal places
        tempYCoordinate = round(float(input()), 2)
        # Checks if the birth rate is between 0.2 and 4.5
        if 0.2 <= tempYCoordinate <= 4.5:
            yCoordinate.append(tempYCoordinate)
        else:
            errorOccurred()
        # Draws the points on the graph
        t.goto(xCoordinate[x], yCoordinate[x])
        t.down()
        # drawMarker function
        drawMarker(xCoordinate[x], yCoordinate[x])
        t.hideturtle()
    # Asks user what year they would like to start for interpolation
    startYear = int(input("Which year would you like to start with?"))
    # Checks if the year is between 1910 and 2022.
    # Does not check uf year is in chronological order as it is the start year nothing before
    # Does not check if year has been entered before as it's the start
    if 1910 <= startYear <= 2022:
        # Checks if the entered year is in the list
        for i in range(numOfPoints):
            if startYear == xCoordinate[i]:
                # Saves the birth year that is saved under the same index as Year User inputted
                startBirthRate = yCoordinate[i]
                break
        else:
            # Prints this when point is not found in the list
            print("The entered data point does not exist.")  # come back to this
            screen.exitonclick()
            quit()
    else:
        errorOccurred()

    # Asks what year the user would like to end interpolation with
    endYear = int(input("Which year would you like to end with?"))
    # Checks if the year is between 1910 and 2022
    # Checks if the year is entered in chronological order
    # Checks if the year is not the same as the start year
    if 1910 <= endYear <= 2022 and endYear > startYear:
        for i in range(numOfPoints):
            # Checks if the end year is in the list
            if endYear == xCoordinate[i]:
                # Saves the birth year that is saved under the same index as Year User inputted
                endBirthRate = yCoordinate[i]
                break
        else:
            # Prints when the conditions in the if statement are not met
            print("The entered data point does not exist.")  # come back to this
            screen.exitonclick()
            quit()
    else:
        errorOccurred()

        # INTERPOLATE
    # Loops through to calculate interpolation for every year between
    # start year and end year, without including them
    for z in range((endYear - startYear) - 1):
        # Calculates
        interpolate = startBirthRate + (endBirthRate - startBirthRate) * (
                ((startYear + indexForInterpolation) - startYear) / (endYear - startYear))
        # Prints the year and the interpolation for that year
        print(startYear + indexForInterpolation, "%.2f" % interpolate)
        # Draws markers for the interpolated points
        drawMarker(int(startYear + indexForInterpolation), float(interpolate))
        indexForInterpolation = indexForInterpolation + 1
    t.hideturtle()
    screen.exitonclick()
else:
    print("Error.")
    screen.exitonclick()  # Ends program on click
