from PIL import Image as p
import cv2


# highly recommended parameter to add that is encoding beoz in windows and linux it is different 


# xlsx = open('Data.xlsx', encoding='UTF-8')

# xlsx.close()
# we could get error while performing operations then file won't close
# for that reason use try... finally block

# try:
#     text = open('wifi.txt', encoding='UTF-8')

# finally:
#     text.close()


# Or we could use with statements for opeartion
# we do not need any close method ;it does internally

# image = p.open('image1.jpeg')
# image.show()


# image = cv2.imread('image1.jpeg')
# # cv2.imshow('Image',image)
# cv2.imwrite( 'demo.jpeg', image )
# cv2.waitKey()


