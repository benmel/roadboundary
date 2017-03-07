import sys
import getopt
from roadboundary import main
import pcl

def run():
  def usage():
    print "python run.py <output_filename>.pcd"

  try:
    opts, args = getopt.getopt(sys.argv[1:], "h")
  except getopt.GetoptError:
    usage()
    sys.exit(2)

  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()

  if len(args) < 1:
    usage()
    sys.exit()

  point_cloud = main.get_road_boundary_point_cloud('data/final_project_point_cloud.fuse')
  pcl.save(point_cloud, args[0])

if __name__ == "__main__":
  run()
