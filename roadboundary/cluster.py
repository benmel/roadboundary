from sklearn.cluster import DBSCAN
from scipy.interpolate import UnivariateSpline
import numpy as np
import math
from itertools import tee, izip

def dbscan(array):
  return DBSCAN(eps=2.0, min_samples=3).fit(array[:,[0,1]])

def get_clusters(array, db):
  labels = db.labels_
  unique_labels = set(labels)
  clusters = [array[labels == i] for i in unique_labels]
  return clusters

def get_clusters_above_threshold(clusters, threshold=30):
  keep_clusters = []
  for c in clusters:
    x, y = get_fitted_values(c)
    dist = get_fitted_distance(x, y)
    if dist > threshold:
      keep_clusters.append(c)
  return keep_clusters

def get_fitted_values(array):
  min_x = min(array[:,0])
  max_x = max(array[:,0])
  num_samples = int(math.ceil((max_x - min_x) * 10))
  x_new = np.linspace(min_x, max_x, num_samples)
  spline = UnivariateSpline(array[:,0], array[:,1])
  y_new = spline(x_new)
  return x_new, y_new

def get_fitted_distance(x, y):
  array = np.column_stack((x, y))
  dist = 0
  for a, b in pairwise(array):
    diff = b - a
    dist += math.sqrt(diff[0] ** 2 + diff[1] ** 2)
  if math.isnan(dist):
    return 0
  else:
    return dist

def pairwise(iterable):
  a, b = tee(iterable)
  next(b, None)
  return izip(a, b)
