import cv2
import numpy as np
from logzero import logger

# Read image
img = cv2.imread("../imori.jpg").astype(np.float)
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# Grayscale
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

# Binarization
sb2_max = 0
argmax = 0
for t in range(256):
    tmp = out.copy()
    w0_cnt = np.sum(tmp < t)
    w1_cnt = np.sum(tmp >= t)
    w0 = w0_cnt / (w0_cnt + w1_cnt)
    w1 = w1_cnt / (w0_cnt + w1_cnt)
    if w0 * w1 * (255 ** 2) > sb2_max:
        argmax = t
        sb2_max = w0 * w1 * (255 ** 2)
        logger.info(f'update: sb2_max = {sb2_max} argmax = {argmax}')
logger.info(f'argmax sb2_max is {argmax}')

out[out < argmax] = 0
out[out >= argmax] = 255

# Save result
cv2.imwrite("my_answer_4.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
