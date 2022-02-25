from AES import AES
from AES import unpad
from EncodeDecode import encode
from EncodeDecode import decode
from ImageInsideImage import *
from PIL import Image

if __name__ == '__main__':
    
    print("Enter 1 to Ecrypt a Message Using AES Encryption\nEnter 2 to Decrypt a Message\nEnter 3 to Encrypt a Message and Hide It In Image Using LSB\nEnter 4 to Decrypt a Image\nEnter 5 to Hide Image Inside Another Image\nEnter 6 to Reveal a Image Inside Another Image\nEnter To Hide Image Inside Another Image Without ")
    choice=int(input())
    if choice==1:
        text=input("Enter the text to be encrypted:\n")
        key=input("Enter 16 bytes long encryption key:\n")
        while(len(key)!=16):
            key=input("The length of the key needs to be 16, please enter 16 bytes long key\n")
        iv=input("Enter 16 bytes long initialization vector:\n")
        while(len(iv)!=16):
            iv=input("The length of the initialization vector needs to be 16, please enter 16 bytes long iv\n")
        obj=AES(key)
        cipher=obj.encrypt_cbc(text,iv )
        enctext=""
        for i in cipher:
            for j in i:
                enctext+=chr(j)
        print("Here is your encrypted message:",cipher)
        
    elif choice==2:
        print("A list needs to be passed as encrypted text ,so please modify the same in code")
        key=input("Enter 16 bytes long decryption key:\n")
        while(len(key)!=16):
            key=input("The length of the key needs to be 16, please enter 16 bytes long key\n")
        iv=input("Enter 16 bytes long initialization vector:\n")
        while(len(iv)!=16):
            iv=input("The length of the initialization vector needs to be 16, please enter 16 bytes long iv\n")
        obj=AES(key)
        cipher=[[82, 214, 73, 255, 189, 148, 31, 109, 36, 213, 241, 19, 240, 128, 113, 142], [248, 241, 148, 140, 143, 63, 222, 195, 202, 210, 244, 74, 102, 0, 190, 200], [29, 45, 179, 186, 183, 88, 115, 91, 115, 240, 60, 133, 170, 156, 139, 215]]
        msg=obj.decrypt_cbc(cipher, iv)
        msgstr=""
        for i in msg:
            for j in i:
                msgstr+=chr(j)
        print("Here is your decrypted message:",unpad(msgstr))
        
    elif choice==3:
        text=input("Enter the text to be encrypted:\n")
        key=input("Enter 16 bytes long encryption key:\n")
        while(len(key)!=16):
            key=input("The length of the key needs to be 16, please enter 16 bytes long key\n")
        iv=input("Enter 16 bytes long initialization vector:\n")
        while(len(iv)!=16):
            iv=input("The length of the initialization vector needs to be 16, please enter 16 bytes long iv\n")
        obj=AES(key)
        cipher=obj.encrypt_cbc(text,iv)
        enctext=""
        for i in cipher:
            for j in i:
                enctext+=chr(j)
        encode(enctext)
        
    elif choice==4:
        name=input("Enter the name of the image to be decrypted along with proper extension (.png):\n")
        rvale=decode(name)
        print("The information hidden in image is:  ",rvale)

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

        key=input("Enter 16 bytes long decryption key:\n")
        while(len(key)!=16):
            key=input("The length of the key needs to be 16, please enter 16 bytes long key\n")
        iv=input("Enter 16 bytes long initialization vector:\n")
        while(len(iv)!=16):
            iv=input("The length of the initialization vector needs to be 16, please enter 16 bytes long iv\n")
        obj=AES(key)
        msg=obj.decrypt_cbc(nlist, iv)
        msgstr=""
        for i in msg:
            for j in i:
                msgstr+=chr(j)
        print("Here is your decrypted message:",unpad(msgstr))

    elif choice==5:
        name1=input("Enter the name of the First image (Cover Image) along with proper extension (.jpg):\n")
        name2=input("Enter the name of the Second image (Cover Image) along with proper extension (.jpg):\n")

        output = 'output.png'
        merged_image = Steganography.merge(Image.open(name1), Image.open(name2))
        merged_image.save(output)

    elif choice==6:
        name=input("Enter the name of Cover Image along with proper extension (.png):\n")

        output = 'HiddenImage.png'
        unmerged_image = Steganography.unmerge(Image.open(name))
        unmerged_image.save(output)




        
        
         
        
        
    
       