D = {'a':[19,15,39],'b':[21,15,81],'c':[20,16,6] ,'d':[23,16,77], 'e':[31,17,40], 'f':[22,17,76],
     'g':[35,18,6],  'h':[23,18,94], 'i':[64,19,3] , 'j':[30,19,72]}

# create centroids
centroids = {}
alpha = ['a','b','c']
for i in alpha:
    l= []
    for j in range(1,4):
        a = float(input(f"Enter {i}.{j} number: "))    # i represent number of cetroid
        l.append(a)
    centroids[i]=l

# prints centroids
print("Centroids")
for c,value in centroids.items():
    print(c,value)

# prints data points
print("\nData points")
for i,j in D.items():
    print(i,j)


def euclidean_distance(p1, p2):
    return (((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2) + ((p1[2]-p2[2])**2))**(1/2)


distances = {}

for p_key, point in D.items():
    distances[p_key] = {}
    
    for c_key, centroid in centroids.items():
        dist = euclidean_distance(point, centroid)
        distances[p_key][c_key] = round(dist, 2)

for point, dists in distances.items():
    print(f"\nPoint {point}:")
    for centroid, dist in dists.items():
        print(f"  Distance to centroid {centroid}: {dist}")