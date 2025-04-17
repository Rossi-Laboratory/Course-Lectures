# Camera Calibration Homework (HW3)

This assignment demonstrates how to compute the projection matrix, decompose it into camera intrinsics and extrinsics, re-project 3D points, and visualize camera pose using two views of a chessboard image.

---

## ? Import Data
The data includes 3D world coordinates, 2D image coordinates, and images of a chessboard box captured from two perspectives.

```python
import cv2
import numpy as np
import scipy.io
from scipy import signal
import scipy
import matplotlib.pyplot as plt
```

```python
point3D = np.loadtxt('./data/Point3D.txt', delimiter=' ')
point2D1 = np.load('image1.npy')
point2D2 = np.load('image2.npy')
img1 = cv2.imread('data/image1.jpeg')
img2 = cv2.imread('data/image2.jpeg')
```

---

## ?儭?(A) Compute the Projection Matrix

A pair of corresponding points in homogeneous coordinates satisfies:

```latex
\[
\begin{bmatrix}
u \\ v \\ 1
\end{bmatrix}
\sim
\mathbf{P}
\begin{bmatrix}
X \\ Y \\ Z \\ 1
\end{bmatrix}
\]
```

We can derive two equations:

```latex
\[
x = \frac{p_{11} X + p_{12} Y + p_{13} Z + p_{14}}{p_{31} X + p_{32} Y + p_{33} Z + p_{34}},\quad
y = \frac{p_{21} X + p_{22} Y + p_{23} Z + p_{24}}{p_{31} X + p_{32} Y + p_{33} Z + p_{34}}
\]
```

This can be rearranged into matrix form as \( A \mathbf{p} = 0 \), and solved using least-squares or eigenvector methods. An alternative is to constrain the solution with:

```latex
\[
p_{11} + p_{12} + \ldots + p_{34} = 1
\]
```

---

## ?妙 Code Examples

The rest of the code performs:
- Computing projection matrix `P`
- Decomposing into `K`, `R`, and `T`
- Projecting 3D to 2D and computing RMSE
- Visualizing camera poses and angle
- Optional automated 2D corner detection

Each step is embedded in Python blocks throughout the notebook or report.

---

## ? Sample Visual Outputs

- **Projection Results:** Overlay original and projected points
- **Camera Visualization:** Show 3D position and relative angles
- **Chessboard Images:** Reprojection validation

---

## ?妒 Optional Task

Use OpenCV-based automated detection (`cv2.cornerHarris`, Hough Transform, etc.) to replace manual corner labeling.

---

? For questions, contact the instructor: **yfyangd@nycu.edu.tw**
