import load
import filter
import segment
import pcl

def find_road_boundary(filepath):
  meters_array = load.meters_array_from_file(filepath)
  point_cloud = pcl.PointCloud(meters_array[:,[0,1,2]])
  pc_filtered = filter.statistical_outlier(point_cloud)
  pc_voxel = filter.voxel_grid(pc_filtered)
  pc_minus_roads = segment.normal_plane(pc_voxel, distance_threshold=0.5, negative=True)
  pc_boundary = segment.normal_plane(pc_minus_roads, distance_threshold=1.0)
  return pc_boundary
