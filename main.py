# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:46:12 2018

@author: SHENG-KAI HUANG
"""
import cv2
import numpy as np
from show_optical_function import makecolorwheel, motionToColor

#flow_path = '../../output/optical_flow_calc';

colorwheel = []; 
makecolorwheel(colorwheel);

flow = np.load('flow_0_1.out.npy');#flow_path + '/flow_0_1.out.npy');
"""
flow = np.ones((200,200,2));
flow[:,:,0] *= 0;
flow[:,:,1] *= -1;
"""
color_flow = motionToColor(flow, colorwheel);

cv2.imshow("flow", color_flow);

cv2.waitKey(0);
cv2.destroyAllWindows();
