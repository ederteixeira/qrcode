import pyqrcode

url = pyqrcode.create('https://www.linkedin.com/in/teixeiraeder/')
url.svg('linkedin.svg', scale=6)
url.png('LInkedin.png', scale=6)
