# Import Data
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
point3D = np.loadtxt('.\data\Point3D.txt', delimiter=' ')
point2D1 = np.load('image1.npy')
point2D2 = np.load('image2.npy')
img1 = cv2.imread('data/image1.jpeg')
img2 = cv2.imread('data/image2.jpeg')
```

### (A) Compute the projection matrix *P* from a set of 2D-3D point correspondences by using the leastsquares (eigenvector) method for each image.

A pair of corresponding point in homogenous coordinate satisfies:

$$
\begin{bmatrix}
u \\
v \\
1
\end{bmatrix}
\sim
\mathbf{P}
\begin{bmatrix}
X \\
Y \\
Z \\
1
\end{bmatrix}
$$

Where $\sim$ means equality up to scale. We can derive two equations:

$$
\begin{align}
x = \frac
{p_{11} X + p_{12} Y + p_{13} Z + P_{14}}
{p_{31} X + p_{32} Y + p_{33} Z + P_{34}}
,
y = \frac
{p_{21} X + p_{22} Y + p_{23} Z + P_{24}}
{p_{31} X + p_{32} Y + p_{33} Z + P_{34}}
\end{align}
$$

Rearrange it in matrix form:

$$
\begin{pmatrix}
X & Y & Z  & 1 & 0 & 0 & 0 & 0 & -uX & -uY & -uZ & -u \\
0 & 0 & 0 & 0 & X & Y & Z & 1 & -vX & -vY & -vZ & -v \\
&&&&&&\vdots\\
&&&&&&\vdots\\
&&&&&&\vdots\\
\end{pmatrix}
\begin{pmatrix}
p_{11} \\ p_{12} \\ p_{13} \\ \vdots \\ p_{34}
\end{pmatrix}
= \bb{0}
$$

It is a homogeneous system **A p = 0**.  
Since there are 12 unknowns, but the actual degree of freedom of **p** is 11 (5 in **K**, 3 in **R**, and 3 in **T**), we add one constraint to the system: ‖**p**‖ = 1.

Usually, more than 6 correspondences are given, so the system doesn't have a unique solution. Instead, we try to find the **p** that minimizes ‖**A** **p** − **0**‖. The solution is the eigenvector of **AᵀA** (i.e., **A<sup>T</sup>A**) that corresponds to the minimum eigenvalue. The proof is given in the appendix.

Another way to solve this system is to use the least squares method. However, since the unit norm constraint cannot be directly expressed in the system, we use another constraint instead:

$$
p_{11} + p_{12} + \ldots + p_{34} = 1
$$

After adding constraint, the system becomes:

$$
\begin{pmatrix}
X & Y & Z  & 1 & 0 & 0 & 0 & 0 & -xX & -xY & -xZ & -x \\
0 & 0 & 0 & 0 & X & Y & Z & 1 & -yX & -yY & -yZ & -y \\
 & & & & & &\vdots\\
 & & & & & &\vdots\\
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
p_{11} \\ p_{12} \\ p_{13} \\ \vdots \\ p_{34}
\end{pmatrix} = 
\begin{pmatrix}
0 \\ 0 \\ 0 \\ \vdots \\ 1
\end{pmatrix}
$$


```python
def Projection_Matrix(point2D, point3D):
    ########################################################################
    # TODO:                                                                #
    #   Using 2D coordinator and 3D coordinator,                           #
    #   , calculate the 3D to 2D projection matrix P                       #
    ########################################################################
    

    
    ########################################################################
    #                                                                      #
    #                           End of your code                           #
    #                                                                      # 
    ########################################################################
    return M
```


```python
P1 = Projection_Matrix(point2D1, point3D)
P2 = Projection_Matrix(point2D2, point3D)
```


```python
# Verify the projection matrix (P), use P to project the 3D coordinator to 2D coordinates
# input: P, 3D world coordinator, output: 2D image coordinator
def Verify(P,point3D):
    lenPoints = len(point3D)
    ThreeD = np.zeros((lenPoints,4),dtype=np.float32)
    for i in range(lenPoints):
        for j in range(3):
            ThreeD[i,j]=point3D[i,j]
    
    for i in range(lenPoints):
        ThreeD[i,3]=1

    TwoDD = np.zeros((lenPoints,3),dtype=np.float32)

    for i in range(lenPoints):
        TwoDD[i] = P.dot(ThreeD[i])
        TwoDD[i] = TwoDD[i]/TwoDD[i,-1]
    
    SE = 0.000
    
    for i in range(lenPoints):
        SE = SE + np.square(TwoDD[i,0]-point2D1[i,0])+np.square(TwoDD[i,1]-point2D1[i,1])
    RMSE = np.sqrt(SE/lenPoints)
    
    return RMSE, TwoDD
