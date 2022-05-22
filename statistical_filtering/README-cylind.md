# PolarNet for binary segmentation of snow

The code is tested on linux ubuntu 20.04 (conda version: 4.10.3).


#### Pre-setup:
##### Create a environment:
  * conda create -n myenv python=3.6
 ##### Activate it using:
  * conda activate myenv
##### Install packages:
  * pip install -r requirements.txt
##### Confirm that you are using torch 1.10.x+cu102
```
   python -c "import torch; print(torch.version)"
```
##### Install torch-scatter:
  * pip install torch-scatter -f https://data.pyg.org/whl/torch-1.10.0+cu102.html
##### Install additional package:
* pip install -U scikit-learn
* conda install tensorboard

  
  
### How to use it:


#### Training (potentially need to chmod +x the file)

1. 


#### Generate prediction labels ( )


  Args:
* --demo-folder : Path to the dataset (sequences folder)
 ##### Example:
```

```


#### Evaluate file (Result.py)    
Inputs:
* --prediction-folder : Path to predictions folder (/pred)
* --dataset-folder : Path to the dataset (/dataset/sequences/)   
 ##### Example:
 ```
 ``` 
  
  ### Acknowledgment
Acknowledgment are given to the open source code of 
