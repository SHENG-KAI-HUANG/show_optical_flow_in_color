### show_optical_flow_in_color
This is python3 code to show optical flow in color.<br />
If there are anything don't understand or bug, please feel free to post an issue.<br />

Coding and testing by Anaconda in Windows 10 with python 3.6.5.<br />

This code is modified from:<br />
https://blog.csdn.net/zouxy09/article/details/8683859 <br />

Please install following package before using this code:<br />
1. opencv<br />
2. numpy<br />

## Some important information:
Flow field color coding:

![alt text](https://github.com/SHENG-KAI-HUANG/show_optical_flow_in_color/blob/master/readme_image/optical_flow_color.png)

This image is a clone from flownet2[1] supplementary material.<br />
In this code, I using opencv's coordinate which means east is postive x, and south is postive y.<br />
(original point is the white point in the image).<br />
<br />

## How to using this code:
In this project will have a sample .pfm to show how to use this code.<br />
this .pfm is download from [Monkaa scene flow dataset sample pack](https://lmb.informatik.uni-freiburg.de/resources/datasets/SceneFlowDatasets.en.html)<br /> 
you can also find original code that how to read .pfm by python from the above website.<br /> 

Run the code by input:<br />
python3 main.py<br />

It will create a windows to show the result like this.<br />
![alt text](https://github.com/SHENG-KAI-HUANG/show_optical_flow_in_color/blob/master/readme_image/flow_48.jpg)<br />
Functions that turn optical flow vector into color all in the show_optical_function.py.<br />

-----------------<br />
Reference:<br />
[1]	E.Ilg, N.Mayer, T.Saikia, M.Keuper, A.Dosovitskiy, and T.Brox, “FlowNet 2.0: Evolution of Optical Flow Estimation With Deep Networks,” in The IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017.<br />
[2]	E.Ilg, T.Saikia, M.Keuper, and T.Brox, “Occlusions, Motion and Depth Boundaries with a Generic Network for Disparity, Optical Flow or Scene Flow Estimation,” in The European Conference on Computer Vision (ECCV), 2018.<br />

