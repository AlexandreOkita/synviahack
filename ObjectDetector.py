from __future__ import division
import time
import torch 
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import cv2 
from utils import *
import argparse
import os 
import os.path as osp
from darknet import Darknet
import pickle as pkl
import pandas as pd
import random

class Object_Detector:
    def __init__(self, bs=1, confidence=0.5, nms_thresh=0.4, cfgfile="cfg/yolov3.cfg",
                 weightsfile="yolov3.weights", resolution=256, videofile=0, num_classes=80,
                 classes="data/coco.names"):
        self.batch_size = bs
        self.confidence = confidence
        self.nms_thesh = nms_thresh
        self.cfgfile = cfgfile
        self.weightsfile = weightsfile
        self.resolution = resolution
        self.videofile = videofile
        self.num_classes = num_classes
        self.start = 0
        self.CUDA = torch.cuda.is_available()
        
        
        print("Loading network.....")
        self.model = Darknet(self.cfgfile)
        self.model.load_weights(self.weightsfile)
        print("Network successfully loaded")
        
        self.model.net_info["height"] = self.resolution
        self.inp_dim = int(self.model.net_info["height"])
        assert self.inp_dim % 32 == 0 
        assert self.inp_dim > 32
        
        
    def loop(self):
        
        self.frames = 0  
        start = time.time()
        process = 0
        
        self.model.eval()
        self.cap = cv2.VideoCapture(self.videofile)
        assert self.cap.isOpened(), 'Cannot capture source'
        
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            
            if ret:
                process += 1
                if process % 10 == 0:
                    process = 0
                    frame = self.process(frame)
                cv2.imshow("frame", frame)
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break
                continue
                    

    
    def process(self, frame):
        im_dim = frame.shape[1], frame.shape[0]
        im_dim = torch.FloatTensor(im_dim).repeat(1,2)
        
        img = prep_image(frame, self.inp_dim)
        with torch.no_grad():
            output = self.model(Variable(img), self.CUDA)
        output = write_results(output, self.confidence, self.num_classes, nms_conf = self.nms_thesh)
        if type(output) == int:
            new_frame = frame
        else:
            im_dim = im_dim.repeat(output.size(0), 1)
            scaling_factor = torch.min(256/im_dim,1)[0].view(-1,1)
            
            output[:,[1,3]] -= (self.inp_dim - scaling_factor*im_dim[:,0].view(-1,1))/2
            output[:,[2,4]] -= (self.inp_dim - scaling_factor*im_dim[:,1].view(-1,1))/2

            output[:,1:5] /= scaling_factor

            for i in range(output.shape[0]):
                output[i, [1,3]] = torch.clamp(output[i, [1,3]], 0.0, im_dim[i,0])
                output[i, [2,4]] = torch.clamp(output[i, [2,4]], 0.0, im_dim[i,1])

            self.classes = load_classes('data/coco.names')
            self.colors = pkl.load(open("pallete", "rb"))

            list(map(lambda x: self.draw_rec(x, frame), output))

            new_frame = frame
        
            
        return new_frame
    
    def draw_rec(self, x, results):
        """
        Draws a rectangle with a random color from colors.
        Moreover, draws a filled rectangle on the top left corner
        of the boundring box, and writes the class of the object detected.
        """
        c1 = tuple(x[1:3].int())
        c2 = tuple(x[3:5].int())
        img = results
        cls = int(x[-1])
        label = "{0}".format(self.classes[cls])
        color = random.choice(self.colors)

        # draw a rectangle
        cv2.rectangle(img, c1, c2,color, 1)

        t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 1 , 1)[0]
        c2 = c1[0] + t_size[0] + 3, c1[1] + t_size[1] + 4

        # draw a filled rectangle
        cv2.rectangle(img, c1, c2,color, -1)

        # write the class of the object
        cv2.putText(img, label, (c1[0], c1[1] + t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 1, [225,255,255], 1)

        return img
        