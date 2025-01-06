import pytesseract
import cv2
from sys import platform


pytesseract.pytesseract.tesseract_cmd = (
    r"/usr/local/bin/tesseract" if platform == "darwin" else r"/usr/bin/tesseract"
)


FILES = ["image_1.png", "image_2.jpg", "image_3.jpg", "image_4.jpg", "image_5.png"]


def read_text(file_path: str) -> str:
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(
        cv2.medianBlur(img, 29),
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2,
    )
    img = cv2.threshold(
        cv2.GaussianBlur(img, (5, 5), 0), 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]
    img = cv2.adaptiveThreshold(
        cv2.bilateralFilter(img, 20, 75, 75),
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2,
    )
    return pytesseract.image_to_string(img)


# def show_image(file_path: str) -> None:
#     img = cv2.imread(file_path)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # img = cv2.medianBlur(img, 3)
#     # img = cv2.threshold(
#     #     cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
#     # )[1]
#     # img = cv2.threshold(
#     #     cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
#     # )[1]
#     # img = cv2.threshold(
#     #     cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
#     # )[1]

#     # img = cv2.adaptiveThreshold(
#     #     cv2.GaussianBlur(img, (5, 5), 0),
#     #     255,
#     #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     #     cv2.THRESH_BINARY,
#     #     31,
#     #     2,
#     # )
#     # img = cv2.adaptiveThreshold(
#     #     cv2.bilateralFilter(img, 9, 75, 75),
#     #     255,
#     #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     #     cv2.THRESH_BINARY,
#     #     31,
#     #     2,
#     # )
#     # img = cv2.adaptiveThreshold(
#     #     cv2.medianBlur(img, 3),
#     #     255,
#     #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     #     cv2.THRESH_BINARY,
#     #     31,
#     #     2,
#     # )
#     img = cv2.threshold(
#         cv2.GaussianBlur(img, (5, 5), 0), 5, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
#     )[1]
#     # img = cv2.adaptiveThreshold(
#     #     cv2.bilateralFilter(img, 20, 75, 75),
#     #     255,
#     #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     #     cv2.THRESH_BINARY,
#     #     31,
#     #     2,
#     # )
#     cv2.imshow("image", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


def show_image(file_path: str) -> None:
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # converted_img = cv2.medianBlur(img, 1)

    converted_img = cv2.threshold(
        cv2.GaussianBlur(img, (5, 5), 0), 5000, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    converted_img = cv2.threshold(
        cv2.bilateralFilter(converted_img, 5, 75, 75),
        5000,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )[1]

    converted_img = cv2.threshold(
        cv2.medianBlur(converted_img, 3), 1000, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    converted_img = cv2.adaptiveThreshold(
        cv2.GaussianBlur(converted_img, (5, 5), 0),
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        25,
    )

    converted_img = cv2.adaptiveThreshold(
        cv2.bilateralFilter(converted_img, 9, 75, 75),
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        20,
    )

    # converted_img = cv2.adaptiveThreshold(
    #     cv2.medianBlur(img, 3),
    #     255,
    #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #     cv2.THRESH_BINARY,
    #     31,
    #     2,
    # )
    cv2.imshow("image", converted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    for file in FILES:
        print(f"### File: {file} ###\n")
        print(read_text("images/" + file))
    print("#########################")
    print(read_text("images/screenshot_1.png"))
    # show_image("images/screenshot_1.png")
