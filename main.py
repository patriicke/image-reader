from pytesseract import pytesseract
from PIL import Image

path_to_image = "water-meter-reading.jpg"
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)
print(text)