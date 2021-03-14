import time
import rsa

data = "rangoisbackagainr"
for i in range(9,10):
    keysize = 2**i
    st = time.time()
    print("Key Size: ",keysize)
    pub,priv = rsa.newkeys(keysize)
    
    et = time.time()
    print("Time taken : ",et-st,"Seconds")
    
    #print(type(priv))
    #print(len(priv))
    pa = rsa.key.PublicKey(priv.n,priv.e)
    k = str(priv)[11:-1]
    #print(k)
    p = k.rstrip().split(",")
    print("Comp : ",len(p))
    #print(p)
    
    enc = rsa.encrypt(data.encode('utf-16'),pa)
    #print(enc)
    print(rsa.decrypt(enc,rsa.key.PrivateKey(int(p[0]),int(p[1]),int(p[2]),int(p[3]),int(p[4]))).decode('utf-16'))

