from math import *

# Function to calculate the correlation coefficient
def correl(x,y):
    n=len(x)
    if(len(x)!=len(y)):
        sys.exit("Lists must have the same length\n")

    # Set counters to zero
    sx=0
    sy=0
    sxx=0
    sxy=0
    syy=0

    # Loop over each week of the data
    for a in range(n):

        # Convert the data to floating point, and
        # skip if it's a blank entry
        xx=x[a].strip()
        yy=y[a].strip()
        if xx=='' or yy=='':
            continue
        xx=float(xx)
        yy=float(yy)

        # Add this data to the counters
        sx+=xx
        sy+=yy
        sxx+=xx*xx
        sxy+=xx*yy
        syy+=yy*yy

    # Calculate variance and covariance
    sx/=n
    sy/=n
    varx=sxx/n-sx*sx
    covxy=sxy/n-sx*sy
    vary=syy/n-sy*sy

    # Calculate correlation
    return covxy/sqrt(varx*vary)

