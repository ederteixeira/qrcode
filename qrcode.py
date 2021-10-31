import pyqrcode

url = pyqrcode.create('https://github.com/ederteixeirahttps://github.com/ederteixeira')
url.svg('github.svg', scale=6)
url.png('github.png', scale=6)
