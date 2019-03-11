import cv2
import numpy as np

img = cv2.imread('../assets/imori.jpg')
img2 = img.copy()
H, W = img2.shape[:2]
img2[:H//2, :W//2] = img2[:H//2, :W//2, (2, 1, 0)]
cv2.imshow('', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