```


```python
def Project(img, point2D, TwoD, save_name):
    x = point2D[:,0]
    y = point2D[:,1]
    x1 = TwoD[:,0]
    y1 = TwoD[:,1]
    fig = plt.figure()
    img12 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(20,10))
    plt.plot(x,y,"o", label="original point")
    plt.plot(x1,y1,"x", label="projected point")
    plt.legend(loc='upper right')
    plt.imshow(img12)
    plt.savefig('./output/' + save_name + '.png')
```


```python
RMSE1, TwoDD1 = Verify(P1,point3D)
RMSE2, TwoDD2 = Verify(P2,point3D)
print(RMSE1, RMSE2)
```

    1.215362935781567 52.01368724958299
    


```python
Project(img1, point2D1, TwoDD1,save_name='verify of chessboard_1')
```


    <Figure size 432x288 with 0 Axes>



<img style="float: left;" src="https://drive.google.com/uc?export=view&id=1YvbLsEp0PH7w_rqHYw9V9CAoYUS3YTz7" width="40%">



```python
Project(img2, point2D2, TwoDD2,save_name='verify of chessboard_2')
```


    <Figure size 432x288 with 0 Axes>



<img style="float: left;" src="https://drive.google.com/uc?export=view&id=1rZdtLEQ0DpUgaOV7aOJB3acaSeOL2RGu" width="40%">


### (B) Decompose the two computed projection matrices from (A) into the camera intrinsic matrices K, rotation matrices R and translation vectors t by using the Gram-Schmidt process.

### K, R, T

**P** = **K** [**R** | **T**] = [**KR** | **KT**]  
    = [**P**<sub>3×3</sub> | **P**<sub>4</sub>] = [**M** | **P**<sub>4</sub>]

That is,

**M** = **K** **R**  
**P**<sub>4</sub> = **K** **T**

We know **K** is upper triangular and **R** is orthogonal.  
We can utilize **RQ-decomposition** to find **K**, **R**:

**M** = **Ŕ** **Q̂** = **K** **R**  
∴ **K** = **Ŕ**, **R** = **Q̂**

If **RQ-decomposition** is not available (e.g., in MATLAB), we can use **QR-decomposition** instead by decomposing **M**⁻¹.  
This works because the inverse of an upper triangular matrix is also upper triangular, and the inverse of an orthogonal matrix is also orthogonal:

**M**⁻¹ = **Q̇** **Ṙ**  
⇒ **M** = (**Q̇** **Ṙ**)<sup>−1</sup> = **Ṙ**⁻¹ **Q̇**⁻¹ = **K** **R**  
∴ **K** = **Ṙ**⁻¹, **R** = **Q̇**⁻¹

And **T** is simply:

**T** = **K**⁻¹ **P**<sub>4</sub>

```python
def KRt(P):
    ########################################################################
    # TODO:                                                                #
    #   Extract the intrinsic matrix (K), rotation matrix (R)              #
    #   , and translation vector(T) from the projection matrix.            #
    ########################################################################
    

    
    ########################################################################
    #                                                                      #
    #                           End of your code                           #
    #                                                                      # 
    ########################################################################
    return K2, R1, T
