import numpy as np
import matplotlib.pyplot as plt

def calculate_euclidean_distance(a, b):
    return np.linalg.norm(a - b)

def single_linkage(data_points):
    num_points = len(data_points)
    clusters = [[i] for i in range(num_points)]

    while len(clusters) > 1:
        min_distance = float('inf')
        merge_indices = (0, 0)

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                cluster_i = clusters[i]
                cluster_j = clusters[j]

                distance = min(calculate_euclidean_distance(data_points[p1], data_points[p2]) for p1 in cluster_i for p2 in cluster_j)

                if distance < min_distance:
                    min_distance = distance
                    merge_indices = (i, j)

        i, j = merge_indices
        clusters[i].extend(clusters[j])
        del clusters[j]

    return clusters[0]

# Input data
num_points = int(input("Enter the number of data points: "))
data_points = []

for i in range(num_points):
    x = float(input(f"Enter x-coordinate for point {i+1}: "))
    y = float(input(f"Enter y-coordinate for point {i+1}: "))
    data_points.append(np.array([x, y]))

# Perform hierarchical clustering with single linkage
single_clusters = single_linkage(data_points)

# Display single linkage clusters
print("Single Linkage Clusters:", single_clusters)
