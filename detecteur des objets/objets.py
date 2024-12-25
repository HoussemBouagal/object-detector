import os
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk

# Classe principale de l'application
class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Détecteur d'objets")
        self.root.geometry("400x300")
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Création des styles pour les boutons
        self.style.configure("Green.TButton", background="#90EE90", foreground="black")
        self.style.map("Green.TButton", background=[("active", "#90EE90")])

        self.style.configure("Blue.TButton", background="#87CEEB", foreground="black")
        self.style.map("Blue.TButton", background=[("active", "#87CEEB")])

        self.style.configure("Orange.TButton", background="#e67e22", foreground="black")
        self.style.map("Orange.TButton", background=[("active", "#e67e22")])

        self.camera_running = False
        self.create_widgets()

        # Utilisation d'une image comme icône de la fenêtre
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "Recognition.png")
        if os.path.exists(icon_path):
            self.icon_image = ImageTk.PhotoImage(file=icon_path)
            self.root.iconphoto(False, self.icon_image)
        else:
            print("Fichier d'icône non trouvé :", icon_path)

    def create_widgets(self):
        # Frame pour les boutons
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=20)

        # Bouton pour charger une image (Vert clair)
        self.load_image_button = ttk.Button(
            self.button_frame, text="Charger une image", command=self.load_image, style="Green.TButton"
        )
        self.load_image_button.grid(row=0, column=0, padx=10, pady=10)

        # Bouton pour démarrer la caméra (Bleu clair)
        self.start_camera_button = ttk.Button(
            self.button_frame, text="Démarrer la caméra", command=self.start_camera, style="Blue.TButton"
        )
        self.start_camera_button.grid(row=0, column=1, padx=10, pady=10)

        # Bouton pour afficher les informations du développeur (Orange)
        self.info_button = ttk.Button(
            self.button_frame, text="Info Développeur", command=self.show_developer_info, style="Orange.TButton"
        )
        self.info_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Label pour afficher le statut
        self.status_label = ttk.Label(self.root, text="")
        self.status_label.pack(pady=20)

    def load_image(self):
        img_path = filedialog.askopenfilename(title="Choisissez une image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if img_path:
            self.detect_objects_in_image(img_path)

    def start_camera(self):
        if not self.camera_running:
            self.camera_running = True
            self.detect_objects_in_camera()

    def detect_objects_in_image(self, img_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        classFile = os.path.join(current_dir, 'coco.names')
        configPath = os.path.join(current_dir, 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
        weightPath = os.path.join(current_dir, 'frozen_inference_graph.pb')

        # Vérification des fichiers nécessaires
        if not os.path.exists(classFile) or not os.path.exists(configPath) or not os.path.exists(weightPath):
            messagebox.showerror("Erreur", "Fichiers de modèle manquants.")
            return

        img = cv2.imread(img_path)

        with open(classFile, 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n')

        net = cv2.dnn_DetectionModel(weightPath, configPath)
        net.setInputSize(320, 230)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        classIds, confs, bbox = net.detect(img, confThreshold=0.5)
        self.draw_predictions(img, classIds, confs, bbox, classNames)
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def detect_objects_in_camera(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        classFile = os.path.join(current_dir, 'coco.names')
        configPath = os.path.join(current_dir, 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
        weightPath = os.path.join(current_dir, 'frozen_inference_graph.pb')

        if not os.path.exists(classFile) or not os.path.exists(configPath) or not os.path.exists(weightPath):
            messagebox.showerror("Erreur", "Fichiers de modèle manquants.")
            return

        cam = cv2.VideoCapture(0)
        cam.set(3, 740)
        cam.set(4, 580)

        with open(classFile, 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n')

        net = cv2.dnn_DetectionModel(weightPath, configPath)
        net.setInputSize(320, 230)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        while self.camera_running:
            success, img = cam.read()
            if not success:
                messagebox.showerror("Erreur", "Échec de la capture d'image.")
                break

            classIds, confs, bbox = net.detect(img, confThreshold=0.5)
            self.draw_predictions(img, classIds, confs, bbox, classNames)

            cv2.imshow('Camera', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.camera_running = False
                break

        cam.release()
        cv2.destroyAllWindows()

    def draw_predictions(self, img, classIds, confs, bbox, classNames):
        if len(classIds) != 0:
            for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 20),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), thickness=2)

    def show_developer_info(self):
        messagebox.showinfo("Info Développeur", "Nom: Houssem Bouagal\nEmail: mouhamedhoussem813@gmail.com")

if __name__ == "__main__":
    root = tk.Tk()
    app = ObjectDetectionApp(root)
    root.mainloop()
