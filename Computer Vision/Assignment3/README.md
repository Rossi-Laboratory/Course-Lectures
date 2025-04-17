# HW3: Camera Calibration

**Course:** IIAI30013 - Computer Vision  
**Instructor:** YuanFu Yang  
**TA:** 陳政錡  
**Institute:** Institute of Artificial Intelligence Innovation

## 📅 Deadline
- **Due:** 4/29 23:59
- **Late Policy:** -1 point per day (up to 3 days)
- **Submission:** Submit both `HW3_CameraCalibration.ipynb` and a report (6 questions) in `.zip` and `.pdf` formats.

## 🧰 Provided Files
- `Point3D.txt`: 3D world coordinates (36 points)
- `image1.npy`, `image2.npy`: 2D image coordinates (36 points)
- `clicker.py`: Manual corner annotation (follow top-left to bottom-right order)
- `visualize.py`: 3D plotting utility for objects and camera positions

## 🧪 Functions to Implement
1. `Project_Matrix(point2D, point3D)`  
   Compute projection matrix via least-squares (eigenvector method).
2. `KRt(P)`  
   Decompose projection matrix into intrinsic matrix K, rotation R, and translation t (Gram-Schmidt or QR).

## 📋 Report Contents
- **A.** Compute the projection matrix (10%)
- **B.** Decompose to K, R, t (10%)
- **C.** Reproject 2D points and calculate RMSE, include visual results (10%)
- **D.** Plot camera poses, compute angle between them (10%)
- **E.** Print chessboard, paste on a box, take two photos, repeat A-D (40%)
- **F.** Bonus: Automate 2D corner detection (Hough Transform, etc.) (20%)

## 💻 Tools
- Can be done on **Google Colab** or your **local PC**  
  [Colab Link](https://colab.research.google.com/?hl=zh-tw)

---

For questions, please contact the TA on E3.
