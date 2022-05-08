# CS598 Deep Learning for Healthcare, Paper Reproduction
### ConCare: Personalized Clinical Feature Embedding via Capturing the Healthcare Context
#### Group ID: 141, Paper ID: 210 (classified as hard)
#### Linhan Yang (linhany2) and Alejandro Pimentel (ap41)

### Citation to the original paper

https://arxiv.org/abs/1911.12216

Liantao Ma, Chaohe Zhang, Yasha Wang, Wenjie Ruan, Jiangtao Wang, Wen Tang, Xinyu Ma, Xin Gao, Junyi Gao

### Original repository

https://github.com/Accountable-Machine-Intelligence/ConCare

### Data download instruction

MIMIC-III data must be acquired from https://mimic.physionet.org/. Specifically, download the CSVs. 

To build the **in-hospital mortality** dataset follow instructions from https://github.com/YerevaNN/mimic3-benchmarks/.

Save the ```train``` and ```test``` folders under ```data/``` directory.

8 different list files are provided under ```data/```:

* split<n>_train_listfile.csv
* split<n>_val_listfile.csv

where <n> can be 0,1,2,3,4,5,6 or 9.

Number 9 is the smallest data split.
Additionally, ```splitc_``` files correspond to the original data split shared by ConCare authors. 

For the demographic data can be downloaded from https://drive.google.com/drive/folders/1M8a-VD39v3FxZU_T-FK4q5odif4A3XuB?usp=sharing, 

The file ```demographic.zip``` should be extracted under ```data/```.

### Execution environment

A Conda environment file is provided with the list of dependencies used. See ```ConCare.yaml```

```yaml
name: ConCare

channels:
  - conda-forge
  - defaults

dependencies:
  - pip
  - python=3.7.3
  - numpy
  - pytorch
  - cudatoolkit
  - scipy
  - scikit-learn
```

### Training

To execute examples:

```
python concare.py split9 train
```

```
python concare.py splitc train
```

Depending on the executed split, a model will be created under ```model``` folder.

### Evaluation

```
python concare.py split9 test
```

```
python concare.py splitc test
```

The corresponding model trained on the indicated split will be evaluated using the files ```test_listfile.csv``` 
and ```test/```.

### Reproduced trained model

Model can be downloaded from: https://drive.google.com/drive/folders/1M8a-VD39v3FxZU_T-FK4q5odif4A3XuB?usp=sharing

Note that provided model was created using an environment with GPU support.

### Reproduced Results

* Paper Test Results (Bootstraping)

| AUROC   | AUPRC  | min(Se, P+)    |
| --------|--------|--------------- |
| 0.8702  | 0.5317 | 0.5082         |

* Reproduced Test Results (Bootstraping)

| AUROC   | AUPRC  | min(Se, P+)    |
| --------|--------|--------------- |
| 0.8675  | 0.5293 | 0.5092         |