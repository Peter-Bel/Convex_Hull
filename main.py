import random

size = 8;
range_max = 10;

# coordinate data type
class coordinate_class:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Set the coordinate values
coordinates = [coordinate_class(random.randint(0, range_max-1),
                       random.randint(0, range_max-1))
               for _ in range(size)]

# set coordinate locations 
for xx in range(range_max):
    for yy in range(range_max):
        print_sym = " - ";
        for i in range(len(coordinates)):
            if (coordinates[i].x == xx and coordinates[i].y == yy):
                print_sym = " * ";
        print(print_sym, end="");
    print("");

# print coordinates
for i in coordinates:
    print( "(", i.x, ",", i.y, ")", end="");
print("");

# set convex hull
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# A utility function to find next
# to top in a stack
def nextToTop(S):
    a = S.pop()
    b = S.pop()
    S.append(a)
    return b

# swap points
def swap(p1, p2):
    return p2, p1

# return square of 2 points
def distSq(p1, p2):
    return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)

# Prints convex hull of a set of n
def convexHull(points, n):
    # There must be at least 3 points
    if (n < 3):
        return

    # Initialize Result
    hull = []

    # Find the leftmost point
    l = 0
    for i in range(1, n):
        if (points[i].x < points[l].x):
            l = i

    p = l
    q = 0
    while (True):
        hull.append(points[p])
        q = (p + 1) % n

        for i in range(0, n):
            # current q, then update q
            if (orientation(points[p], points[i], points[q]) == 2):
                q = i

        # Now q is the most counterclockwise with
        p = q

        # While we don't come to first point
        if (p == l):
            break

    # Print Result
    printHull(hull)

# return square of distance between p1 and p2
def distSq(p1, p2):
    return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)

# To find orientation of ordered triplet (p, q, r).
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if (val == 0):
        return 0  # collinear
    elif (val > 0):
        return 1   # clock or wise
    else:
        return 2   # counterclock or wise

# Prints convex hull of a set of n points.
def printHull(hull):
    print("The points in Convex Hull are:")
    for i in range(len(hull)):
        print("(", hull[i].x, ", ", hull[i].y, ")")


# apply convex hull
convexHull(coordinates, size);
