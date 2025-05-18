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

## 🗂️ Submission Requirements

Submit the following files:

1. `.py` or `.ipynb` file with your implementation
2. 3 validation result images at:
   - Epoch 5
   - Epoch 10
   - Epoch 20
3. 10 predicted segmentation images from the test set  
   (saved in a folder named `predict`)
4. A **report in PDF format**, including:
   - Quantitative analysis using **PSNR** and **IoU**
   - Qualitative visual comparisons

---

## 📆 Deadline & Late Policy

- 📅 **Due Date**: May 20, 23:59
- 🕒 **Late Penalty**: -1 point per day
- ❌ **Final Deadline**: 3 days after due date (no submission accepted afterward)

---

## ⚙️ Rules & Scoring

1. You **may use** pre-trained models and fine-tune them.
2. You **may also train from scratch** (will receive **higher scores**).
3. Implement and report:
   - Per-class **IoU** and mean **IoU**
   - Per-image **PSNR** and average **PSNR**

---

## 📊 Evaluation Metrics

### 1. IoU (Intersection over Union)

Used to compare predicted masks and ground truth masks for each class.

### 2. PSNR (Peak Signal-to-Noise Ratio)

Used to assess the pixel-wise similarity between predicted and ground truth masks.

---

## 🧪 Example Validation Output (per Epoch)

| Epoch 5 | Epoch 10 | Epoch 20 |
|---------|----------|----------|
| ![ep5](images/epoch5.png) | ![ep10](images/epoch10.png) | ![ep20](images/epoch20.png) |

---

## 🎯 Example Performance Results

### Example A
- PSNR: **17.71**
- IoU:
  - Armrest (brown): 97.13%
  - Leg (black): 95.99%
  - Seat Base (yellow): 85.40%
  - Backrest (gray): 97.28%

### Example B
- PSNR: **17.21**
- IoU:
  - Leg (black): 77.18%
  - Seat Base (yellow): 98.49%

### Example C
- PSNR: **11.40**
- IoU:
  - Leg (black): 95.80%
  - Seat Base (yellow): 90.30%
  - Backrest (gray): 94.92%

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

Feel free to reach out to the instructor if you have any questions or need clarification.

📧 Email: yfyangd@nycu.edu.tw

---

© 2025 Institute of Artificial Intelligence Innovation, National Yang Ming Chiao Tung University

