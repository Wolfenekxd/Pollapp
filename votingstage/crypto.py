import base64, re
from Crypto.Cipher import AES
from Crypto import Random
from django.conf import settings
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

class AESCipher:
    
    def __init__(self, key, blk_sz):
        self.key = key
        self.blk_sz = blk_sz

    def encrypt( self, raw ):
        if raw is None or len(raw) == 0:
            raise NameError("No value given to encrypt")
        raw = raw + '\0' * (self.blk_sz - len(raw) % self.blk_sz)
        raw = raw.encode('utf-8')
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key.encode('utf-8'), AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ).decode('utf-8')

    def decrypt( self, enc ):
        if enc is None or len(enc) == 0:
            raise NameError("No value given to decrypt")
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_CBC, iv )
        return re.sub(b'\x00*$', b'', cipher.decrypt( enc[16:])).decode('utf-8')

key = "dsfkfasjkdbadwww"
aes = AESCipher( key, 32)
msg = 'xd'
encryp_msg = aes.encrypt( msg )
print(encryp_msg)
msg = aes.decrypt( encryp_msg )
print(msg)
    