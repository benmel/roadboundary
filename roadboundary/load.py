import numpy as np
import pcl

def point_cloud_from_file(filepath):
  points_array = np.loadtxt(filepath, dtype=np.float32, usecols=(0,1,2))
  return pcl.PointCloud(points_array)
