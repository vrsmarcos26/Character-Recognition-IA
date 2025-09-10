from google.colab import drive
drive.mount('/content/drive')

!pip install -q ultralytics

!yolo task=detect mode=train model=yolov8n.pt data=/content/drive/MyDrive/Inteligencia_Artificial/custom.yaml epochs=3 imgsz=640

!yolo task=detect mode=train model=yolov8n.pt data=/content/drive/MyDrive/Inteligencia_Artificial/custom.yaml epochs=150 imgsz=640

!yolo predict model=/content/runs/detect/train2/weights/best.pt source="/content/drive/MyDrive/Inteligencia_Artificial/videoplayback.mp4"

from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image


files = list(Path('/content/runs/detect/predict').glob('*.jpg'))

fig, axs = plt.subplots(2, 2, figsize=(16,16))
axs = [ax for row in axs for ax in row]

for file, ax in zip(files, axs):
    ax.imshow(Image.open(file))
    ax.axis('off')

