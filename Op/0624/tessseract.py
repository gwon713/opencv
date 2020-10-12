from PIL import Image
from pytesseract import *



filename = '../img/tesser.jpg'
image = Image.open(filename)
text = pytesseract.image_to_string(image, lang='kor')

print("================ OCR result ================")
print(text)

