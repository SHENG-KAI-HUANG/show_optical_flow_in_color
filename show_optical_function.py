# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:04:35 2018

@author: SHENG-KAI HUANG

Farneback dense optical flow calculate and show in Munsell system of colors  
Author : Zouxy  
Date   : 2013-3-15  
HomePage : http://blog.csdn.net/zouxy09  
Email  : zouxy09@qq.com 

Color encoding of flow vectors from:  
http://members.shaw.ca/quadibloc/other/colint.htm  
This code is modified from:  
http://vision.middlebury.edu/flow/data/ 
"""
import numpy as np

def makecolorwheel(colorwheel):

    RY = 15;  
    YG = 6;  
    GC = 4;  
    CB = 11;  
    BM = 13;  
    MR = 6;  
   
    for i in range(0, RY):
        colorwheel.append(np.array([255, 255 * i / RY, 0]));  
    for i in range(0, YG):
        colorwheel.append(np.array([255 - 255 * i / YG, 255, 0]));  
    for i in range(0, GC):
        colorwheel.append(np.array([0, 255, 255 * i / GC]));  
    for i in range(0, CB):
        colorwheel.append(np.array([0, 255 - 255 * i / CB, 255]));  
    for i in range(0, BM):
        colorwheel.append(np.array([255 * i / BM, 0, 255]));  
    for i in range(0, MR):
        colorwheel.append(np.array([255, 0, 255 - 255 * i / MR]));  

def motionToColor(flow, colorwheel):#input flow then output color
    """
    assume y-direction flow in flow[:,:,0] and x in flow[:,:,1]
    first ":" means rows number (in matrix form)
    second ":" means cols number (in matrix form)
    """
    color = np.zeros((flow.shape[0], flow.shape[1], 3), dtype=np.uint8); 
  
    #determine motion range:
    maxrad = 0.0;  
    UNKNOWN_FLOW_THRESH = 1e9;
    
    #Find max flow to normalize fx and fy  
    for i in range(0, flow.shape[0]): 
        for j in range(0, flow.shape[1]):
            
            fy = flow[i][j][0]; 
            fx = flow[i][j][1];  
            
            if (np.abs(fx) >  UNKNOWN_FLOW_THRESH) or (np.abs(fy) >  UNKNOWN_FLOW_THRESH): 
                continue;  
            rad = np.sqrt(fx * fx + fy * fy);
            
            if maxrad > rad:
                maxrad = maxrad;
            else:
                maxrad = rad;

    for i in range(0, flow.shape[0]):
        for j in range(0, flow.shape[1]):
            fy = flow[i][j][0] / maxrad;
            fx = flow[i][j][1] / maxrad;  
            
            if (np.abs(fx) >  UNKNOWN_FLOW_THRESH) or (np.abs(fy) >  UNKNOWN_FLOW_THRESH): 
                color[i, j, :] = 0;
                continue;
             
            rad = np.sqrt(fx * fx + fy * fy);
            angle = np.arctan2(-fy, -fx) / np.pi;
            
            fk = (angle + 1.0) / 2.0 * (len(colorwheel) - 1);
            k0 = int(fk);  
            k1 = (k0 + 1) % len(colorwheel);
            f = fk - k0;
            #f = 0; #uncomment to see original color wheel  
  
            for b in range(0, 3):#(int b = 0; b < 3; b++)   
                col0 = colorwheel[k0][b] / 255.0;  
                col1 = colorwheel[k1][b] / 255.0;  
                col = (1 - f) * col0 + f * col1;  
                if (rad <= 1):  
                    col = 1 - rad * (1 - col); #increase saturation with radius  
                else:
                    col *= 0.75; #out of range  
                color[i][j][2 - b] = int(255.0 * col);
    return color;