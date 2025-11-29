from PIL import Image
print("PILLOW")
img=Image.open("img12.jpg.png")
print(img.show())
print(img.format)
print(img.size)
print(img.mode)
#resized_img=img.resize((400,400))
#print(resized_img)
#img.thumbnail((400,400))    #to maintain aspect ratio
#img.show()
gray_img=img.convert("1")
gray_img.show()
"""1"mode=1-bit per pixel used for true black and white image"""
"""L"mode=8-bit grayscale each pixel represents a shade of grey(0=black,255=white)"""
"""RGB"mode=8-bit*3 channels--red,green,blue and standard mode for colour images"""
"""RGBA"mode=8-bit*4 channels--rgb, alpha and similar to rgb but includes alpha(transperancy) channel"""
"""CMYK"mode=8-bit*4 channels--cyan,magenta,yellow,black and commanly used for printing and publishing"""
#rotated_img=img.rotate(180)
#rotated_img.show()
cropped_img=img.crop((400,0,1000,100))
cropped_img.show()
