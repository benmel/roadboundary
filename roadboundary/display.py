from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def plot_array(array):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(array[:,0], array[:,1], array[:,2], c=array[:,2])
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Altitude')
  plt.show()

def plot_array_with_original(array, original):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(original[:,0], original[:,1], original[:,2], c=original[:,2], alpha=0.1)
  ax.scatter(array[:,0], array[:,1], array[:,2], c='r')
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Altitude')
  plt.show()

def plot_array_2d(array):
  fig = plt.figure()
  plt.scatter(array[:,0], array[:,1], c=array[:,2])
  plt.colorbar()
  plt.show()

def plot_clusters(array, db):
  labels = db.labels_
  core_samples_mask = np.zeros_like(labels, dtype=bool)
  unique_labels = set(labels)
  colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

  for k, col in zip(unique_labels, colors):
    if k == -1:
      continue

    class_member_mask = (labels == k)

    xy = array[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)

    xy = array[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6)

  plt.show()
