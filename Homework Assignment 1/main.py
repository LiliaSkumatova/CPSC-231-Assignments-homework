from turtlesetup import *

print("Here are a square, a triangle, a pentagon, and a star!")
# Draw the Triangle use coordinates
turtle.down()
turtle.goto(x=0, y=100)  # Creates first point of square
turtle.goto(x=100, y=100)  # Creates second point of square
turtle.goto(x=100, y=0)  # Creates third point of square
turtle.goto(x=0, y=0)  # Creates fourth point of square
turtle.up()
turtle.back(distance=150)
# code for drawing the square
turtle.down()
turtle.goto(x=-200, y=100)  # Draws first side of triangle
turtle.goto(x=-250, y=0)  # Draws second side of triangle
turtle.forward(distance=100)  # Draws third side of triangle
turtle.up()
turtle.back(distance=200)  # Moves turtle to different spot for next shape
# code for drawing the pentagon
turtle.down()
pentagonDis = 70  # variable created to have equal distance for the pentagon's side
turtle.back(pentagonDis)
turtle.left(angle=108)  # Angle different from the rest to get turtle on the right path
# Repeats angle and forward until all 5 sides are completed
turtle.forward(pentagonDis)
turtle.right(angle=72)
turtle.forward(pentagonDis)
turtle.right(angle=72)
turtle.forward(pentagonDis)
turtle.right(angle=72)
turtle.forward(pentagonDis)
turtle.up()
# code for drawing the star
turtle.goto(x=200, y=0)  # Moves to unused space
starDis = 50  # variable created for distance for all the star's sides to keep them equal
# angles used to measure out a symmetrical star
# angles changed based on exterior or interior angles of the star
turtle.down()
turtle.left(angle=180)
turtle.forward(starDis)
turtle.left(angle=72)
turtle.forward(starDis)
turtle.right(angle=144)
turtle.forward(starDis)
turtle.left(angle=72)
turtle.forward(starDis)
turtle.right(angle=144)
turtle.forward(starDis)
turtle.right(angle=288)
turtle.forward(starDis)
turtle.right(angle=144)
turtle.forward(starDis)
turtle.left(angle=72)
turtle.forward(starDis)
turtle.right(angle=144)
turtle.forward(starDis)
turtle.left(angle=72)
turtle.forward(starDis)
turtle.up()
turtle.forward(distance=100)  # move the turtle away from the shapes
# Asks the user what they would like to draw between the Triangle and the Square
choice = input("What would you like to draw?")
# uses lower method to make sure that all letters are in lowercase
# for if user input an uppercase it doesn't mark it
if choice.lower() == "triangle":
    print("Great, show me a triangle!")
    # if the user inputs triangle, and it matches the if, then program asks user to input the coordinates of the points
    # user is asked for 3 points to match the three vertices of a triangle
    firstTriPointX = int(input("Enter x coordinate of the first point: "))
    firstTriPointY = int(input("Enter y coordinate of the first point: "))
    secondTriPointX = int(input("Enter x coordinate of the second point: "))
    secondTriPointY = int(input("Enter y coordinate of the second point: "))
    thirdTriPointX = int(input("Enter x coordinate of the third point: "))
    thirdTriPointY = int(input("Enter y coordinate of the third point: "))
    # The collinear formula is used to make sure the shape is a triangle
    # collinear formula checks if any points lie on the same straight line
    triangleArea = (
                           firstTriPointX * (secondTriPointY - thirdTriPointY) + secondTriPointX * (
                           thirdTriPointY - firstTriPointY) + thirdTriPointX * (
                                   firstTriPointY - secondTriPointY)) * 0.5
    # Draws the shape based on users inputs
    turtle.clearscreen()
    turtle.up()
    turtle.goto(firstTriPointX, firstTriPointY)  # Goes to first point
    turtle.down()
    turtle.goto(secondTriPointX, secondTriPointY)  # Draws first side
    turtle.goto(thirdTriPointX, thirdTriPointY)  # Draws second side
    turtle.goto(firstTriPointX, firstTriPointY)  # Draws third side
    # Another if else statement to check if shape is triangle.
    # Using collinear formula if the area ends up equaling zero then the shape is not a triangle
    # If not that means that some points are on the same line and the shape is not a triangle
    if triangleArea != 0:
        print("You got it right!")
    else:
        print("Sorry, that is not a triangle.")
        # elif used to see if user wants to draw a square
elif choice.lower() == "square":
    print("Great, show me a square!")
    # asks the user for coordinates of the points of a square
    firstSquPointX = int(input("Enter x coordinate of the first point: "))
    firstSquPointY = int(input("Enter y coordinate of the first point: "))
    secondSquPointX = int(input("Enter x coordinate of the second point: "))
    secondSquPointY = int(input("Enter y coordinate of the second point: "))
    thirdSquPointX = int(input("Enter x coordinate of the third point: "))
    thirdSquPointY = int(input("Enter y coordinate of the third point: "))
    fourthSquPointX = int(input("Enter x coordinate of the fourth point: "))
    fourthSquPointY = int(input("Enter y coordinate of the fourth point: "))
    # Draws the shape based on the user's inputted points
    turtle.clearscreen()
    turtle.up()
    turtle.goto(firstSquPointX, firstSquPointY)  # Goes to first point
    turtle.down()
    turtle.goto(secondSquPointX, secondSquPointY)  # Draws first side
    turtle.goto(thirdSquPointX, thirdSquPointY)  # Draws second side
    turtle.goto(fourthSquPointX, fourthSquPointY)  # Draws third side
    turtle.goto(firstSquPointX, firstSquPointY)  # Draws fourth side
    # Uses distance formula for two points to calculate if all sides are equal
    # Formula used for every side
    # distance formula:  ((x-x)^2 + (y-y)^2 )**1/2
    side1Distance = (((secondSquPointX - firstSquPointX) ** 2) + ((secondSquPointY - firstSquPointY) ** 2)) ** (1 / 2)
    side2Distance = (((thirdSquPointX - secondSquPointX) ** 2) + ((thirdSquPointY - secondSquPointY) ** 2)) ** (1 / 2)
    side3Distance = (((fourthSquPointX - thirdSquPointX) ** 2) + ((fourthSquPointY - thirdSquPointY) ** 2)) ** (1 / 2)
    side4Distance = (((firstSquPointX - fourthSquPointX) ** 2) + ((firstSquPointY - fourthSquPointY) ** 2)) ** (1 / 2)
    # USes distance formula to find if the two diagonals are equal
    diagonal1 = (((thirdSquPointX - firstSquPointX) ** 2) + ((thirdSquPointY - firstSquPointY) ** 2)) ** (1 / 2)
    diagonal2 = (((fourthSquPointX - secondSquPointX) ** 2) + ((fourthSquPointY - secondSquPointY) ** 2)) ** (1 / 2)
    # Uses another if else statement to see if the user's shape is a square
    # The shape is only a square if all the distances are equal and if the two diagonals equal as well
    if (side1Distance == side2Distance == side3Distance == side4Distance) and diagonal1 == diagonal2:
        print("You got it right!")
    else:
        print("Sorry, that is not a square.")
# Have exitonclick function to make the program end when user clicks on the turtle screen
turtle.exitonclick()
