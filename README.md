Object Detection Application

This project is a simple Object Detection application built with Python using the Tkinter library for the graphical user interface (GUI) and OpenCV for object detection.

Features

Load Image for Detection: Users can upload an image file, and the application will detect objects in the image.

Real-Time Detection with Camera: Start the camera to detect objects in real-time.

Developer Information: Displays the developer's name and contact information.

Customizable Interface: Includes styled buttons for better usability and aesthetics.

Requirements

To run this project, you need to install the following Python libraries:

tkinter (comes pre-installed with Python)

opencv-python

Pillow

You can install the required libraries using the following command:

pip install opencv-python pillow

Required Files

Make sure the following files are in the same directory as the application:

coco.names: Contains the names of classes for object detection.

ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt: Configuration file for the object detection model.

frozen_inference_graph.pb: Pre-trained model for object detection.

Recognition.png: Icon image for the application.

How to Run

Clone or download this repository to your local machine.

Ensure all required files are in the project directory.

Run the application using the following command:

python object_detection_app.py

How to Use

Load Image:

Click the "Load Image" button.

Select an image file from your computer.

The application will display the detected objects in the image.

Start Camera:

Click the "Start Camera" button.

The application will open the webcam and detect objects in real-time.

Press the q key to stop the camera.

Developer Information:

Click the "Developer Info" button to view the developer's contact information.

Notes

The application uses a pre-trained model for object detection. Ensure all required files are present in the project directory.

For better performance, ensure the camera resolution is set to a suitable size (e.g., 740x580).

Developer Information

Name: Houssem Bouagal

Email: mouhamedhoussem813@gmail.com

Future Enhancements

Add a feature to save the detection results.

Provide multi-language support for the user interface.

Allow users to adjust model parameters, such as confidence thresholds.

License

This project is open-source and available for use and modification.

