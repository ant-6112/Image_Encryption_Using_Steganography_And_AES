from AES import AES
from AES import unpad
from EncodeDecode import encode
from EncodeDecode import decode
from ImageInsideImage import *
from PIL import Image

def HideImage(name1,name2):
        name1=name1
        name2=name2

        output = 'output.png'
        merged_image = Steganography.merge(Image.open(name1), Image.open(name2))
        merged_image.save(output)
        return output

def RevealImage(name):
        name=name

        output = 'HiddenImage.png'
        unmerged_image = Steganography.unmerge(Image.open(name))
        unmerged_image.save(output)

        return output

def DecryptImage(name,key,iv):
        rvale=decode(name)
        ciphervec = [];

        for k in rvale:
            ciphervec.append(ord(k))

        nlist=[]
        tlist=[]
        count=0
        for i in ciphervec:
            tlist.append(i)
            if (count+1)%16==0:
                nlist.append(list(tlist))
                tlist.clear()
            count+=1
        
        obj=AES(key)
        msg=obj.decrypt_cbc(nlist, iv)
        msgstr=""
        for i in msg:
            for j in i:
                msgstr+=chr(j)
        return unpad(msgstr)

def EncryptImage(imgname,text,key,iv):
        enctext = text
        key = key
        iv = iv 
        obj=AES(key)
        cipher=obj.encrypt_cbc(text,iv)
        enctext=""
        for i in cipher:
            for j in i:
                enctext+=chr(j)
        encode(enctext,imgname)






        
        
         
        
        
    
       