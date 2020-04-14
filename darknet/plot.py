import numpy as np
import matplotlib.pyplot as plt

def yolov3_plot():
	""" This function plots the ROC for the YOLOv3 model by comparing 
		1000 and 2000 iteration training with each other. """

	plot_data_1 = np.load("ROC/IoU_0.5_it1000_Yolo.npz",allow_pickle=True)
	plot_data_2 = np.load("ROC/IoU_0.7_it1000_Yolo.npz",allow_pickle=True)
	plot_data_3 = np.load("ROC/IoU_0.9_it1000_Yolo.npz",allow_pickle=True)

	data_1 = plot_data_1['arr_0']
	data_2 = plot_data_2['arr_0']
	data_3 = plot_data_3['arr_0']

	x1 = [item[0] for item in data_1]
	y1 = [item[1] for item in data_1]

	x2 = [item[0] for item in data_2]
	y2 = [item[1] for item in data_2]

	x3 = [item[0] for item in data_3]
	y3 = [item[1] for item in data_3]

	# Plot
	plt.subplot(121)
	plt.plot(x1, y1, 'ro-', label='IoU Threshold 0.5', markersize=2)
	plt.plot(x2, y2, 'go-', label='IoU Threshold 0.7', markersize=2)
	plt.plot(x3, y3, 'bo-', label='IoU Threshold 0.9', markersize=2)
	plt.xlabel("False Positive Rate [-]")
	plt.ylabel("True Positive Rate [-]")
	plt.title('YOLOv3 Model 1000 Iterations')
	plt.legend()
	plt.ylim(0, 1)
	plt.grid()



	plot_data_4 = np.load("ROC/IoU_0.5_it2000_Yolo.npz",allow_pickle=True)
	plot_data_5 = np.load("ROC/IoU_0.7_it2000_Yolo.npz",allow_pickle=True)
	plot_data_6 = np.load("ROC/IoU_0.9_it2000_Yolo.npz",allow_pickle=True)

	data_4 = plot_data_4['arr_0']
	data_5 = plot_data_5['arr_0']
	data_6 = plot_data_6['arr_0']

	x4 = [item[0] for item in data_4]
	y4 = [item[1] for item in data_4]

	x5 = [item[0] for item in data_5]
	y5 = [item[1] for item in data_5]

	x6 = [item[0] for item in data_6]
	y6 = [item[1] for item in data_6]

	# Plot
	plt.subplot(122)
	plt.plot(x4, y4, 'ro-', label='IoU Threshold 0.5', markersize=2)
	plt.plot(x5, y5, 'go-', label='IoU Threshold 0.7', markersize=2)
	plt.plot(x6, y6, 'bo-', label='IoU Threshold 0.9', markersize=2)
	plt.xlabel("False Positive Rate [-]")
	plt.ylabel("True Positive Rate [-]")
	plt.title('YOLOv3 Model 2000 Iterations')
	plt.legend()
	plt.ylim(0, 1)
	plt.grid()
	plt.show()
	
def yolov3_tiny_plot():
	""" This function plots the ROC for the YOLOv3 Tiny model by comparing 
		1000 and 2000 iteration training with each other. """

	plot_data_1 = np.load("ROC/IoU_0.5_it1000_Yolo_Tiny.npz",allow_pickle=True)
	plot_data_2 = np.load("ROC/IoU_0.7_it1000_Yolo_Tiny.npz",allow_pickle=True)
	plot_data_3 = np.load("ROC/IoU_0.9_it1000_Yolo_Tiny.npz",allow_pickle=True)

	data_1 = plot_data_1['arr_0']
	data_2 = plot_data_2['arr_0']
	data_3 = plot_data_3['arr_0']

	x1 = [item[0] for item in data_1]
	y1 = [item[1] for item in data_1]

	x2 = [item[0] for item in data_2]
	y2 = [item[1] for item in data_2]

	x3 = [item[0] for item in data_3]
	y3 = [item[1] for item in data_3]

	# Plot
	plt.subplot(121)
	plt.plot(x1, y1, 'ro-', label='IoU Threshold 0.5', markersize=2)
	plt.plot(x2, y2, 'go-', label='IoU Threshold 0.7', markersize=2)
	plt.plot(x3, y3, 'bo-', label='IoU Threshold 0.9', markersize=2)
	plt.xlabel("False Positive Rate [-]")
	plt.ylabel("True Positive Rate [-]")
	plt.title('YOLOv3 Tiny Model 1000 Iterations')
	plt.legend()
	plt.ylim(0, 1)
	plt.grid()



	plot_data_4 = np.load("ROC/IoU_0.5_it2000_Yolo_Tiny.npz",allow_pickle=True)
	plot_data_5 = np.load("ROC/IoU_0.7_it2000_Yolo_Tiny.npz",allow_pickle=True)
	plot_data_6 = np.load("ROC/IoU_0.9_it2000_Yolo_Tiny.npz",allow_pickle=True)

	data_4 = plot_data_4['arr_0']
	data_5 = plot_data_5['arr_0']
	data_6 = plot_data_6['arr_0']

	x4 = [item[0] for item in data_4]
	y4 = [item[1] for item in data_4]

	x5 = [item[0] for item in data_5]
	y5 = [item[1] for item in data_5]

	x6 = [item[0] for item in data_6]
	y6 = [item[1] for item in data_6]

	# Plot
	plt.subplot(122)
	plt.plot(x4, y4, 'ro-', label='IoU Threshold 0.5', markersize=2)
	plt.plot(x5, y5, 'go-', label='IoU Threshold 0.7', markersize=2)
	plt.plot(x6, y6, 'bo-', label='IoU Threshold 0.9', markersize=2)
	plt.xlabel("False Positive Rate [-]")
	plt.ylabel("True Positive Rate [-]")
	plt.title('YOLOv3 Tiny Model 2000 Iterations')
	plt.legend()
	plt.ylim(0, 1)
	plt.grid()
	plt.show()

# The main program
#yolov3_plot()
yolov3_tiny_plot()
