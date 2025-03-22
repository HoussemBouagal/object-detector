# 🔍 Object Detection Application  

A simple **Object Detection** application built with **Python**, featuring a **Tkinter-based GUI** and powered by **OpenCV** for object recognition.  

---

## ✨ Features  

✅ **Load Image for Detection** – Upload an image, and the app will identify objects within it.  
📷 **Real-Time Detection with Camera** – Start the webcam and detect objects live.  
ℹ️ **Developer Information** – View the developer's details and contact information.  
🎨 **Customizable Interface** – Styled buttons for better user experience and aesthetics.  

---

## 📞 Requirements  

To run this project, install the following Python libraries:  

- **Tkinter** (pre-installed with Python)  
- **OpenCV** (`opencv-python`)  
- **Pillow**  

Install dependencies using:  

```bash
pip install opencv-python pillow
```

---

## 📂 Required Files  

Ensure these files are in the project directory:  

📌 **`coco.names`** – Contains object class names.  
📌 **`ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`** – Configuration file for the object detection model.  
📌 **`frozen_inference_graph.pb`** – Pre-trained object detection model.  
📌 **`Recognition.png`** – Icon image for the application.  

---

## 🚀 How to Run  

1⃣ **Clone or download** the repository.  
2⃣ Ensure all required files are in the project directory.  
3⃣ Run the application using:  

```bash
python objet.py
```

---

## 🎮 How to Use  

### 📷 Load an Image  
1. Click **"Load Image"**.  
2. Select an image from your computer.  
3. The application will display detected objects.  

### 📺 Start the Camera  
1. Click **"Start Camera"**.  
2. The webcam will open, detecting objects in real-time.  
3. Press **`q`** to stop the camera.  

### ℹ️ View Developer Info  
Click **"Developer Info"** to display the developer's contact details.  

---

## 🔔 Notes  

⚡ The application uses a **pre-trained model** for object detection. Ensure all required files are in the project directory.  
📏 For better performance, set the **camera resolution** to a suitable size (e.g., **740x580**).  

---

## 👨‍💻 Developer  

**👤 Name:** Houssem Bouagal  
✉️ **Email:** mouhamedhoussem813@gmail.com  

---

## 🚀 Future Enhancements  

🔹 Add a feature to **save detection results**.  
🌍 Implement **multi-language support**.  
⚙️ Allow users to **adjust model parameters** (e.g., confidence thresholds).  

---

## 📜 License  

🧠 This project is **open-source** and available for modification and use.  

---

