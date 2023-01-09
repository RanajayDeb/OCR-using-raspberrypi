import cv2
import pytesseract
img = cv2.imread("test2_thresh.png")
img = cv2.resize(img, (400, 450))
"""img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)"""
cv2.imshow("Image", img)
text = pytesseract.image_to_string(img)
print(text)
cv2.waitKey(0)
