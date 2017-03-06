import numpy as np

def statistical_outlier(point_cloud):
  fil = point_cloud.make_statistical_outlier_filter()
  fil.set_mean_k(50)
  fil.set_std_dev_mul_thresh(1.0)
  return fil.filter()

def voxel_grid(point_cloud):
  fil = point_cloud.make_voxel_grid_filter()
  fil.set_leaf_size(0.1, 0.1, 0.1)
  return fil.filter()

def altitude_threshold(point_cloud, min_percentile=1, max_percentile=90):
  array = np.asarray(point_cloud)
  min_threshold = np.percentile(array[:,2], min_percentile)
  max_threshold = np.percentile(array[:,2], max_percentile)
  fil = point_cloud.make_passthrough_filter()
  fil.set_filter_field_name('z')
  fil.set_filter_limits(min_threshold, max_threshold)
  return fil.filter()
