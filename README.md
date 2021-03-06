# Deep KCF trackers

This tracker is KCF based one with CNN features, and this version is made for both OTB and VOT evaluation.

## Deep KCF configure
*** Most Inportant, Do use the tensorflow version 1.1 and Cudnn version 5.1, because the higher version will have conflicts in hdf5, which haven't been solved by now.***
* Download inception_v3.ckpt from Kaggle, and link to the current holder
* test the deep kcf by running run_deepkcy.py 

# Tensorflow configuration!!!
    * update tensorflwo into r1.1 `sudo pip  install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.1.0-cp27-none-linux_x86_64.whl`
    * use cudnn 5.1, download cudnn 5.1 `https://developer.nvidia.com/rdp/cudnn-download`, and install under the cudnn install direction `http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html`.





## Eval on OTB

### Download the OTB evaluation benchmark
```bash
git clone git@github.com:ugv-tracking/OTB_Tracker.git
```
### Download the OTB sequence from the OTB website.

### Download the DeepKCF
```bash
cd OTB_Tracker/trackers
git clone git@github.com:ugv-tracking/DeepKCF.git
```
### Evaluation 
open Matlab and change the dir to OTB_Tracker
```bash
run main_running.m
```
### Configure the images sequences and compartive trackers
```	
check util/configSeqs.m
check util/configTrackers.m
```
### Draw figures
```bash
run perfPlot.m
```

## Eval on VOT

### Download VOT evaluation benchmark
```bash
git clone git@github.com:ugv-tracking/VOT-Tracker.git
```
### Download Tracker 
```bash
cd VOT-Tracker/workspace_DKCF
git clone git@github.com:ugv-tracking/DeepKCF.git
```
### Evaluation
```bash
cd VOT-Tracker/workspace_DKCF
run_experiments.m % This script can be used to execute the experiments for a single tracker
run_test.m % This script can be used to test the integration of a tracker to the framework.
run_analysis.m % This script can be used to perform a comparative analyis of the experiments in the same manner as for the VOT challenge.
```
### Modify Tracker

Check the below files:
* tracker.py
* DeepKCF_OTB.py
* DeepKCF_VOT.py

