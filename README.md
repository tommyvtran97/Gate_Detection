# Gate Detection using Convolutional Neural Network in Autonomous Drone Racing

## Only step 5 is neccesary to show the results! Step 1-4, is only neccessary for reproducing of the trained model and files necessary for showing the results in step 5. 


#### 1 - Creating the required files for training

To train the YOLOv3 Tiny model first download the files in {insert link}. It contains the following folders.
* Folder YOLOv3 - contains the files that are required to train the YOLOv3 model and the final weigs obtained from training
* Folder_txt - contains txt files of the training images with the labels in the format <object-class> <x> <y> <width> <height> Note that the coordinate all all normalize relative to the size of the image.
* Images_Test - Contains the test images
* Images_Train - Contains the training images
* Images_Validation - Contains the validation images

In the corners.csv file the coordinates of the labelled images are stated. In order to generate the required files, first run the create_txt.py by navigation to the directory and running the following command:
* python create_txt.py

This python script will generate the test.txt, train.txt and val.txt. Also in Folder_txt, txt files are created for all the training images. Note that Folder YOLOv3, contains the files in order train the YOLOv3 model. However, this is optional as the YOLOv3 Tiny model is chosen.

#### 2 - Placing the created files in the correct directory

- The files in Folder_txt folder should be placed in Darknet/data/obj
- The files in the Images_Train folder should be placed in /Darknet/data/obj
- The files in the Images_Test folder should be placed in /Darknet/data/test_image
- The test.txt, train.txt and val.txt files should be placed in /Darknet/data
- In the YOLOv3 folder, 'darknet53.conv.74' should be placed in /Darknet, the remaining files that contains '.weights' as an extension should all be placed in Darknet/backup/Yolo

#### 3 - Training the YOLOv3-Tiny Model
To train the YOLOv3-Tiny model, navigate to /Darknet and run the following command:
- ./darknet detector train data/obj.data cfg/yolov3-tiny-obj.cfg yolov3-tiny.conv.15

To train the YOLOv3 model, navigate to /Darknet and run the following command:
- ./darknet detector train data/obj.data cfg/yolo-obj.cfg darknet53.conv.74

This process, might take a while depending what kind of GPU is used.

#### 4 - Testing the trained model on the test-images
To run the trained YOLOv3-Tiny model on the test images, navigate to /Darknet and run the following command:
- ./darknet detector test data/obj.data cfg/yolov3-tiny-obj.cfg backup/Yolo-Tiny/yolov3-tiny-obj_final.weights -dont_show -ext_output < data/test.txt > result_yolo_tiny_2000.txt

To run the trained YOLOv3 model on the test images, navigate to /Darknet and run the following command:
- ./darknet detector test data/obj.data cfg/yolo-obj.cfg backup/Yolo/yolo-obj_final.weights -dont_show -ext_output < data/test.txt > result_yolo_2000.txt

This command will generate a txt file that contains the confidence level and coordinates of the predicted box. In a similar way the the txt files for 1000 iteration can be obtained by changing yolo-obj-tiny_1000.weights and result_yolo_tiny_1000.txt

#### 5 - Showing the results
The python file gate_data.py will generate the results obtained from trained model on the test images. This script contains four main functions CNN_CSV_File(), sort_corners(), plot_box() and IoU(). By default this script will shows the predicted results of the images. To run this script navigate to /Darknet and run the following command:

- python gate_data.py

To generate the data for the ROC curve, the python script should be modified by commenting plot_box() at line 302 and uncommenting line 303. To generate the data for 1000 and 2000 iterations simply change line 10 to the number of iterations. Note that this could take a couple of minutes before the code is finished. Once it is finished the data files should be saved in /Darknet/ROC. 

To generate the ROC plots, the plot.py script can be used. This script contains two main functions, yolov3_plot() and yolov3_tiny_plot(). By default this script will generate the ROC for YOLOv3 Tiny model for 1000 iterations and 2000 iterations. If the ROC curve for YOLOv3 is required simply comment yolov3_tiny_plot() on line 136 and uncomment yolov3_plot() on line 135. To run this script navigate to /Darknet and run the following command:

- python plot.py






