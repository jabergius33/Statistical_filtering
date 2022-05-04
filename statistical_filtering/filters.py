import numpy as np
from sklearn.neighbors import KDTree
from numpy import linalg as LA


def DSOR(P, Sfactor:float, r:float, k:int=4):
    """
    Implementation of Dynamic Statistical Outlier Removal algorithm
    
    Inputs:
    P = Point cloud dataset ((x,y,z).....)
    Kneighbour = minimum number of nearest neighbors
    Sfactor = multiplication factor for standard deviation
    r = multiplication factor for range
    
    Returns:
    Mask where 1 means outlier
    """
    P= P[:, :3] 
    tree = KDTree(P, leaf_size=50, metric='manhattan')  #Create a KD tree (euclidean)
    dist, i = tree.query(P, k=k+1)
    mean_dist = dist.mean(axis=1)

    #calculate:
    mean = np.mean(mean_dist)
    std = np.std(mean_dist) 
    threshold_g = mean + (std * Sfactor)
    
    distance = P[:, :3]*P[:, :3] 
    distance = distance.sum(axis=1)**.5
    mask = [mean_d >= (threshold_g * r * d) for mean_d, d in zip(mean_dist, distance)]

    return np.asarray(mask, dtype=np.bool)


def DROR(P, b=3, alpha=0.16, kmin=4, SRmin=0.04, rp=2):
    """
    Dynamic Radius Outlier Removal
    
    Inputs:
    P : the raw point cloud containing all points p
    b : multiplication factor
    alpha : horizontal angular resolution of the lidar
    kmin : minimum number of neighbors
    SRmin : minimum search radius
    rp : the range from the sensor to the point p
    
    Returns:
    Mask where 1 means outlier
    """
    P= P[:, :3] 
    tree = KDTree(P ,leaf_size=50 , metric='manhattan')  # leaf_size=5
    #rp = P[:,:2]*P[:,:2]
    #rp = rp.sum(axis=1)**.5  
    LA.norm(P1[:,:2],axis=1)

    search_radius = np.ndarray((P.shape[0],))
    for index, radius in enumerate(rp):
        rp = SRmin if radius < SRmin else b * (radius * alpha)
        search_radius[index] = rp
        
    number_of_neighbours = tree.query_radius(P, r=search_radius, count_only=True) # this line eats cpu time
    mask = [n < kmin for n in number_of_neighbours]
            
    return np.asarray(mask, dtype=np.bool)



def LIOR(P, search_radius=0.1, kmin=3, Sdr=71.235, Ithreshold= 0.066):
    """
    Dynamic Radius Outlier Removal
    
    Inputs:
    P : the raw point cloud containing all points p
    search_radius : minimum search radius (0.1 meter)
    kmin : minimum number of neighbors (3)
    Sdr :  Snow detection range (71 meter)
    threshold = Intensity threshold constant
    
    Returns:
    Mask where 1 means outlier
    
    """
    P1 = P.copy()
    distance = LA.norm(P1[:,:3],axis=1)
    mask1 = distance >= Sdr
    P1[mask1, -1] = 0

    tree = KDTree(P1[:, :3] , leaf_size=50, metric='manhattan')  #Create a KD tree
    number_of_neighbours = tree.query_radius(P1[:, :3], r=search_radius, count_only=True)
    

    mask1 = number_of_neighbours <= kmin
    mask2 = P1[:, -1] <= Ithreshold

    return mask1 & mask2



def DSOR_and_LIOR(P, search_radius=0.05, k=4, Sdr=288, Ithreshold= 0.066,  Sfactor:float=0.04, r:float=0.08):
    """

    Inputs:
    P : the raw point cloud containing all points p
    search_radius : minimum search radius 
    k : minimum number of neighbors
    Sdr :  Snow detection range 
    threshold = Intensity threshold constant

     ...
    k = minimum number of nearest neighbors
    Sfactor = multiplication factor for standard deviation
    r = multiplication factor for range


    Returns:
    Mask where 1 means outlier

    """
    #Lior
    P1 = P.copy()
    #distance = P[:, :3]*P[:, :3] 
    #distance = distance.sum(axis=1)**.5
    distance = LA.norm(P[:,:3],axis=1)
    mask1 = distance >= Sdr
    P1[mask1, -1] = 0

    tree = KDTree(P1[:, :3] , leaf_size=50, metric='manhattan')  #Create a KD tree
    number_of_neighbours = tree.query_radius(P1[:, :3], r=search_radius, count_only=True)

    mask1 = number_of_neighbours <= k
    mask2 = P1[:, -1] <= Ithreshold


    #Dsor
    dist, i = tree.query(P1[:, :3] , k=k+1)
    mean_dist = dist.mean(axis=1)


    mean = np.mean(mean_dist)
    std = np.std(mean_dist) 
    threshold_g = mean + (std * Sfactor)
    
    distance = LA.norm(P[:,:3],axis=1)
    
    mask3 = [mean_d >= (threshold_g * r * d) for mean_d, d in zip(mean_dist, distance)]

    return mask1 & mask2 & mask3



def DROR_and_LIOR(P, search_radius=0.05, k=3, Sdr=144, Ithreshold= 0.066,  b:int=3, alpha:float=0.16, SRmin:float=0.04, rp:int=2):
    """
    Inputs:
    P : the raw point cloud containing all points p
    search_radius : minimum search radius 
    k : minimum number of neighbors
    Sdr :  Snow detection range 
    threshold = Intensity threshold constant
     ...
    b : multiplication factor
    alpha : horizontal angular resolution of the lidar
    k : minimum number of neighbors
    SRmin : minimum search radius
    rp : the range from the sensor to the point p

    Returns:
    Mask where 1 means outlier
    """
    #LIOR part ----------------------
    P1 = P.copy()

    distance = LA.norm(P1[:,:3],axis=1)
    mask1 = distance >= Sdr
    P1[mask1, -1] = 0

    tree = KDTree(P1[:, :3] , leaf_size=50, metric='manhattan')  #Create a KD tree
    number_of_neighbours = tree.query_radius(P1[:, :3], r=search_radius, count_only=True)

    mask1 = number_of_neighbours <= k
    mask2 = P1[:, -1] <= Ithreshold


    #DROR part ----------------------
    rp = LA.norm(P1[:,:2],axis=1) 

    search_radius = np.ndarray((P1.shape[0],))
    
    
    search_radius = [SRmin if radius < SRmin else b * (radius * alpha) for radius in rp]

        
    number_of_neighbours = tree.query_radius(P1[:, :3], r=search_radius, count_only=True) # this line eats cpu time
    mask3 = number_of_neighbours < k
    
    return mask1 & mask2 & mask3
