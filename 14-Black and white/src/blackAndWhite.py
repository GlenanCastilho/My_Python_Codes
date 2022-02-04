from PIL import Image

img = Image.open('bill.jpg');
blackAndWhite = img.convert("L")
blackAndWhite.save("bw_bill.jpg")
blackAndWhite.show()
