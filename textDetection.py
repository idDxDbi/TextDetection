import cv2
import numpy
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('2.jpeg')
# 由于tessercat只接受RGB值，再OpenCV中，我们要将图片的颜色转换成RGB值再传入到tessercat当中
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))

# # Detecting Characters 检测字母
hImg, wImg, r= img.shape
# print(hImg)
boxs = pytesseract.image_to_boxes(img)
# print(boxs.splitlines())
for b in boxs.splitlines():

    b = b.split(" ")
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
    cv2.putText(img,b[0],(x,hImg-y+12),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.75,(50,50,255),1)

# # Detecting Words 识别单词
# hImg,wImg,r = img.shape
# boxs = pytesseract.image_to_data(img)
# print(boxs)
# for x,b in enumerate(boxs.splitlines()):
#     # print(x)
#     # print(b)
#     if x != 0:
#         b = b.split()
#         print(b)
#         if len(b) == 12:
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.75,(50,50,255),1)

# # Detecting Words 识别数字
# hImg,wImg,r = img.shape
# cong = r'--oem 3 --psm 6 outputbase digits'
# boxs = pytesseract.image_to_data(img,config=cong)
# print(boxs)
# for x,b in enumerate(boxs.splitlines()):
#     # print(x)
#     # print(b)
#     if x != 0:
#         b = b.split()
#         print(b)
#         if len(b) == 12:
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.75,(50,50,255),1)

cv2.imshow("Result", img)
cv2.waitKey(0)
