
import os
import sys
import hashlib


def check(folder):
    txt=""
    for f in os.listdir(folder):  
        if f.endswith(".txt") and f.startswith("out"):
            txt=txt+open(folder+"/"+f,"r").read()
    m.update(txt)
    
m = hashlib.md5()

print("\""+check(sys.argv[1])+"\",")

return m.hexdigest()
