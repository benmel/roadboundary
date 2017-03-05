import pcl

def normal_plane(point_cloud, distance_threshold=0.03, normal_distance_weight=0.1, negative=False):
  seg = point_cloud.make_segmenter_normals(ksearch=50)
  seg.set_optimize_coefficients(True)
  seg.set_method_type(pcl.SAC_RANSAC)
  seg.set_model_type(pcl.SACMODEL_NORMAL_PLANE)
  seg.set_normal_distance_weight(normal_distance_weight)
  seg.set_max_iterations(100)
  seg.set_distance_threshold(distance_threshold)
  indices, model = seg.segment()
  return point_cloud.extract(indices, negative)

def plane(point_cloud, distance_threshold=0.03, negative=False):
  seg = point_cloud.make_segmenter_normals(ksearch=50)
  seg.set_optimize_coefficients(True)
  seg.set_method_type(pcl.SAC_RANSAC)
  seg.set_model_type(pcl.SACMODEL_PLANE)
  seg.set_distance_threshold(distance_threshold)
  indices, model = seg.segment()
  return point_cloud.extract(indices, negative)

def line(point_cloud, distance_threshold=0.03, negative=False):
  seg = point_cloud.make_segmenter_normals(ksearch=50)
  seg.set_optimize_coefficients(True)
  seg.set_method_type(pcl.SAC_RANSAC)
  seg.set_model_type(pcl.SACMODEL_LINE)
  seg.set_distance_threshold(distance_threshold)
  indices, model = seg.segment()
  return point_cloud.extract(indices, negative)
