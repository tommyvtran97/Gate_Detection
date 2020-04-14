import cv2
import numpy as np
from PIL import Image
import os
import natsort
import operator
import csv
import matplotlib.pyplot as plt

iteration = 2000           # Results for either 1000 iteration or 2000 iteration

f = open("result_yolo_tiny_" + str(iteration) + ".txt", "r")
g = open("corners.csv", "r")

corners = g.readlines()
lines = f.readlines()[:-1]

path_image = "data/test_images/"

def CNN_CSV_File():
    """ This function manipulates the txt-file that is obtained from the Convulational Neural Network (CNN)
        by extracting the important parameters such as the name of the image, box coordinates, confidence score
        and computing speed and writing it into a CSV file. """

    CSV_CNN = open('CNN_corners.txt', 'w+')

    # Set condition to avoid taking wrong line at beginning and end of txt.file
    condition = False

    # Reading the txt.file line by line
    for line in lines:

        # The file post-processed before written as a new CSV-file. 
        line = line.strip(' ').split(' ')
        while("" in line): 
            line.remove("") 

        if line[0] == 'Gate:' or line[0] == 'Enter':
            for item in line:
                item.strip(' ')
            
            if line[0] == 'Enter':
                img_name = line[3].strip(':')[-11:]
                comp_speed = line[6]

                img_path = "data/test_image/" + img_name
                img = cv2.imread(img_path)

                condition = True

            if line[0] == 'Gate:':

                top_left_x = line[2]
                top_left_y = line[4]
                width = line[6]
                height = line[8].strip(')\n')
                confidence = line[1].strip('%\t(left_x:')

                top_right_x = int(top_left_x) + int(width)
                top_right_y = int(top_left_y)
                bottom_left_x = int(top_left_x)
                bottom_left_y = int(top_right_y) + int(height)
                bottom_right_x = int(top_right_x)
                bottom_right_y = int(bottom_left_y)
                
                # The result parameters from the CNN YOLOv3 are written in a CSV-file
                if condition:
                    CSV_CNN.write(img_name + ',' + str(top_left_x) + ',' + str(top_right_y) + ',' 
                    + str(top_right_x) + ',' + str(top_right_y) + ',' + str(bottom_right_x) + ',' 
                    + str(bottom_right_y) + ',' + str(bottom_left_x) + ',' + str(bottom_left_y) + ','
                    + confidence + ',' +comp_speed + '\n')

    CSV_CNN.close()
    f.close()

def sort_corners():
    """ This function sorts the CSV file based on the name and 
        the top-left x-coordinates to make the CSV file cleaner. """


    # Sorting the ground truth CSV-file, first priority names and second priority left-top x-coordinates box in ascending order
    corners_file = open('corners.csv', 'r')
    corners_file = csv.reader(corners_file, delimiter=',')

    sort = sorted(corners_file, key=lambda row: (str(row[0]), int(row[5])))
    f = open('corners.csv', 'w+')
    for line in sort:
        f.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] +
                 ',' + line[4] + ',' + line[5] + ',' + line[6] + ',' + line[7] + ',' + line[8] + '\n')
    f.close()

    # Sorting the ground truth CSV-file, first priority names and second priority left-top x-coordinates box in ascending order
    corners_file = open('CNN_corners.txt', 'r')
    corners_file = csv.reader(corners_file, delimiter=',')

    sort = sorted(corners_file, key=lambda row: (str(row[0]), int(row[1])))
    f = open('CNN_corners.txt', 'w+')
    for line in sort:
        f.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[5] +
                 ',' + line[4] + ',' + line[5] + ',' + line[6] + ',' + line[7] + 
                 ',' + line[8] + ',' + line[9] + ',' + line[10] + '\n')
    f.close()

