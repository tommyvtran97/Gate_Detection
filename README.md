# Gate Detection using Convolutional Neural Network in Autonomous Drone Racing

## Main Setup LINUX


#### Creating the required files for setup

To train the YOLOv3 Tiny model first download the files in {insert link}. It contains the following folders and files.
* Folder YOLOv3
* Folder_txt 
* Images_Test
* Images_Train 
* Images_Validation 
* corners.csv
* create_txt.py

Step 1) Navigate in the terminal to the directory that contains the following items as listed above. 

Step 2) Run the python script create_txt.py. This script will generate test.txt, train.txt, val.txt and txt files in the folder 'Folder_txt'. To run this script use the following command in terminal:
* python create_txt.py

#### Placing the created files in the correct directory

Step3 ) Now that the required files are created, the files should be moved to the correct location. First of all create two folders named 'obj' and 'test_images' in /darknet/data. Then move the files to the correct location as described below:

- Files in 'Folder_txt' should be located in darknet/data/obj
- Files in the 'Images_Train' folder should be located in /darknet/data/obj
- Files in the 'Images_Test' should be located in /darknet/data/test_image
- The 'test.txt', 'train.txt' and 'val.txt' files should be located in /darknet/data
- In the YOLOv3 folder, 'darknet53.conv.74' should be placed in /darknet, the remaining files that contains '.weights' as an extension should all be placed in darknet/backup/Yolo. The folder 'Yolo' does not exist yet so create this folder. 

## Training the YOLOv3-Tiny Model
Step 1) To train the YOLOv3-Tiny model, navigate to /Darknet and run the following command:
* ./darknet detector train data/obj.data cfg/yolov3-tiny-obj.cfg yolov3-tiny.conv.15

Step 2) To train the YOLOv3 model, navigate to /darknet and run the following command:
* ./darknet detector train data/obj.data cfg/yolo-obj.cfg darknet53.conv.74

This process, might take a while depending what kind of GPU is used.

## Testing the trained model on the test-images
Step 1) To run the trained YOLOv3-Tiny model on the test images, navigate to /darknet and run the following command:
* ./darknet detector test data/obj.data cfg/yolov3-tiny-obj.cfg backup/Yolo-Tiny/yolov3-tiny-obj_final.weights -dont_show -ext_output < data/test.txt > result_yolo_tiny_2000.txt

Step 2) To run the trained YOLOv3 model on the test images, navigate to /darknet and run the following command:
* ./darknet detector test data/obj.data cfg/yolo-obj.cfg backup/Yolo/yolo-obj_final.weights -dont_show -ext_output < data/test.txt > result_yolo_2000.txt

This command will generate a txt file that contains the confidence level and coordinates of the predicted box. In a similar way the the txt files for 1000 iteration can be obtained by changing yolo-obj-tiny_1000.weights and result_yolo_tiny_1000.txt.

#### 5 - Showing the results
The python file gate_data.py will generate the results obtained from trained model on the test images. This script contains four main functions CNN_CSV_File(), sort_corners(), plot_box() and IoU(). By default this script will shows the predicted results of the images. To run this script navigate to /Darknet and run the following command:

- python gate_data.py

To generate the data for the ROC curve, the python script should be modified by commenting plot_box() at line 302 and uncommenting line 303. To generate the data for 1000 and 2000 iterations simply change line 10 to the number of iterations. Note that this could take a couple of minutes before the code is finished. Once it is finished the data files should be saved in /Darknet/ROC. 

To generate the ROC plots, the plot.py script can be used. This script contains two main functions, yolov3_plot() and yolov3_tiny_plot(). By default this script will generate the ROC for YOLOv3 Tiny model for 1000 iterations and 2000 iterations. If the ROC curve for YOLOv3 is required simply comment yolov3_tiny_plot() on line 136 and uncomment yolov3_plot() on line 135. To run this script navigate to /Darknet and run the following command:

- python plot.py






