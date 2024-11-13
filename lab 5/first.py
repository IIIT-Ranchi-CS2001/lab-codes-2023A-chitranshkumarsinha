import math
first = (1,2,3)
second = (4,5,6)

d1 = (second[0]-first[0])**2
d2 = (second[2]-first[2])**2
d3 = (second[1]-first[1])**2
f = d1+d2+d3

distance = math.sqrt(f)
print(distance)