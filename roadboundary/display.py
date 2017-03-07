from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def plot_point_cloud(point_cloud, elev=50, azim=250):
  array = np.asarray(point_cloud)
  fig = plt.figure(figsize=(12, 9))
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(array[:,0], array[:,1], array[:,2], c=array[:,2])
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Altitude')
  ax.view_init(elev, azim)
  plt.show()

def plot_point_cloud_with_original(point_cloud, original, elev=50, azim=250):
  array = np.asarray(point_cloud)
  original_array = np.asarray(original)
  fig = plt.figure(figsize=(12, 9))
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(original_array[:,0], original_array[:,1], original_array[:,2], c=original_array[:,2], alpha=0.1)
  ax.scatter(array[:,0], array[:,1], array[:,2], c='r')
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Altitude')
  ax.view_init(elev, azim)
  plt.show()

def plot_point_cloud_2d(point_cloud):
  array = np.asarray(point_cloud)
  fig = plt.figure(figsize=(12, 9))
  ax = fig.add_subplot(111)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  plt.scatter(array[:,0], array[:,1], c=array[:,2])
  plt.colorbar()
  plt.show()

def plot_clusters(point_cloud, db):
  array = np.asarray(point_cloud)
  labels = db.labels_
  core_samples_mask = np.zeros_like(labels, dtype=bool)
  unique_labels = set(labels)

  fig = plt.figure(figsize=(12, 9))
  ax = fig.add_subplot(111)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  colors = plt.cm.Spectral(np.linspace(0, 3, len(unique_labels)))

  for k, col in zip(unique_labels, colors):
    if k == -1:
      continue

    class_member_mask = (labels == k)

    xy = array[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)

    xy = array[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6)

  plt.show()
