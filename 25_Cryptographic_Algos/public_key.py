import rsa

data = "rango_isbackagain"

pub,priv = rsa.newkeys(2048)
print(pub)

print(priv)

enc = rsa.encrypt(data.encode('utf-16'),pub)
print(enc)
print(rsa.decrypt(enc,priv).decode('utf-16'))

