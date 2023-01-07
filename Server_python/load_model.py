# NOTE: file nay demo viec thuc hien load mot trained model vao va su dung

import os
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vsu
from object_detection.builders import model_builder
from object_detection.utils import config_util

import cv2 
import numpy as np
#from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter
import serial
import pickle
#matplotlib inline
data = [0]
datapkl_path='data.pkl'

# Declare variable

pathToModel = "export"
piplineConfigFile = "export/pipeline.config"
label_map_file = "label_map.pbtxt"

# DEFINE FUNCTION

#ham nhan anh vao va tra ra mot detection
@tf.function
def detect_fn(image):
	image, shapes = detection_model.preprocess(image)
	prediction_dict = detection_model.predict(image, shapes)
	detection = detection_model.postprocess(prediction_dict, shapes)
	return detection

# HAM DETECT TU WEBCAM - VID
@tf.function
def detect_from_video(camera):
	print("Starting detect from video...")
	cap = cv2.VideoCapture(camera)
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

	while cap.isOpened(): 
	    ret, frame = cap.read()
	    image_np = np.array(frame)
	    
	    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
	    detections = detect_fn(input_tensor)
	    
	    num_detections = int(detections.pop('num_detections'))
	    detections = {key: value[0, :num_detections].numpy()
	                  for key, value in detections.items()}
	    detections['num_detections'] = num_detections

	    # detection_classes should be ints.
	    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

	    label_id_offset = 1
	    image_np_with_detections = image_np.copy()
	 
	    vsu.visualize_boxes_and_labels_on_image_array(
	                image_np_with_detections,
	                detections['detection_boxes'],
	                detections['detection_classes']+label_id_offset,
	                detections['detection_scores'],
	                category_index,
	                use_normalized_coordinates=True,
	                max_boxes_to_draw=3,
	                min_score_thresh=.8,
	                agnostic_mode=False)
	    #Minh log
	    #print(detections['detection_classes'].astype(np.int64))
	    
	    highest_index = 0
	    change = detections['detection_scores'][0]
	    nameClass = detections['detection_classes'][0] + 1

	    if detections['detection_scores'][0] >= 0.9:
	    	print("{} , {}".format(change, category_index[nameClass]['name']))
	    	# Mở một file để ghi dữ liệu
	    	with open(datapkl_path, 'wb') as file:
	            # Sử dụng hàm pickle.dump() để lưu biến data vào file
	            data.append(int(detections['detection_classes'][0]))
	            pickle.dump(data, file)
	            # In giá trị của biến data
	            print(data)
	    	
	    cv2.imshow('object detection',  cv2.resize(image_np_with_detections, (800, 600)))
	    
	    if cv2.waitKey(10) & 0xFF == ord('q'):
	        cap.release()
	        cv2.destroyAllWindows()
	        break

# HAM DETECT TU IMAGE
@tf.function
def detect_from_image(image_path, image_path_detect):
	print("Starting detect from image...")
	img = cv2.imread(image_path)
	image_np = np.array(img)
	tf.config.run_functions_eagerly(True)

	input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, axis=0), dtype=tf.float32)
	detections = detect_fn(input_tensor)

	num_detections = int(detections.pop('num_detections'))
	detections = {key: value[0, :num_detections].numpy()
	              for key, value in detections.items()}
	detections['num_detections'] = num_detections

	# detection_classes should be ints.
	detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

	label_id_offset = 1
	image_np_with_detections = image_np.copy()

	vsu.visualize_boxes_and_labels_on_image_array(
	            image_np_with_detections,
	            detections['detection_boxes'],
	            detections['detection_classes']+label_id_offset,
	            detections['detection_scores'],
	            category_index,
	            use_normalized_coordinates=True,
	            max_boxes_to_draw=1,
	            min_score_thresh=.9,
	            agnostic_mode=False)

	highest_index = 0
	if detections['detection_scores'][0] >= 0.85:
		print(category_index[detections['detection_classes'][0] + 1])
		
	cv2.imwrite(image_path_detect, image_np_with_detections)
	# plt.imshow(cv2.cvtColor(image_np_with_detections, cv2.COLOR_BGR2RGB))
	# plt.show()

	return category_index[detections['detection_classes'][0] + 1]

#=============================================================================================
# start of program
configs = config_util.get_configs_from_pipeline_file(piplineConfigFile)
detection_model = model_builder.build(model_config= configs['model'], is_training= False)

#print(configs)
ckpt = tf.compat.v2.train.Checkpoint(model= detection_model)
ckpt.restore(os.path.join(pathToModel, 'ckpt-3')).expect_partial()

#----------------------------
category_index = label_map_util.create_category_index_from_labelmap(label_map_file)
#print(category_index)

# image_path = 'imag_test/WIN_20221210_11_04_40_Pro.jpg'
# detect_from_image(image_path)



