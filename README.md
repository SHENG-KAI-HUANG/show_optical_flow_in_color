# show_optical_flow_in_color
This is python3 code to show optical flow in color form.

This code is modified from:  
https://blog.csdn.net/zouxy09/article/details/8683859

Please install following package before using this code:
1. opencv
2. numpy

Coding and testing by Anaconda in Windows 10 with python 3.6.4.

Flow field color coding:

![alt text](https://github.com/SHENG-KAI-HUANG/show_optical_flow_in_color/blob/master/optical_flow_color.png)

This image is a clone from flownet2[1] supplementary material.
In this code, I using opencv's coordinate which means right direction is postive x, and down direction is postive y (original point is the white point in the image).

Beware, ususally optical flow will be put in .flo, but here I assume already can get x and y direction optical flow vector successfullly.

In this project will have a sample .npy to show how to use this code.
The original .flo file is created by [[2] github code](https://github.com/lmb-freiburg/netdef_models).
Then, restore the .flo file by numpy. 

How to use this code:
1. 


-----------------
Reference:
[1]	E.Ilg, N.Mayer, T.Saikia, M.Keuper, A.Dosovitskiy, and T.Brox, “FlowNet 2.0: Evolution of Optical Flow Estimation With Deep Networks,” in The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017.
[2]	E.Ilg, T.Saikia, M.Keuper, andT.Brox, “Occlusions, Motion and Depth Boundaries with a Generic Network for Disparity, Optical Flow or Scene Flow Estimation,” in The European Conference on Computer Vision (ECCV), 2018.

