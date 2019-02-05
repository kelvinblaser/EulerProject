################################################################################
# Euler 395 - Pythagorean Tree
# Kelvin Blaser      2015.03.13
#
################################################################################
import scipy as sp
from scipy import stats
from scipy.spatial import ConvexHull
import pylab as pl


def pythagoreanArea():
    # Right and Left tree matrices
    leftTree = sp.array([[16,-12,0],[12,16,25],[0,0,25]],dtype=sp.float64)
    leftTree /= 25.0
    rightTree = sp.array([[9,12,16],[-12,9,37],[0,0,25]],dtype=sp.float64)
    rightTree /= 25.0

    # Starting values
    points = sp.array([[0,1,0,1],[0,0,1,1],[1,1,1,1]],dtype=sp.float64)
    xmin, xmax, ymin, ymax = 0,1,0,1
    A = 1
    delta = 1
    print '%0.11f\t%d\t%0.11f\t%0.11f\t%0.11f\t%0.11f'%(A,len(points[0,:]),xmin,
                                                        xmax,ymin,ymax)

    # Iterate tree some number of times
    while delta > 1e-12:
        # Create left and right tree points by matrix multiplication then
        # extract points
        ltree = leftTree.dot(points)
        rtree = rightTree.dot(points)
        points = sp.concatenate((ltree,rtree),1)

        # Find new min and max and calculate area
        #points_y = [x[1] for x in points]
        xmin = min(min(points[0,:]),xmin)
        xmax = max(max(points[0,:]),xmax)
        ymin = min(min(points[1,:]),ymin)
        ymax = max(max(points[1,:]),ymax)
        delta = (ymax - ymin)*(xmax - xmin) - A
        A = (ymax - ymin)*(xmax - xmin)

        # Reduce points
        try:
            hull = ConvexHull(points[:2,:].transpose())
            points = points[:,hull.vertices]
        except:
            print 'errrrrybody'
            
        # Print
        print '%0.11f\t%d\t%0.11f\t%0.11f\t%0.11f\t%0.11f'%(A,len(points[0,:]),
                                                            xmin,xmax,ymin,ymax)
    return A

if __name__ == '__main__':
    print pythagoreanArea()

        
        

    
