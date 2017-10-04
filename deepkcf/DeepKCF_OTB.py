from __future__ import print_function
import scipy.misc as scpmi
import cv2
from matplotlib import pyplot as plt
from util import *
import numpy as np
from tracker import Tracker
from kernel_params import Params
import sys,os

def DeepKCF(seq, res_path, bSaveImage):

    parameters = Params()

    #img_files, pos, target_sz, ground_truth, video_path = load_video_info(video_path)  # Load video info
    img_files, pos, target_sz, video_path = load_video_gt(seq)


    parameters.init_pos = np.floor(pos) + np.floor(target_sz / 2)                                # Initial position
    parameters.pos = parameters.init_pos                                                         # Current position
    parameters.target_size = np.floor(target_sz)                                                 # Size of target
    parameters.img_files = img_files                                                             # List of image files
    parameters.video_path = video_path                                                           # Path to the sequence

    num_frames = len(img_files)

    results = np.zeros((num_frames, 4))

    start = start_timer()

    # For each frame
    for frame in xrange(num_frames):

        # Read the image
        #im = cv2.imread(video_path + img_files[frame], 1)
        im = scpmi.imread(video_path + img_files[frame])

        # Initialize the tracker using the first frame
        if frame == 0:
            tracker1 = Tracker(im, parameters)
            tracker1.train(im, True)
            results[frame, :] = np.array(
                (pos[0] + np.floor(target_sz[0] / 2), pos[1] + np.floor(target_sz[1] / 2), target_sz[0], target_sz[1]))
        else:
            results[frame, :], lost, xtf = tracker1.detect(im)  # Detect the target in the next frame
            if not lost:
                tracker1.train(im, False, xtf)  # Update the model with the new infomation

    tracker1.close()
    duration = end_timer(start, "to complete tracking")
    fps = round(num_frames/duration, 2)
    
    return results, fps

'''
if __name__ == "__main__":

    seq = {"path":"Benchmark/Shaking/img/","startFrame":1,"endFrame":365,"annoBegin":1,"init_rect":[255,135,61,71], "name":"shaking_1"}
    res_path='tmp'
    bSaveImage=0

    DeepKCF(seq, res_path, bSaveImage)
'''