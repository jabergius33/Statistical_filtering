# Cylinder for binary segmentation of snow

The code is implmeted on linux ubuntu 20.04


#### Pre-config:
##### Create a environment with:
  * 
 ##### Activate it using:
  * conda activate Cylinder
##### Install additional package:
  * 
  *
  
### How to use it for binary segmentation:


#### Training (potentially need to chmod +x the file)

1. Modify the config file at '/config/semantickitti.yaml' (change setup and dataset path)
2. Train the network by running: 
```
sh train.sh
```

#### Generate prediction labels (demo_test_folder.py )
  Args:
* --demo-folder : Path to the data sequence
 ##### Example:
```
python demo_test_folder.py --demo-folder /dataset/sequences/
```


#### Evaluate file (Result.py)    
Inputs:
* --prediction-folder : Path to predictions folder
* --dataset-folder : Path to the dataset (/data_path)   
 ##### Example:
 ```
 python Result.py --prediction-folder /pred --dataset-folder /dataset/sequences/
 ``` 
  
  
