import load
import filter
import segment
import cluster
import pcl
import numpy as np

def get_road_boundary_point_cloud(filepath):
  meters_array = load.meters_array_from_file(filepath)
  point_cloud = pcl.PointCloud(meters_array[:,[0,1,2]])
  pc_filtered = filter.statistical_outlier(point_cloud)
  pc_voxel = filter.voxel_grid(pc_filtered)
  pc_minus_roads = segment.normal_plane(pc_voxel, distance_threshold=0.5, negative=True)
  pc_boundary = segment.normal_plane(pc_minus_roads, distance_threshold=1.0)
  pc_array = np.asarray(pc_boundary)
  db = cluster.dbscan(pc_array)
  clusters_array = cluster.get_clusters(pc_array, db)
  thresholded_clusters_array = cluster.get_clusters_above_threshold(clusters_array, threshold=30)
  pc_clusters = pcl.PointCloud(np.concatenate(thresholded_clusters_array))
  pc_upsampled = filter.kd_tree_upsample(pc_clusters, point_cloud, iterations=10)
  pc_final = filter.altitude(pc_upsampled, min_percentile=3, max_percentile=85)
  return pc_final
