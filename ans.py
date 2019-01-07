
import os
import sys
import hashlib


def check(folder):
    m = hashlib.md5()
    txt=""
    for f in os.listdir(folder):  
        if f.endswith(".txt") and f.startswith("out"):
            txt=txt+open(folder+"/"+f,"r").read()
    m.update(txt)
    return m.hexdigest()


print("\""+check(sys.argv[1])+"\",")
