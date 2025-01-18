import hashlib
import os
import binascii

def secure_password(input):
    salt = hashlib.sha256(os.urandom(32)).hexdigest().encode("ascii")
    hash = hashlib.pbkdf2_hmac("sha256", input.encode("utf-8"), salt, 1000)
    hash = binascii.hexlify(hash)
    return salt + hash

def verify_password(password, input):
    password = password.decode("ascii")
    salt = password[:64]
    password = password[64:]
    hash = hashlib.pbkdf2_hmac("sha256", input.encode("utf-8"), salt.encode("ascii"), 1000)
    hash = binascii.hexlify(hash).decode("ascii")
    return hash == password
