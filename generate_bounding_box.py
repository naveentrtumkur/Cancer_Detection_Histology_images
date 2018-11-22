#### Learnt by watching the tutorial https://imgaug.readthedocs.io/en/latest/source/examples_bounding_boxes.html

### Given an image just apply bounding box on that image and display teh image.
## Possible thoughts, 
# 1.use different colors based on the prediction score
# 2. Try to augment or enlarge teh image region where bounding box is applied.
import sys

from PIL import Image, ImageDraw

def draw_bound(image_name):
    img = Image.open(image_name)
    width, height = img.size
    print("width = ", width, "height==", height)
    bound_vals = (0 + 200, 0 + 200, width - 200, height - 200)
    # bound_vals = (100, 1000, 1000, 2000)
    out_col = (0, 0, 255)
    rimg = img.copy()
    rimg_draw = ImageDraw.Draw(rimg)
    rimg_draw.rectangle(bound_vals, fill=None, outline=out_col, width=25)
    rimg.show()


if __name__=="__main__":
    image = Image.open("./Full_Size_Images/TUPAC-TE-319.svs_01_05.png")
    #image = Image.open("BuckId.jpg")
    width, height = image.size
    print("width = ",width, "height==",height)
    bound_vals = (0 +200, 0 +200, width -200, height-200)
    #bound_vals = (100, 1000, 1000, 2000)
    out_col = (0, 0, 255,255)
    draw_bound("./Full_Size_Images/TUPAC-TE-319.svs_01_05.png")
    #draw_bound("./Full_Size_Images/TUPAC-TE-319.svs_01_05.png", bound_vals, out_col)
'''
import numpy as np
import cv2 as cv
img = cv.imread('BuckId.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
im2,contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]
print(cnt)
#M = cv.moments(cnt)
#print( M )

x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
'''
'''
import numpy as np
import cv2 as cv

#Create an object for the image
img = cv.imread('BuckId.jpg')

color = (0,255,0)

label = 'Mitosis'

cv.rectangle(img, (100,1000),(1000,2000),color, 2)

cv.putText(img, label, (100 - 10, 1000 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

cv.imshow("object detection", img)

cv.waitKey()
'''