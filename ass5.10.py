#WAP to accept coordinates of point and determine in which Quadrant it lies
X  = int(input('Enter value for X-axis :'))
Y = int(input('Enter value for Y-axis :'))
#check for 1st quadrant
if X > 0 and Y > 0:
    print('X and Y lie at First quadrant')
#check for 2nd quadrant
elif X < 0 and Y > 0:
    print('X and Y lie at Second quadrant')
#check for 3rd quadrant
elif X < 0 and Y < 0:
    print('X and Y lie at Third quadrant')
#check for fourth quadrant
elif X > 0 and Y < 0:
    print('X and Y lie at Fourth quadrant')
else:
    print('X and Y lie at Origin')