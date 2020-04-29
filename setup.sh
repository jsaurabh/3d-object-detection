#!/bin/bash

# setup lyft dataset sdk
#pip install lyft-dataset-sdk

# kaggle competitions data download
[ -d data ] || mkdir data
cd data

{
 kaggle competitions download -c 3d-object-detection-for-autonomous-vehicles 
} ||
{
echo "Kaggle API could not download the dataset. 
Make sure Kaggle API has been setup properly and/or you've entered the competition. Refer to README for instructions."
}

echo "Data downloaded successfully"
unzip 3d-object-detection-for-autonomous-vehicles.zip -q
cd ..
ln -s data/train_maps maps
ln -s data/train_images images
ln -s data/train_lidar lidar
echo "Data unzipped"