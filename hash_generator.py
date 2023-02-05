import hashlib

password = "1q2w3e4r5t"
hash = hashlib.sha256(password.encode('utf-8'))
print(hash.hexdigest())