from barcode import EAN13
from barcode.writer import ImageWriter

with open(r'barcode1.png', 'wb') as f:
    EAN13('123456789105452', writer=ImageWriter()).write(f)