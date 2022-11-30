import cv2
img = cv2.imread("1.jpg")

grey_filter = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("result1.png", img)

invert = cv2.bitwise_not(grey_filter)
cv2.imwrite("result2.png", grey_filter )

blur = cv2.GaussianBlur(invert, (21,21),0)
cv2.imwrite("result3.png", invert)

invertedblur = cv2.bitwise_not(blur)
cv2.imwrite("result4.png", blur)

sketch_filter = cv2.divide(grey_filter, invertedblur, scale = 256.0)

cv2.imwrite("result.png", sketch_filter)