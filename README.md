# roadboundary

This application extracts a road boundary from a point cloud.

## Requirements

The required packages are listed in requirements.txt. They are: numpy, Cython, matplotlib, utm, scipy and scikit-learn. The Point Cloud Library is a dependency. python-pcl is also needed.

## Usage

The application is run with run.py, for example "python run.py /Users/ben/Desktop/output.pcd". The input point cloud should be saved at data/final_project_point_cloud.fuse. The output will be a PCD file containing only the road boundary point cloud.

## Approach

Six steps are used in extracting the road boundary: filtering, segmentation, clustering, spline, upsample and altitude threshold. The application can successfully extract a guardrail from the test data.