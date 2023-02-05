import hashlib

password = "0p9o8i7u"
hash = hashlib.sha256(password.encode('utf-8'))
print(hash.hexdigest())