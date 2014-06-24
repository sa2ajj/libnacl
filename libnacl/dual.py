'''
The dual key system allows for the creation of keypairs that contain both
cryptographic and signing keys
'''
# import libnacl libs
import libnacl
import libnacl.utils
import libnacl.public
import libnacl.sign


class DualSecret(libnacl.utils.BaseKey):
    '''
    Manage crypt and sign keys in one object
    '''
    def __init__(self, crypt=None, sign=None):
        self.crypt = libnacl.public.SecretKey(crypt)
        self.signer = libnacl.sign.Signer(sign)
        self.sk = self.crypt.sk
        self.seed = self.signer.seed

    def sign(self, msg):
        '''
        Sign the given message
        '''
        return self.signer.sign(msg)

    def signature(self, msg):
        '''
        Return just the signature for the message
        '''
        return self.signer.signature(msg)
