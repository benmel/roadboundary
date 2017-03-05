from sklearn.cluster import DBSCAN

def dbscan(array):
  return DBSCAN(eps=2.0, min_samples=3).fit(array[:,[0,1]])
