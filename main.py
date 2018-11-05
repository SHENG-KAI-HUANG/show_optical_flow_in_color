# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:28:33 2018

@author: mark
"""
import cv2

from show_optical_function import makecolorwheel, motionToColor
from to_read_pfm import readPFM

colorwheel = [];
makecolorwheel(colorwheel);

flow, scale = readPFM('0048.pfm');
color_flow = motionToColor(flow, colorwheel);
    
cv2.imwrite('flow_48.jpg', color_flow);
    
cv2.imshow("flow", color_flow);

cv2.waitKey(0);
cv2.destroyAllWindows();