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


#### Training (train_SemanticKITTI.py)

1. Set dataset path in train_SemanticKITTI.py ('INPUT_PATH')
2. Run: train_SemanticKITTI.py  

##### Example:
```
python train_SemanticKITTI.py
```


#### Generate prediction labels (test_pretrain_SemanticKITTI.py)
1. Set dataset path in 'test_pretrain_SemanticKITTI.py'
2. Set model in 'test_pretrain_SemanticKITTI.py'
3. Generate prediction by running: test_pretrain_SemanticKITTI.py
4. Output stored in: /out

##### Example:
```
python test_pretrain_SemanticKITTI.py
```


#### Evaluate file (Result.py)    
Inputs:
* --prediction-folder : Path to predictions folder (/pred)
* --dataset-folder : Path to the dataset (/dataset/sequences/)   
 ##### Example:
 ```
  python Result.py --prediction-folder /pred --dataset-folder /dataset/sequences/
 ``` 
  
  ### Acknowledgment
Acknowledgment are given to the open source code of [PolarNet]
