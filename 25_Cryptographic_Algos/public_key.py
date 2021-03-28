import time
import rsa
import json
import sys

def loadKey(fileName):
    pub,priv = rsa.newkeys(512)
    with open(fileName,"r") as fp:
        conf = json.load(fp)
    priv.n = conf["n"]
    priv.e = conf["e"]
    priv.d = conf["d"]
    priv.p = conf["p"]
    priv.q = conf["q"]
    pub.n = priv.n
    pub.e = priv.e
    return pub,priv

if __name__=="__main__":
    Public, Private = loadKey(sys.argv[1])
    bufferLen = 248
    if sys.argv[2] =="e":
        try:
            while(True):
                try:
                    data = input()
                    if len(data) > bufferLen:
                        encrypted = b""
                        i = bufferLen
                        while i < len(data):
                            encrypted = encrypted+rsa.encrypt(data[i-bufferLen:i].encode('utf-16'),Public)
                            i += bufferLen
                            if i>=len(data):
                                break
                        encrypted = rsa.encrypt(data[i:].encode('utf-16'),Public)
                    else:
                        encrypted = rsa.encrypt(data.encode('utf-16'),Public)
                    #print(encrypted)
                    print(encrypted.hex())
                except EOFError:
                    pass
        except KeyboardInterrupt:
            pass
    elif sys.argv[2] == "d":
        try:
            while(True):
                try:
                    data = bytes.fromhex(input())
                    #print(data)
                    print(rsa.decrypt(data,Private).decode('utf-16'))
                except EOFError:
                    pass
        except KeyboardInterrupt:
            pass
    else:
        print(0)
    #print(rsa.decrypt(enc,priv).decode('utf-16'))