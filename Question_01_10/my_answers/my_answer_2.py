import cv2
import numpy as np

# Read image
img = cv2.imread('../imori.jpg')
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# Gray Scaling
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

# 確認用
# 2次元の numpy array が cv2.imwrite に渡された場合は BGR でなく輝度として解釈される
print(out)
print(out.shape)

cv2.imwrite('my_answer_2.jpg', out)
cv2.imshow('Gray Scale', out)
cv2.waitKey(0)
cv2.destroyAllWindows()