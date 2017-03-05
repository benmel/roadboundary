import pcl

def normal_plane(point_cloud):
  seg = point_cloud.make_segmenter_normals(ksearch=50)
  seg.set_optimize_coefficients(True)
  seg.set_method_type(pcl.SAC_RANSAC)
  seg.set_model_type(pcl.SACMODEL_NORMAL_PLANE)
  seg.set_normal_distance_weight(0.1)
  seg.set_max_iterations(100)
  seg.set_distance_threshold(0.03)
  indices, model = seg.segment()
  return point_cloud.extract(indices)
