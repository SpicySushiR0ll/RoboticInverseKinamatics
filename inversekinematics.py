import math
import math
from ast import increment_lineno

import matplotlib
matplotlib.use("MacOSX")  # IMPORTANT for PyCharm animation. Change according to ide
import matplotlib.pyplot as plt
import matplotlib.animation as animation

trail_x = []
trail_y = []

rows = 4 # number of points
cols = 2 # number of coordinates (x, y)

# inputted points are going to represent our "extreme" values or "frame" positions
point = [[0 for i in range(cols)] for j in range(rows)] # these are going to be our inputted points

 ## point [n][0] are going to be our x coordinates
 ## point [n][1] are going to be our y coordinates

point[0][0] = 0.0
point[0][1] = -130.0
point[1][0] = -25.0
point[1][1] = -43.3
point[2][0] = -50.0
point[2][1] = -130.0
point[3] = point[0] ## Making sure that the end effector goes back to the start position

allPoints = {} # these are going to be found using interpolation later. They represnt all postions
allPoints[0] = point[0] # initializing the first as the the first key frame


 ## declaring our variables / characteristics of the leg

thigh1 = 100.00
thigh2 = 100.00
tibby1 = 25.00
tibby2 = 75.00
originX  = 0.0
originY = 0.0

##  setting our joints up
j0 = {} # this is a constant. For every calculation made, we set this eaqul to 0,0
j1 = {}
j2 = {}
j3 = {}
f0 = {} # this is our end effector aka the food

drawOrder = [j0,j1,f0,j2,j3, j0] # This determines the order in which we draw our lines. The grapgh is a continuous line so keep that in mind. This array is how we orginize our coordinates for later

xVals = {} # we are going to split our values into x and y coordinates later
yVals = {} # these are organized such that the row number is your point and your column number is your joint. The data is ur x and y

## now onto our calculations

def distance(X1,Y1,X2,Y2): # finds distance between two points using Pythagorean theorem
    return math.sqrt((X1 - X2)**2 + (Y1 - Y2)**2)

def angle (opposite, adjacent): # finds angle using arctan
    #base case
    if adjacent == 0: # we cant device by zero
        return 0
    else:
        return math.atan(opposite/adjacent)

def lawOfCosineAngle (side1, side2, oppositeSide): # uses law of cosines to find the missing angle
    return math.acos(((oppositeSide**2) - (side1**2) - (side2**2)) / (-2 * side1 * side2))

def lineExtension (A, B, L, case): # using the position of two joints, it repositions the second joint a certain angle distance away

    dX = B[0] - A[0]
    dY = B[1] - A[1]

    theta = math.atan(dY/dX)
   

    if case == 0: # this is the special case where we are starting from a frame position
        if (dX > 0 and dY > 0): 
            solution = [A[0] + L * math.cos(theta), A[1] + L * math.sin(theta)]
        elif (dX < 0 and dY > 0): 
            solution = [A[0] - L * math.cos(theta), A[1] - L * math.sin(theta)]
        elif (dX > 0 and dY < 0):
            solution = [A[0] + L * math.cos(theta), A[1] + L * math.sin(theta)]
        else: # for sure good
            solution = [A[0] - L * math.cos(theta), A[1] - L * math.sin(theta)]
    else:
        if (dX > 0 and dY > 0): 
            solution = [B[0] + L * math.cos(theta), B[1] + L * math.sin(theta)]
        elif (dX < 0 and dY > 0): 
            solution = [B[0] - L * math.cos(theta), B[1] - L * math.sin(theta)]
        elif (dX > 0 and dY < 0): 
            solution = [B[0] + L * math.cos(theta), B[1] + L * math.sin(theta)]
        else: 
            solution = [B[0] - L * math.cos(theta), B[1] - L * math.sin(theta)]

    return solution

# this function finds the intersection of two circles in order to find the locations of an unknown joint
def circIntersection(jointA, jointB, lengthA, lengthB):
    xA, yA = jointA
    xB, yB = jointB
    Lc = math.hypot(xA - xB, yA - yB)
    bb = ((lengthB ** 2) - (lengthA ** 2) + (Lc ** 2)) / (2 * Lc)
    h = math.sqrt(lengthB ** 2 - bb ** 2)

    Xp = xB + bb * (xA - xB) / Lc
    Yp = yB + bb * (yA - yB) / Lc

    solution1 =[ Xp - h * (yB - yA) / Lc, Yp + h * (xB - xA) / Lc]

    return solution1

