import math

points = [(15,4),(8,-7),(-5,-22)]
distances = []

def euclideanDistance(point1,point2):
    return math.dist(point1,point2)

for i in range(len(points)):
    for j in range(i+1,len(points)):
        distances.append(euclideanDistance(points[i],points[j]))

print("Minimum Distance:",min(distances))