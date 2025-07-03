import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from lib.core.enums import PRIORITY
__priority__ = PRIORITY.NORMAL
def dependencies():    
    pass
def tamper(payload, **kwargs):    
    return encrypt(payload)
def encrypt(s):    
    key = "ilovethi"
    iv = bytes([1, 2, 3, 4, 5, 6, 7, 8])
    cipher = DES.new(key.encode(), DES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(s.encode(), DES.block_size))
    var1 = base64.b64encode(encrypted_data).decode()
    var1 = var1.replace("%", "@2HJ5@")
    var1 = var1.replace("+", "@2HJB@")
    var1 = var1.replace(" ", "@2HJ0@")
    var1 = var1.replace("/", "@2HJF@")
    var1 = var1.replace("?", "@3HJF@")
    var1 = var1.replace("#", "@2HJ3@")
    var1 = var1.replace("&", "@2HJ6@")
    var1 = var1.replace("=", "@3HJD@")
    var1 = var1.replace("\r\n", "").replace("\n", "").replace("\r", "")
    var1 = var1.replace("@", "PAATTP")
    return var1