import hashlib

SECRET_KEY = "asdsad9978&(("


def encode4md5(txt):
    md5_ = hashlib.md5(txt.encode('utf-8'))
    md5_.update(SECRET_KEY.encode('utf-8'))
    return md5_.hexdigest()