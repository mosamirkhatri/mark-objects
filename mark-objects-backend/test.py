import cv2
import xml.etree.ElementTree as ET
from datetime import datetime

img = cv2.imread('bag.jpg', -1)
font = cv2.FONT_HERSHEY_SIMPLEX
result_img = img

tree = ET.parse('bag.xml')
root = tree.getroot()
filename = root.find('filename').text
print(filename)
timestamp = datetime.timestamp(datetime.now())
print(int(timestamp))

for child in root.findall('./object'):
    name = child.find('name').text
    bndbox = child.find('bndbox')
    xmin = int(bndbox.find('xmin').text)
    ymin = int(bndbox.find('ymin').text)
    xmax = int(bndbox.find('xmax').text)
    ymax = int(bndbox.find('ymax').text)
    result_img = cv2.rectangle(
        result_img, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
    cv2.putText(img, name, (xmin, ymin-5), font,
                1, (0, 0, 255), 2, cv2.LINE_AA)


cv2.imshow('Image', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# for type_tag in root.findall('object/name'):
#     value = type_tag.get('name')
#     print(value)
