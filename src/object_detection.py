import cv2
import numpy as np
import imutils
from src.config import ROOT_DIR


def process_image(file_name: str) -> int:
    file_path = f"{ROOT_DIR}/images/{file_name}"
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    image = cv2.imread(file_path)

    MAX_WIDTH = 1500
    if image.shape[0] > MAX_WIDTH:
        ratio = image.shape[0] / MAX_WIDTH
        image = imutils.resize(image, width=MAX_WIDTH, height=image.shape[1] * ratio)
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
            filtered_objects.append(regions[index])
    for object in filtered_objects:
        x, y, w, h = object
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite(file_path, image)
    return len(filtered_objects)


if __name__ == "__main__":
    pass
