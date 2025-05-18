
# HW4: Semantic Segmentation - Sofa Component Segmentation

**Instructor**: Prof. YuanFu Yang  
📧 Email: yfyangd@nycu.edu.tw  
🧑‍🏫 Course: IIAI30013 – Computer Vision  
🏛️ Institute of Artificial Intelligence Innovation

---

## 📘 Assignment Description

This homework focuses on **Semantic Segmentation**, with the goal of **segmenting components of sofas**.

- Input: RGB image of a sofa  
- Output: Pixel-wise segmentation map labeling different sofa parts

---

## 🖼️ Segmentation Example

| Input Image | Ground Truth | Predicted Output |
|-------------|--------------|------------------|
| ![Input](https://drive.google.com/uc?export=view&id=1ny_p8P2sLOxnk_jDtOK1ynzxFyPR3umC) | ![GT](https://drive.google.com/uc?export=view&id=1pTFZLKo_6noF4uLAdbx-wJK54Ryd_T_d) | ![Output](https://drive.google.com/uc?export=view&id=1O8VAsMb0lKzsPvdDffGTES6Fie0Kyzkk) |

---

## 📁 Dataset

- **Training Set**: 400 labeled images with ground truth masks
- **Test Set**: 10 images with ground truth

> ⚠️ **Do not use ground truth for the test set during training. This is considered cheating.**

---

## 🗂️ Submission Checklist

Submit the following files:

1. `.py` or `.ipynb` file with your implementation  
2. 3 validation result images at:
   - Epoch 5
   - Epoch 10
   - Epoch 20

| Epoch 5 | Epoch 10 | Epoch 20 |
|---------|----------|----------|
| ![ep5](https://drive.google.com/uc?export=view&id=12RSdCIZdZDH2R7jWqwFQ2pdF21G6sfml) | ![ep10](https://drive.google.com/uc?export=view&id=1sbQla6kTO4ShAB_VVI8x1j6-ZH_QqpL1) | ![ep20](https://drive.google.com/uc?export=view&id=1d3lCJfMcXdolP0XRDHpUnoOHmgpB2BQB) |

3. 10 predicted segmentation images from the test set (in `predict/` folder)  
4. A **PDF report**, including:
   - Quantitative analysis using **PSNR** and **IoU**
   - Qualitative visual comparisons

---

## 🚀 Running on Google Colab

You may choose to run the training and testing on [Google Colab](https://colab.research.google.com/?hl=zh-tw), which supports GPU acceleration.

### 🔧 Steps:

1. Upload your code (`.ipynb` or `.py`) and dataset folders (`train/`, `val/`, `test/`) to Colab.
2. Mount Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

3. Install required packages (if needed):

```bash
!pip install torch torchvision matplotlib scikit-image
```

4. Run your training script:

```python
!python train.py --train_dir ./train --val_dir ./val --epochs 20 --batch_size 8 --lr 0.001
```

---

## 🔍 Inference Instructions

After training, you must generate segmentation results for the test set and save them in a folder called `predict/`.

### Example inference script:

```python
from model import YourSegmentationModel
import cv2
import torch
import os

# Load trained model
model = YourSegmentationModel()
model.load_state_dict(torch.load('checkpoint_epoch20.pth'))
model.eval()

# Inference loop
test_dir = './test'
output_dir = './predict'
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(test_dir):
    img = cv2.imread(os.path.join(test_dir, filename))
    img_input = preprocess(img)  # your preprocessing
    with torch.no_grad():
        pred = model(img_input.unsqueeze(0))  # add batch dimension
    pred_mask = postprocess(pred)  # your postprocessing
    cv2.imwrite(os.path.join(output_dir, filename), pred_mask)
```

> 🔔 Make sure your prediction outputs have the same filename as the original test images.

---

## 🎯 Example Performance Results

### Example A

![Example A](https://drive.google.com/uc?export=view&id=11HTFhjpjeQILEZPGncWqtPdoTJGvM5WK)

```
PSNR: 17.71  
IoU: Armrest (brown): 97.13%, Leg (black): 95.99%,  
Seat Base (yellow): 85.40%, Backrest (gray): 97.28%
```

---

### Example B

![Example B](https://drive.google.com/uc?export=view&id=1rBU72f3l0dGvJEvJVqKsuMudNLPi3C1u)

```
PSNR: 17.21  
IoU: Leg (black): 77.18%, Seat Base (yellow): 98.49%
```

---

### Example C

![Example C](https://drive.google.com/uc?export=view&id=1dZSK0ZbJArXt-uJ6bE9bwg3we-ghv0Uc)

```
PSNR: 11.40  
IoU: Leg (black): 95.80%, Seat Base (yellow): 90.30%,  
Backrest (gray): 94.92%
```

---

## 📈 Final Result Breakdown (Example)

| Component        | Color (RGB)       | IoU (%) |
|------------------|------------------|---------|
| Cushion          | (60, 180, 90)     | 76.76   |
| Armrest          | (110, 40, 40)     | 77.64   |
| Leg              | (50, 10, 70)      | 67.86   |
| Seat Base        | (180, 200, 60)    | 75.83   |
| Backrest         | (100, 100, 100)   | 60.20   |
| **Overall mIoU** | –                | **71.66** |

---

## ❓ Questions?

📧 Email: yfyangd@nycu.edu.tw

---

© 2025 Institute of Artificial Intelligence Innovation, National Yang Ming Chiao Tung University