```


```python
K1, R1, T1 = KRt(P1)
K2, R2, T2 = KRt(P2)
```


```python
np.savetxt("./output/intrinsic matrices of chessboard_1.txt",K1)
np.savetxt("./output/rotation matrices of chessboard_1.txt",R1)
np.savetxt("./output/translation vectors of chessboard_1.txt",T1)
np.savetxt("./output/intrinsic matrices of chessboard_2.txt",K2)
np.savetxt("./output/rotation matrices of chessboard_2.txt",R2)
np.savetxt("./output/translation vectors of chessboard_2.txt",T2)
```

(C) Re-project 2D points on each of the chessboard images by using the computed intrinsic matrix, rotation matrix and translation vector. Show the results (2 images) and compute the point reprojection root-mean-squared errors. 


```python
def ReProject2D(K, R, T, point2D, point3D):
    lenPoints = len(point3D)
    Pro = np.zeros((3,4),dtype=np.float32)
    Pro[0,0] = 1
    Pro[1,1] = 1
    Pro[2,2] = 1
    Rt = np.zeros((4,4),dtype=np.float32)
    for i in range(3):
        for j in range(3):
            Rt[i,j]=R[i,j]
    Rt[0,3]=T[0]
    Rt[1,3]=T[1]
    Rt[2,3]=T[2]
    Rt[3,3] = 1
    KPRt = K.dot(Pro).dot(Rt)
    
    ThreeD = np.zeros((lenPoints,4),dtype=np.float32)
    for i in range(lenPoints):
        for j in range(3):
            ThreeD[i,j]=point3D[i,j]
    
    for i in range(lenPoints):
        ThreeD[i,3]=1
    
    TwoD = np.zeros((lenPoints,3),dtype=np.float32)
    for i in range(lenPoints):
        TwoD[i] = KPRt.dot(ThreeD[i])
        TwoD[i] = TwoD[i]/TwoD[i,-1]
    
    SE = 0.000
    for i in range(lenPoints):
        SE = SE + np.square(TwoD[i,0]-point2D[i,0])+np.square(TwoD[i,1]-point2D[i,1])
    
    RMSE = np.sqrt(SE/lenPoints)
    
    SEX = 0.000
    for i in range(lenPoints):
        SEX = SEX + np.square(TwoD[i,0]-point2D[i,0])
    
    SEY = 0.000
    for i in range(lenPoints):
        SEY = SEY + np.square(TwoD[i,1]-point2D[i,1])    
        
    return RMSE, TwoD, SEX, SEY
```


```python
RMSE1, TwoD1, SE_X1, SE_Y1 = ReProject2D(K1, R1, T1, point2D1, point3D)
RMSE2, TwoD2, SE_X2, SE_Y2 = ReProject2D(K2, R2, T2, point2D2, point3D)
```


```python
print("RMSE of 1st image: ",RMSE1)
print("RMSE of 2nd image: ",RMSE2)
```

    RMSE of 1st image:  13.142565050815152
    RMSE of 2nd image:  6.219724416182343
    


```python
Project(img1, point2D1, TwoD1,save_name='ReProject2D of chessboard_1')
```


    <Figure size 432x288 with 0 Axes>



<img style="float: left;" src="https://drive.google.com/uc?export=view&id=1MXbJIHBtnjaHX8yq9NuZb3X-1Z5TTuul" width="40%">



```python
Project(img2, point2D2, TwoD2,save_name='ReProject2D of chessboard_2')
```


    <Figure size 432x288 with 0 Axes>



<img style="float: left;" src="https://drive.google.com/uc?export=view&id=1n8mQvbIT6M6ByyhLD7syGUViDX4ZSIo8" width="40%">


### (D) Plot camera poses for the computed extrinsic parameters (R, t) and then compute the angle between the two camera pose vectors.


```python
from visualize import visualize
# Input:
# pts: 36x3 3D points
# R1: 3x3 rotation matrix of image 1
# T1: 3x1 translation vector of image 1
# R2: 3x3 roatation matrix of image 2
# T2: 3x1 translation vector of image 2
```


```python
T11 = T1.reshape(3,1)
T22 = T2.reshape(3,1)
```


```python
save_name='3D'
visualize(point3D, R1, T1.reshape(3,1), R2, T2.reshape(3,1),save_name)
```

    Angle between two cameras:  30.97297189055029
    


<img style="float: left;" src="https://drive.google.com/uc?export=view&id=1dMiojbZ-IWeg42TEWKE4YyGr7izbBZFx" width="40%">


### (E) Print out two “chessboard.png” in the attached file and paste them on a box. Take two pictures from different angles. For each image, perform the steps above (A ~ D).


```python
cb = cv2.imread('data/chessboard.png')
cb = cv2.cvtColor(cb, cv2.COLOR_BGR2RGB)
plt.imshow(cb)
```




    <matplotlib.image.AxesImage at 0x22b92f387b8>




<img style="float: left;" src="https://drive.google.com/uc?export=view&id=1OFdwS-JH8Wm7m9xK7NlRFntkH9J9CzhY" width="40%">



```python

```

### (F) Instead of mark the 2D points by hand, you can find the 2D points in your images automatically by using corner detection, hough transform, etc.


```python

```
