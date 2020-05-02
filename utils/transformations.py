import numpy as np

def transformation2voxel(shape, size, offset):
    shape, size, offset = np.array(shape), np.array(size), np.array(offset)
    
    tm = np.eye(4, dtype = np.float32)
    translation = shape/2 + offset/size
    
    tm = tm * np.array(np.hstack((1/size, [1])))
    tm[:3, 3] = np.transpose(translation)
    return tm

def transform(points, matrix):
    if points.shape[0] not in [3,4]:
        raise Exception("Points input should be (3,N) or (4,N) shape, received {}".format(points.shape))
    return matrix.dot(np.vstack((points[:3, :], np.ones(points.shape[1]))))[:3, :]

def car2voxel(points, shape, size, z_offset = 0):
    if len(shape) != 3:
        raise Exception("Voxel volume shape should be 3 dimensions (x,y,z)")
        
    if len(points.shape) != 2 or points.shape[0] not in [3, 4]:
        raise Exception("Input points should be (3,N) or (4,N) in shape, found {}".format(points.shape))

    tm = transformation2voxel(shape, size, (0, 0, z_offset))
    p = transform(points, tm)
    return p

def createPointCloud(points, shape, size = (0.5,0.5,1), z_offset = 0):

    points_voxel_coords = car2voxel(points.copy(), shape, size, z_offset)
    points_voxel_coords = points_voxel_coords[:3].transpose(1,0)
    points_voxel_coords = np.int0(points_voxel_coords)
    
    bev = np.zeros(shape, dtype=np.float32)
    bev_shape = np.array(shape)

    within_bounds = (np.all(points_voxel_coords >= 0, axis=1) * np.all(points_voxel_coords < bev_shape, axis=1))
    
    points_voxel_coords = points_voxel_coords[within_bounds]
    coord, count = np.unique(points_voxel_coords, axis=0, return_counts=True)
        
    bev[coord[:,1], coord[:,0], coord[:,2]] = count
    return bev

def normalizeVoxels(bev, max_intensity = 16):
    return (bev/max_intensity).clip(0,1)

