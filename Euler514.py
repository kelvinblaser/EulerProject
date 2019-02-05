################################################################################
# Euler 514 - Geoboard Shapes
# Kelvin Blaser      2015.05.20
#
# Enumerate possible geoboard shapes
# Calculate Area and probability
# Sum
################################################################################
from numpy import arctan2, pi

def polygon_gen(N):
    points = [(x,y) for x in range(-N,N+1) for y in range(N+1)
              if y > 0 or x > 0]
    for p in points:
        for poly in polygon_gen_recurse(N,[(0,0),p],points):
            yield poly

def polygon_gen_recurse(N,poly,points):
    x_max = max([p[0] for p in poly])
    x_min = min([p[0] for p in poly])
    new_points = [p for p in points
                  if angle(poly[-1],p) > angle(poly[-2],poly[-1])
                  and angle(poly[-1],p) < angle(p,poly[0])
                  and p[0] - x_min <= N
                  and x_max - p[0] <= N]
    for p in new_points:
        yield poly + [p,]
        for pg in polygon_gen_recurse(N,poly+[p,], new_points):
            yield pg
    
def angle(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    phi = arctan2(y2-y1,x2-x1)
    if phi < 0:
        phi += 2*pi
    return phi
