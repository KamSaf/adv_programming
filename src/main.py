import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

FILES = ["image_1.png", "image_2.jpg", "image_3.jpg", "image_4.jpg", "image_5.png"]


def read_text(file_path: str) -> str:
    img = cv2.imread(file_path)
    conv_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    conv_img = cv2.medianBlur(img, 3)
    return pytesseract.image_to_string(conv_img)


if __name__ == "__main__":
    for file in FILES:
        print(f"### File: {file} ###\n")
        print(read_text("images/" + file))
    print("#########################")
