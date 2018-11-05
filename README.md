# show_optical_flow_in_color
This is python3 code to show optical flow in color form.<br />
If there are anything don't understand please feel free to contact to me.<br />

This code is modified from:<br />
https://blog.csdn.net/zouxy09/article/details/8683859 <br />

Please install following package before using this code:<br />
1. opencv<br />
2. numpy<br />

Coding and testing by Anaconda in Windows 10 with python 3.6.4.<br />

Flow field color coding:

![alt text](https://github.com/SHENG-KAI-HUANG/show_optical_flow_in_color/blob/master/optical_flow_color.png)

This image is a clone from flownet2[1] supplementary material.<br />
In this code, I using opencv's coordinate which means right direction is postive x, and down direction is postive y.<br />
(original point is the white point in the image).<br />
<br />
Beware, ususally optical flow will be put in .flo, but here I assume already can get x and y direction optical flow vector successfullly.<br />
<br />
In this project will have a sample .npy to show how to use this code.<br />
The original .flo file is created by [[2] github code](https://github.com/lmb-freiburg/netdef_models).<br />
Then, restore the .flo file by numpy. <br />
the optical flow is from [chair001 video](https://lmb.informatik.uni-freiburg.de/resources/datasets/StereoEgomotion.en.html)(left frame).<br /> 

How to use this code:<br />
1. make sure the .npy using channel 0 as y direction vector and channel 1 as x direction vector<br />
2. run the code by input:<br />
python3 main.py
then it will create a windows to show the result.

-----------------<br />
Reference:<br />
[1]	E.Ilg, N.Mayer, T.Saikia, M.Keuper, A.Dosovitskiy, and T.Brox, “FlowNet 2.0: Evolution of Optical Flow Estimation With Deep Networks,” in The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017.<br />
[2]	E.Ilg, T.Saikia, M.Keuper, andT.Brox, “Occlusions, Motion and Depth Boundaries with a Generic Network for Disparity, Optical Flow or Scene Flow Estimation,” in The European Conference on Computer Vision (ECCV), 2018.<br />

