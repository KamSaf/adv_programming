import argparse
import cv2
import numpy as np
import imutils

parser = argparse.ArgumentParser()
parser.add_argument("--id")
args = parser.parse_args()

print("hello " + args.id)


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


image = cv2.imread("image4.jpg")

if image.shape[0] > 1500:
    new_width = 1500
    ratio = image.shape[0] / 1500
    image = imutils.resize(image, width=1500, height=image.shape[1] * ratio)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


regions, weights = hog.detectMultiScale(
    gray, winStride=(2, 2), padding=(5, 5), scale=1.02
)

mean = np.mean(weights)
std = np.std(weights)
k = 0.86
filtered_objects = []
for index, weight in enumerate(weights):
    if weight >= (mean - k * std):
        print(weight)
        filtered_objects.append(regions[index])

for object in filtered_objects:
    x, y, w, h = object
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
