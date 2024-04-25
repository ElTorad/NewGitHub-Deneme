points = ((2,0),(-6,6))

def euclideanDistance(point1,point2):
    distance_1 = abs(point1[0] - point2[0])
    distance_2 = abs(point1[1] - point2[1])
    return ((distance_1 ** 2) + (distance_2 ** 2)) ** 0.5
    
print(euclideanDistance(points[0], points[1]))
