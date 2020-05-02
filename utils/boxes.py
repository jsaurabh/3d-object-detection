import numpy as np
import cv2 as cv

from lyft_dataset_sdk.utils.data_classes import LidarPointCloud, Box, Quaternion
from utils.transformations import car2voxel

def moveBoxesToCar(boxes, ego_pose):
    """
    Move boxes from world space to car space.
    Note: mutates input boxes.
    """
    translation = -np.array(ego_pose['translation'])
    rotation = Quaternion(ego_pose['rotation']).inverse
    
    for box in boxes:
        box.translate(translation)
        box.rotate(rotation)
    
    return boxes

def scaleBoxes(boxes, factor):
    for box in boxes:
        box.wlh = box.wlh * factor
    
    return boxes
        

    return image