from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plot_array(array):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(array[:,1], array[:,0], array[:,2], c=array[:,3], cmap='gray')
  ax.set_xlabel('Longitude')
  ax.set_ylabel('Latitude')
  ax.set_zlabel('Altitude')
  plt.show()
