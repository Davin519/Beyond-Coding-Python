import cv2 as cv
from PIL import Image

ascii_chars = """&@WM%8D#b$0NqGXOEyVS2xCj}t?lv^i/r7<+!*~";_:,'-.`"""

def image_to_ascii(image):
    pixels = image.getdata()
    characters = []
    for pixel in pixels:
        characters.append(ascii_chars[pixel//int(255/len(ascii_chars) + 1)])
    characters = "".join(characters)

    pixel_count = len(characters)
    ascii_image = []
    for i in range(0, pixel_count, 200):
        ascii_image.append(characters[i:i+200])
    ascii_image = "\n".join(ascii_image)
    # with open("ascii_image.txt", "w") as f:
    #     f.write(ascii_image)



img = cv.imread("/Users/davin.park.29/Library/Mobile Documents/com~apple~CloudDocs/WEB/Python Class (2022-2022)/cat.jpg")

ratio = img.shape[0]/img.shape[1]

small_img = cv.resize(img, (200, int(ratio * 200)), interpolation=cv.INTER_AREA)

gray = cv.cvtColor(small_img, cv.COLOR_BGR2GRAY)

image_to_ascii(Image.fromarray(gray))



cv.waitKey(0)