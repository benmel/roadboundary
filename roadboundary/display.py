from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plot_array(array):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(array[:,0], array[:,1], array[:,2], c=array[:,2])
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Altitude')
  plt.show()

def plot_array_with_original(array, original):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(original[:,0], original[:,1], original[:,2], c='r', alpha=0.1)
  ax.scatter(array[:,0], array[:,1], array[:,2], c=array[:,2])
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Altitude')
  plt.show()

def plot_array_2d(array):
  fig = plt.figure()
  plt.scatter(array[:,0], array[:,1], c=array[:,2])
  plt.colorbar()
  plt.show()
