#!/usr/bin/python
from __future__ import print_function
import scipy.misc as scpmi
import numpy as np
import collections
import sys,os
import cv2
import vot
import time

CUDA_LIB='/usr/local/cuda-8.0/lib64/'
from ctypes import *
lib1 = cdll.LoadLibrary(CUDA_LIB+'libcublas.so')
lib1 = cdll.LoadLibrary(CUDA_LIB+'libcudart.so')
lib1 = cdll.LoadLibrary(CUDA_LIB+'libcudnn.so')
lib1 = cdll.LoadLibrary(CUDA_LIB+'libcufft.so')
lib1 = cdll.LoadLibrary(CUDA_LIB+'libcufftw.so')
lib1 = cdll.LoadLibrary(CUDA_LIB+'libcuinj64.so')
lib1 = cdll.LoadLibrary(CUDA_LIB+'libcurand.so')

import tensorflow as tf

from util import *
from kernel_params import Params
from tracker import Tracker

# *****************************************
# VOT: Create VOT handle at the beginning
#      Then get the initializaton region
#      and the first image
# *****************************************
handle = vot.VOT("rectangle")
selection = handle.region()

# Process the first frame
imagefile = handle.frame()
if not imagefile:
    sys.exit(0)

# Initialize the Tracker
image = cv2.imread(imagefile, cv2.IMREAD_COLOR)

parameters = Params()
parameters.init_pos = np.floor([selection.x+selection.width/2, selection.y+selection.height/2])                                # Initial position
parameters.pos = parameters.init_pos
parameters.target_size = np.floor([selection.width, selection.height])        

tracker = Tracker(image, parameters)
tracker.train(image, True)

while True:
    # *****************************************
    # VOT: Call frame method to get path of the 
    #      current image frame. If the result is
    #      null, the sequence is over.
    # *****************************************
    imagefile = handle.frame()
    if not imagefile:
        break

    # Processing the current image
    image = cv2.imread(imagefile, cv2.IMREAD_COLOR)
    #region, lost, xtf = tracker.detect(image)
    #if not lost:
    #    tracker.train(image, False, xtf)

    # *****************************************
    # VOT: Report the position of the object 
    #      every frame using report method.
    # *****************************************
    handle.report(selection)