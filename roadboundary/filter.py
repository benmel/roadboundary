def statistical_outlier(point_cloud):
  fil = point_cloud.make_statistical_outlier_filter()
  fil.set_mean_k(50)
  fil.set_std_dev_mul_thresh(1.0)
  return fil.filter()

def voxel_grid(point_cloud):
  fil = point_cloud.make_voxel_grid_filter()
  fil.set_leaf_size(0.1, 0.1, 0.1)
  return fil.filter()  