def calc(i, point): # this function calculates the values for a given point
    ### KEY ASUMPTION: The foot is always in quadrent 3 (the limits being the x and y axis).

    j0[i] = [0.0,0.0] # this is the joint where the motor is so its gunna stay here
    
    f0[i] = [point[i][0], point[i][1]] # this is the foot

    ## finding the angle between the larger thigh and the x axis and defining it as theta 1

    c1 = distance(originX, originY, allPoints[i][0], allPoints[i][1]) # distance from motor / j0 to the end effector (the foot)

    ## we need a special case for when the foot is on the x or y axis
    
    if allPoints[i][0] == 0:
        alpha = lawOfCosineAngle(c1,thigh1, tibby2)
        theta1 = alpha - ((math.pi)/2) ## theta 1 should always be understood to be negative
        
    elif allPoints[i][1] == 0:
        theta1 = lawOfCosineAngle(c1,thigh1, tibby2) # if the foot is on the x axis, there is no need for alpha
        alpha = theta1
        
    else:
        alpha = angle(allPoints[i][0] , allPoints[i][1])  # adjacent side is our x, opposite is the y
        theta1 = lawOfCosineAngle(thigh1, c1, tibby2) - alpha

    ## finding the position of j1
    theta1 = abs(theta1) ## trying this for simplicity
    theta4 = (math.pi)/2 - lawOfCosineAngle(c1, tibby2, thigh1)

    # storing position of joint one in dictionary
    j1[i] = circIntersection(f0[i], j0[i], tibby2, thigh1)

    ## finding the position of j2
    j2[i] = lineExtension(allPoints[i], j1[i], tibby1,1)

    ## finding the angle needed for the upper thigh / motor two and the normal
    j3[i] = circIntersection(j2[i], j0[i], 100, 35)
    theta2 = angle(j3[i][0], j3[i][1])

    xVals[i], yVals[i] =  splitXY(i)
     ## print(distance(*j2[i], *f0[i])) # used this to check for consitent segment lengths


def interpolate(pointA, pointB, increment, counter):
    ## this function is going to take two points and make a straight line path in between them
    # we are going to do this by going an "increment" distance closer to the second point each time

    totalDistance = distance(pointA[0], pointA[1], pointB[0], pointB[1])  # total distance between the two points

    p1 = pointA
    p2 = pointB
    theta = angle(pointA[0] - pointB[0], pointA[1]-pointB[1])
    tolerence = 0.5 # the newpoint is within 0.5 mm we just round it over to equal point b


    while (distance(*allPoints[counter],*pointB) > tolerence):  ## we keep extending the line until the new point equal to point b

        allPoints[counter+1] = lineExtension(allPoints[counter-1], allPoints[counter], increment, 1)  # extend line
        ## print(allPoints[counter+1])

        if (distance(*allPoints[counter], *pointA) > totalDistance):   # make sure we didn't go too far
            allPoints[counter] = pointB
            break

        counter += 1  # add to counter

def splitXY(i):
    xs, ys = [], []
    for j in drawOrder:
        xs.append(j[i][0])
        ys.append(j[i][1])
    return xs, ys

# Over view of code structure
 # We input our "Frame" postions into an array and figure out the inbetween poitions too
 # We then calclulate the position for every joint at every position
 # Then take take each x and y coordinates and put it in a dictionary that uses the positions as keys
 # each key leads to another dictionary that uses the joints as key
 # These keys lead to the coordinates of the joint

## So how do we structure this
 # We first need our extreme positions
 # We then need our inbetween positions (The number of these is going to be determined by the increments i think)
 # And then we finally just calculate all the joint positions

## so lets get started

## extreme positions = the points array at the top

## inbetween positions

increment = 5 # All points are going to me this far apart

for j in range(len(point)-1): ## go through all extreme points
    nextKey = max(allPoints.keys()) + 1
    allPoints[nextKey] = lineExtension(allPoints[nextKey - 1], point[j+1], increment,0)
    interpolate(point[j], point[j+1],increment, int(len(allPoints)-1))

## now we need to calculate the joint positions and thetas
for i in allPoints:
    calc(i, allPoints)

## now we animate
fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(-200, 100)
ax.set_ylim(-200, 100)

line, = ax.plot([], [], '-o', lw=3)
lineR, = ax.plot([], [], '-o', lw=3)
trail_plot, = ax.plot([], [], 'r-', lw=2) # trail
point_plot, = ax.plot([], [], 'ro')      # moving point

maxTrailLength = 30

def animate(i):
    x = allPoints[i][0]
    y = allPoints[i][1]

    line.set_data([xVals[i]], [yVals[i]])
    lineR.set_data([xVals[i]], [yVals[i]])


    point_plot.set_data([x],[y])

    trail_x.append(x)
    trail_y.append(y)
    trail_x[:] = trail_x[-maxTrailLength:]
    trail_y[:] = trail_y[-maxTrailLength:]
    trail_plot.set_data(trail_x,trail_y)

    return line, lineR, point_plot, trail_plot

ani = animation.FuncAnimation(fig, animate,frames = len(allPoints), interval=100, blit=True)

plt.show()
