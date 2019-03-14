import cv2

img = cv2.imread('../imori.jpg')
img2 = img.copy()
img2 = img2[:, :, (2, 1, 0)] # RとBを入れ替え

cv2.imwrite('my_answer_1.jpg', img2)
cv2.imshow('RGB -> BGR', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()