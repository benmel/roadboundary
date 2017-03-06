import load
import filter
import segment
import cluster
import pcl
import numpy as np

def find_road_boundary(filepath):
  meters_array = load.meters_array_from_file(filepath)
  point_cloud = pcl.PointCloud(meters_array[:,[0,1,2]])
  pc_filtered = filter.statistical_outlier(point_cloud)
  pc_voxel = filter.voxel_grid(pc_filtered)
  pc_minus_roads = segment.normal_plane(pc_voxel, distance_threshold=0.5, negative=True)
  pc_boundary = segment.normal_plane(pc_minus_roads, distance_threshold=1.0)
  pc_array = np.asarray(pc_boundary)
  db = cluster.dbscan(pc_array)
  pc_clusters = cluster.get_clusters(pc_array, db)
  pc_final_clusters = cluster.get_clusters_above_threshold(pc_clusters, threshold=30)
  pc_final = pcl.PointCloud(np.concatenate(pc_final_clusters))
  return pc_final
