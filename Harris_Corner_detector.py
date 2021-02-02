from PIL import Image
import numpy as np

img_R = np.array(Image.open('im6.png').convert('L'))
#img_L = np.array(Image.open('im2.png').convert('L'))
img_R = np.asarray(img_R)
#img_L = np.asarray(img_L)
x_derivatives = np.zeros((img_R.shape[0], img_R.shape[1]))
y_derivatives = np.zeros((img_R.shape[0], img_R.shape[1]))
Ix2 = np.zeros((img_R.shape[0], img_R.shape[1]))
Iy2 = np.zeros((img_R.shape[0], img_R.shape[1]))
Ixy = np.zeros((img_R.shape[0], img_R.shape[1]))
Corners = np.zeros((img_R.shape[0], img_R.shape[1]))
H = np.zeros((2,2))
k = 0.15
threshold = 1000000
for i in range (1,img_R.shape[0]-1):
    for j in range(1,img_R.shape[1]-1):
        x_derivatives[i,j] = int(img_R[i,j+1]) - int(img_R[i,j-1]) #central difference
        y_derivatives[i,j] = int(img_R[i+1,j]) - int(img_R[i-1,j])
        Ix2[i,j] = x_derivatives[i,j]**2
        Iy2[i,j] = y_derivatives[i,j]**2
        Ixy[i,j] = x_derivatives[i,j] * y_derivatives[i,j]
for i in range (1,img_R.shape[0]-1):
    for j in range(1,img_R.shape[1]-1):
        Sx2 = np.sum(Ix2[i-1:i+2,j])
        Sy2 = np.sum(Iy2[i-1:i+2,j])
        Sxy = np.sum(Ixy[i-1:i+2,j])
        H[0][0] = Sx2
        H[0][1] = Sxy
        H[1][0] = Sxy
        H[1][1] = Sy2
        R = np.linalg.det(H)-k*(np.trace(H))**2
        if R > threshold:
            Corners[i,j] = R

Corners = np.asarray(Corners, dtype=np.uint8)
img2= Image.fromarray(Corners)
img2.save('Harris_Corner_Detector.png')
img2.show()
