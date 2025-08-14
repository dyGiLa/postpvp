from vtk.numpy_interface import dataset_adapter as dsa
from vtk.numpy_interface import algorithms as algs

import numpy as np
from collections import Counter

import matplotlib.pyplot as plt

labeled_pMCluster_Arr=inputs[0].PointData['Labeled-clusters']

print("pMarker_Array : ", labeled_pMCluster_Arr)

# Get only the non-zero (occupied) labels
labels = labeled_pMCluster_Arr[labeled_pMCluster_Arr > 0]

# Count how many times each label appears (i.e., cluster size)
label_counts = Counter(labels)

# Now count how many clusters are of each size
size_distribution = Counter(label_counts.values())

total_clusters = np.sum(list(size_distribution.values()))
normalized_dist = {size: count / total_clusters for size, count in size_distribution.items()}

sizes = sorted(normalized_dist.keys())
probs = [normalized_dist[size] for size in sizes]

sizes2 = sorted(size_distribution.keys())
sizeNum = [size_distribution[size] for size in sizes2]

# Stack as rows first
combined = np.vstack((sizes, probs, size2, sizeNum))

# Transpose to get desired shape
combined = combined.T

# Save to CSV
np.savetxt("cluster-prob-num.csv", combined, delimiter=",", fmt="%.8f")

fig, ax = plt.subplots(1,1)

#ax.plot(sizes, probs, marker='o', linestyle='-', color='blue')
ax.scatter(sizes, probs, marker='o', color='blue')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Cluster Size (log scale)')
ax.set_ylabel('Probability (log scale)')
ax.set_title('Cluster Size Probability Distribution')
ax.grid(True, which="major", ls="-")

fig.savefig('/home/heidi/Documents/dyGiLa-project/dyGiLa-pvpython-scripts/Phase-Cluster-Counting/cluster_prob_distribution.png')

##########################



fig2, ax2 = plt.subplots(1,1)

#ax.plot(sizes, probs, marker='o', linestyle='-', color='blue')
ax2.scatter(sizes2, sizeNum, marker='o', color='blue')
ax2.set_xscale('log')
ax2.set_yscale('linear')
ax2.set_xlabel('Cluster Size (log scale)')
ax2.set_ylabel('clustrer number (log scale)')
ax2.set_title('Cluster Size Distribution')
ax2.grid(True, which="major", ls="-")

fig2.savefig('/home/heidi/Documents/dyGiLa-project/dyGiLa-pvpython-scripts/Phase-Cluster-Counting/cluster_num_distribution.png')
