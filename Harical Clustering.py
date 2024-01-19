import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

def calculate_euclidean_distance(a, b):
    return np.linalg.norm(a - b)

num_points = int(input("Enter the number of data points: "))
data_points = []

for i in range(num_points):
    x = float(input(f"Enter x-coordinate for point {i+1}: "))
    y = float(input(f"Enter y-coordinate for point {i+1}: "))
    data_points.append([x, y])

data_points = np.array(data_points)

condensed_distance_matrix = pdist(data_points)
distance_matrix = np.zeros((data_points.shape[0], data_points.shape[0]))

for i in range(data_points.shape[0]):
    for j in range(data_points.shape[0]):
        distance_matrix[i][j] = calculate_euclidean_distance(data_points[i], data_points[j])

print("Euclidean Distance Matrix:")
for i in range(data_points.shape[0]):
    for j in range(data_points.shape[0]):
        print(f"{distance_matrix[i][j]:.2f}", end="\t")
    print()

single_linkage = linkage(condensed_distance_matrix, method='single')
single_clusters = dendrogram(single_linkage, no_plot=True)['ivl']

complete_linkage = linkage(condensed_distance_matrix, method='complete')
complete_clusters = dendrogram(complete_linkage, no_plot=True)['ivl']

average_linkage = linkage(condensed_distance_matrix, method='average')
average_clusters = dendrogram(average_linkage, no_plot=True)['ivl']

print("Single Linkage Clusters:", single_clusters)
plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram (Single Linkage)')
plt.xlabel('Data Points')
plt.ylabel('Distance')
dendrogram(single_linkage)
plt.show()

print("Complete Linkage Clusters:", complete_clusters)
plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram (Complete Linkage)')
plt.xlabel('Data Points')
plt.ylabel('Distance')
dendrogram(complete_linkage)
plt.show()

print("Average Linkage Clusters:", average_clusters)
plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram (Average Linkage)')
plt.xlabel('Data Points')
plt.ylabel('Distance')
dendrogram(average_linkage)
plt.show()
