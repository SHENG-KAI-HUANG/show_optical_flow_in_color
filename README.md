# show_optical_flow_in_color
this is python code (for python3) to show optical flow in color form.

This code is modified from:  
https://blog.csdn.net/zouxy09/article/details/8683859

please install following package before using this code:
1. opencv
2. numpy

Flow field color coding:

![alt text](https://github.com/SHENG-KAI-HUANG/show_optical_flow_in_color/blob/master/optical_flow_color.png)

this image is a clone from flownet2[1] supplementary material.

Beware, ususally optical flow will be put in .flo, but here I assume already can get x and y direction optical flow vector successfullly.
in this project will have a sample .npy to show how to use this code(the .npy file is created by [[2] github code](https://github.com/lmb-freiburg/netdef_models))

How to use this code:
1. 


-----------------
Reference:
[1]	E.Ilg, N.Mayer, T.Saikia, M.Keuper, A.Dosovitskiy, and T.Brox, “FlowNet 2.0: Evolution of Optical Flow Estimation With Deep Networks,” in The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017.
[2]	E.Ilg, T.Saikia, M.Keuper, andT.Brox, “Occlusions, Motion and Depth Boundaries with a Generic Network for Disparity, Optical Flow or Scene Flow Estimation,” in The European Conference on Computer Vision (ECCV), 2018.

