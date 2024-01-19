import numpy as np
import matplotlib.pyplot as plt

def calculate_euclidean_distance(a, b):
    return np.linalg.norm(a - b)

def average_linkage(data_points):
    num_points = len(data_points)
    clusters = [[i] for i in range(num_points)]

    while len(clusters) > 1:
        min_distance = float('inf')
        merge_indices = (0, 0)

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                cluster_i = clusters[i]
                cluster_j = clusters[j]

                distance = sum(calculate_euclidean_distance(data_points[p1], data_points[p2]) for p1 in cluster_i for p2 in cluster_j) / (len(cluster_i) * len(cluster_j))

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

# Perform hierarchical clustering with average linkage
average_clusters = average_linkage(data_points)

# Display average linkage clusters
print("Average Linkage Clusters:", average_clusters)