def plot_box():
    """ This function plots the predicted box from the Convolutional Neural Network (CNN)
        and the ground truth box from the reference data """

    b = open('CNN_corners.txt', 'r')
    CSV_CNN = b.readlines()
    # The folder with images in sorted in chronological order based on the number
    file_list = natsort.natsorted(os.listdir(path_image))

    # Loop through every test image in the folder
    for image in file_list:
        img = cv2.imread(path_image + image)

        # Draw the box in the image
        for corner in corners:
            corner = corner.strip('\r\n').split(',')
            if corner[0] == image:
                img = cv2.line(img,(int(corner[1]), int(corner[2])), (int(corner[3]), int(corner[4])) , (0, 0, 255), 2)
                img = cv2.line(img,(int(corner[3]), int(corner[4])), (int(corner[5]), int(corner[6])) , (0, 0, 255), 2)
                img = cv2.line(img,(int(corner[5]), int(corner[6])), (int(corner[7]), int(corner[8])) , (0, 0, 255), 2)
                img = cv2.line(img,(int(corner[7]), int(corner[8])), (int(corner[1]), int(corner[2])) , (0, 0, 255), 2)

        for corner in CSV_CNN:
            corner = corner.strip('\r\n').split(',')
            if corner[0] == image:
                img = cv2.line(img,(int(corner[1]), int(corner[2])), (int(corner[3]), int(corner[4])) , (0, 255, 0), 2)
                img = cv2.line(img,(int(corner[3]), int(corner[4])), (int(corner[5]), int(corner[6])) , (0, 255, 0), 2)
                img = cv2.line(img,(int(corner[5]), int(corner[6])), (int(corner[7]), int(corner[8])) , (0, 255, 0), 2)
                img = cv2.line(img,(int(corner[7]), int(corner[8])), (int(corner[1]), int(corner[2])) , (0, 255, 0), 2)

        # Display the image on the screen
        cv2.imshow(image, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
def IoU():
    """ This function calculates the true and false positive rates by looping
        over the confidence probability from 1 to 0. The output of the function 
        is a saved list with data point of the true and false positive rates using  
        a Intersection over Union (IoU) threshold. The saved list will be used 
        in plot.py to generate the ROC curve. """

    list_threshold = [0.5, 0.7, 0.9]

    for threshold in list_threshold:
                                                                      
        plot_data = [(0,0)]

        for confidence in np.arange(1,-0.2, -0.2):

            true_positives = 0
            false_positives = 0
            TP_counter = 0
            FP_counter = 0
            number_of_gates = 0

            b = open('CNN_corners.txt', 'r')
            CSV_CNN = b.readlines()


            # The folder with images in sorted in chronological order based on the number
            file_list = natsort.natsorted(os.listdir(path_image))
            
            for image in file_list:
                ground_truth_output = cv2.imread(path_image + image)
                cnn_output = cv2.imread(path_image + image)
                output_plot = cv2.imread(path_image + image)

                #Analyze ground truth image
                gate_counter = 0
                false_positive_counter = []

                for corner_1 in corners:
                    corner_1 = corner_1.strip('\r\n').split(',')
                    
                    #Initialize Intersection over Union (IoU)
                    IoU = 0

                    if corner_1[0] == image:
                        contours_csv_output = np.array([ [int(corner_1[1]), int(corner_1[2])],
                                                         [int(corner_1[3]), int(corner_1[4])],
                                                         [int(corner_1[5]), int(corner_1[6])],
                                                         [int(corner_1[7]), int(corner_1[8])] ])

                        gate_counter += 1
                        ground_truth_output = cv2.imread(path_image + image)
                        ground_truth_output = cv2.fillPoly(ground_truth_output, [contours_csv_output], color=(0, 0, 255))

                        # Save the image temporarily
                        cv2.imwrite('test_2.png', ground_truth_output)

                        # Create array with True for the elements with red pixels
                        csv_output_im = Image.open('test_2.png', 'r')
                        csv_output_pixels = np.asarray(csv_output_im.getdata())
                        csv_output_obstacles = np.all(csv_output_pixels == [255, 0, 0], axis=1) # This is in RGB!

                        detection_counter = 0
                        box_list = []

                        for corner1 in CSV_CNN:
                            corner1 = corner1.strip('\r\n').split(',')

                            gate_number = 0
                            if corner1[0] == image and int(corner1[9])/100 >= confidence:
                            	#detection_counter += 1
                                contours_cnn_output = np.array([ [int(corner1[1]), int(corner1[2])],
                                                           		 [int(corner1[3]), int(corner1[4])],
                                                           		 [int(corner1[5]), int(corner1[6])],
                                                           		 [int(corner1[7]), int(corner1[8])] ])
                                detection_counter += 1
                                cnn_output = cv2.imread(path_image + image)
                                cnn_output = cv2.fillPoly(cnn_output, [contours_cnn_output], color=(0, 255, 0))

                                # Save the image temporarily
                                cv2.imwrite('test_3.png', cnn_output)

                                # Create array with True for the elements with green pixels
                                cnn_output_im = Image.open('test_3.png', 'r')
                                cnn_output_pixels = np.asarray(cnn_output_im.getdata())
                                cnn_output_obstacles = np.all(cnn_output_pixels == [0, 255, 0], axis=1) # This is in RGB!

                                # Calculate the area of overlap and intersection
                                area_overlap = np.sum((cnn_output_obstacles == True) & (csv_output_obstacles == True))
                                area_cnn = np.sum(cnn_output_obstacles == True)
                                area_csv = np.sum(csv_output_obstacles == True)

                                # Calculate the Intersection over Union (IoU)
                                IoU_1 = area_overlap / (area_cnn + area_csv - area_overlap)

                                if gate_counter == 1:
                                	false_positive_counter.append(IoU_1)

                                if IoU_1 > threshold and IoU_1 > false_positive_counter[detection_counter -1]:
                                	false_positive_counter[detection_counter - 1] = IoU_1

                                if IoU_1 > IoU:
                                    contours_cnn_output_new = contours_cnn_output
                                    box_list.append(IoU_1)
                                    IoU = IoU_1

                                # Show the image with IoU for each gate
                                output_plot = cv2.polylines(output_plot, [contours_csv_output], True, color=(0, 0, 255))
                                if IoU >= 0:
                                    output_plot = cv2.polylines(output_plot, [contours_cnn_output], True, color=(0, 255, 0))
                        
                        # Count the number of true positives in each image
                        if len(box_list) > 0 and IoU >= threshold:
                                TP_counter += 1
                                if len(box_list) > 1:
                                	if (max(box_list)-min(box_list) < 0.10):
                                		print('Threshold to low {} prediction detected for one gate'.format(len(box_list)))

                        if gate_counter == 1:
                            for i in range(len(false_positive_counter)):
                                if false_positive_counter[i] < max(false_positive_counter) and false_positive_counter[i] > threshold:
                                    FP_counter = FP_counter - 1
                                if false_positive_counter[i] < max(false_positive_counter):
                                    false_positive_counter[i] = 0.0

                # Count the number of false positive in each image
                for i in range(len(false_positive_counter)):
                	if false_positive_counter[i] < threshold:
                		FP_counter += 1
                if FP_counter < 0:
                    FP_counter = 0

                # Print the detection classifications
                print(image)
                print('{} Gate'.format(gate_counter))
                print('{} True Positives'.format(TP_counter))
                print('{} False Postives'.format(FP_counter))
                print ('{} Detection'.format(detection_counter))
                if TP_counter != gate_counter:
                	if TP_counter == detection_counter or TP_counter < gate_counter:
                		print("{} False Negative".format(gate_counter - TP_counter))
                print ('*******************************')
                
                #Update the total true/false positives
                true_positives = true_positives + TP_counter
                false_positives = false_positives + FP_counter     
                number_of_gates = number_of_gates + gate_counter

                # Set the total to zero
                TP_counter = 0
                detection_counter = 0
                FP_counter = 0
            
            # Update the total true/false positive rates
            true_positive_rate = true_positives / (number_of_gates)
            false_positive_rate = false_positives / (number_of_gates)

            plot_data.append((false_positive_rate, true_positive_rate))   

        # Save the data point into a list
        data = np.array(plot_data)
        np.savez("ROC/IoU_" + str(threshold) + "_it" + str(iteration) + "_Yolo_Tiny", data)

# The main program
CNN_CSV_File()
sort_corners()
plot_box()
#IoU()




    