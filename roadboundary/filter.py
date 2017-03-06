import pcl
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

def altitude(point_cloud, min_percentile=3, max_percentile=85):
  array = np.asarray(point_cloud)
  min_threshold = np.percentile(array[:,2], min_percentile)
  max_threshold = np.percentile(array[:,2], max_percentile)
  fil = point_cloud.make_passthrough_filter()
  fil.set_filter_field_name('z')
  fil.set_filter_limits(min_threshold, max_threshold)
  return fil.filter()

def kd_tree_upsample(query_point_cloud, original_point_cloud, iterations=1):
  new_point_cloud = query_point_cloud
  kd_tree = pcl.KdTreeFLANN(original_point_cloud)
  for i in range(iterations):
    indices, sqr_distances = kd_tree.nearest_k_search_for_cloud(new_point_cloud, 6)
    all_indices = indices.flatten()
    unique_indices = np.unique(all_indices)
    new_point_cloud = original_point_cloud.extract(unique_indices)
  return new_point_cloud
