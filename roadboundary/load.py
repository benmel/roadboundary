import numpy as np
import pcl
import utm

def coords_array_from_file(filepath):
  return np.loadtxt(filepath, dtype=np.float32)

def point_cloud_from_file(filepath):
  points_array = np.loadtxt(filepath, dtype=np.float32, usecols=(0,1,2))
  return pcl.PointCloud(points_array)

def meters_array_from_file(filepath):
  points_array = np.loadtxt(filepath, dtype=np.float32)
  for row in points_array:
    utm_coords = utm.from_latlon(*row[0:2])
    row[0] = utm_coords[0]
    row[1] = utm_coords[1]
  return points_array
