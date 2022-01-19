import pyqrcode
import png
from pyqrcode import QRCode

QRString = 'https://github.com/GlenanCastilho'

url = pyqrcode.create(QRString)

url.png(r'qr.png', scale=8)