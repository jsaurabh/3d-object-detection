# 3D Object Detection for Autonomous Vehicles

This repository is my implementation of a UNet FCN for the Kaggle challenge [3D Object Detection for Autonomous Vehicles](https://www.kaggle.com/c/3d-object-detection-for-autonomous-vehicles/).

The task for the challenge is to implement a model for object detection over semantic maps that consist of multiple data sources, namely Lidar and camera input. This is a hard problem, and it should be fun to learn new things as I go through this challenge.

# Setup

Download the data directly from Kaggle. Setup the [Kaggle API](https://github.com/kaggle/Kaggle-API), accept the competition rules and then run

`bash setup.sh`

The script will install the Level5 dataset provided by Lyft, and also download the data from Kaggle, and organize it in the required directory structure. This should take a fair amount of time (say 90-95 minutes), so grab a coffee and come back in a while.

# Data

The dataset for the challenge is the Lyft Level5 dataset described. Lyft has provided an SDK for dealing with the data, making it easier for people to start training models. While I find dealing with and organizing data to be fun, this is a welcome change as the task itself is quite challenging. The sooner you can start, the better.

# Model

Head to the `unet.ipynb` notebook once you're done setting up the data structure.