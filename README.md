#### Gate detection algorithm using Convolutional Neural Network (CNN) for autonomous drone racing applications
* Only perform `Main Setup Linux` from `item 1-4` if you only want to use it for gate detection `item 5 and 6` are not required! 
   * Note that I changed the name convention of the corners.csv file (img_01.png -> img_001.png). Therefore, if you want to test some random images for gate detected make sure that all the images have a name convention with a 3 number digit. 
* `Main Setup Linux` `item 5 and 6` only required if you want to verify the training process and generated files.
* `OPTIONAL` steps are not required if you only want to generate the results

# 1 - Main Setup LINUX

#### 1 Create virtual environment and installing packages

To avoid any potential conflicts while running the code, follow the steps indicated below. If you already have these packages installed on the computer indicated in `step 3`, you should be able to run everything without creating a virtual environment. Then skip `step 1-3` is go to proceed from `step 4`.

Step 1) Create a virtual environment using the following command in terminal:
* `python3 -m venv env`

Step 2) Activate the virtual environment using the following commmand in terminal:
* `source env/bin/activate`

Step 3) Install the required package using the following command in terminal one by one:
* `pip install opencv-python`
* `pip install matplotlib`
* `pip install natsort`
* `pip install pillow`

#### #2 Creating the required files for setup

To train the YOLOv3 Tiny model first download the files in https://drive.google.com/open?id=1tAU94nxl_t4HMqPXizXm84QtYIwCEoYz. It contains the following folders and files.
* `Folder YOLOv3`
* `Folder_txt` 
* `Images_Test`
* `Images_Train` 
* `Images_Validation` 
* `corners.csv`
* `create_txt.py`

Step 1) Navigate in the terminal to the directory that contains the following items as listed above. 

Step 2) Run the python script create_txt.py. This script will generate `test.txt`, `train.txt`, `val.txt` and txt files in the folder `Folder_txt` for the trained images. To run this script use the following command in terminal:
* `python create_txt.py`

#### #3 Placing the created files in the correct directory

Step 3) Now that the required files are created, the files should be moved to the correct location. First of all create two folders named `obj` and `test_images` in `/darknet/data`. Then move the files to the correct location as described below:

- Files in `Folder_txt` should be located in `darknet/data/obj`
- Files in the `Images_Train` folder should be located in `/darknet/data/obj`
- Files in the `Images_Test` should be located in `/darknet/data/test_images`
- The `test.txt`, `train.txt` and `val.txt` files should be located in `/darknet/data`
- In `Folder YOLOv3`, `darknet53.conv.74` should be placed in `/darknet`, the remaining files that contains '.weights' as an extension should all be placed in `/darknet/backup/Yolo`. The folder `Yolo` does not exist yet so create this folder. (OPTIONAL) 
- Copy the `corners.csv` file into the main directory of darknet thus located in `/darknet`

#### #4 Initializing Darknet

Step 1) The default uses the CPU, if your computer has a NVIDIA GPU with CUDA, the training process can be speed up significantly. More information about this can be found on https://pjreddie.com/darknet/install/. If this is the case change the first 4 lines into:
* GPU=1
* CUDNN=1
* CUDNN_HALF=1
* OPENCV=0

Step 2) To initalize, navigate to `/darknet` and type the following command in the terminal:
* make

#### #5 Training the YOLOv3-Tiny Model (OPTIONAL: already in repository)
Step 1) To train the YOLOv3-Tiny model, navigate to `/darknet` and run the following command:
* `./darknet detector train data/obj.data cfg/yolov3-tiny-obj.cfg yolov3-tiny.conv.15`

Step 2) To train the YOLOv3 model, navigate to `/darknet` and run the following command:
* `./darknet detector train data/obj.data cfg/yolo-obj.cfg darknet53.conv.74`

#### #6 Testing the trained model on the test-images (OPTIONAL: already in repository)
Step 1) To run the trained YOLOv3-Tiny model on the test images, navigate to `/darknet` and run the following command:
* `./darknet detector test data/obj.data cfg/yolov3-tiny-obj.cfg backup/Yolo-Tiny/yolov3-tiny-obj_final.weights -dont_show -ext_output < data/test.txt > result_yolo_tiny_2000.txt`

Step 2) To run the trained YOLOv3 model on the test images, navigate to `/darknet` and run the following command:
* `./darknet detector test data/obj.data cfg/yolo-obj.cfg backup/Yolo/yolo-obj_final.weights -dont_show -ext_output < data/test.txt > result_yolo_2000.txt`

This command will generate a txt file that contains the confidence level and coordinates of the predicted bounding box. In a similar way the the txt files for 1000 iterations can be obtained by changing `yolo-obj-tiny_final.weights` to `yolo-obj-tiny_1000.weights`  and `result_yolo_tiny_2000.txt` to `result_yolo_tiny_1000.txt`.

# 2 - Showing the results
Step 1) The python file `gate_data.py` will generate the results obtained from trained model on the test images. This script contains four main functions `CNN_CSV_File()`, `sort_corners()`, `plot_box()` and `IoU()`. By default this script will shows the predicted results of the images. To run this script navigate to `/darknet` and run the following command:

* `python gate_data.py`
  * If you want to use the trained model for other test images, simply replace the images in `/darknet/data/test_images/` by the images that you want to test for and repeat `#5 Testing the trained model on the test images` and afterwards run python `gate_data.py`.

Step 2) To generate the data for the ROC curve, the python script should be modified by commenting `plot_box()` at line 302 and uncommenting `IoU()` on line 303. To generate the data for 1000 and 2000 iterations simply change line 10 to the number of iterations. Note that this could take a couple of minutes before the code is finished. Once it is finished the data files should be saved in `/darknet/ROC`. (OPTIONAL)

Step 3) To generate the ROC plots, the `plot.py` script can be used. This script contains two main functions, `yolov3_plot()` and `yolov3_tiny_plot()`. By default this script will generate the ROC for YOLOv3 Tiny model for 1000 iterations and 2000 iterations. If the ROC curve for YOLOv3 is required simply comment `yolov3_tiny_plot()` on line 136 and uncomment `yolov3_plot()` on line 135. To run this script navigate to `/darknet` and run the following command:

* `python plot.py`






