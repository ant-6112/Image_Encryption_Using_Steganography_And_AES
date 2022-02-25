from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from base64 import b64decode, b64encode
import binascii

def padding(String):
    String = "{}".format(String)
    str = ""
    for i in range(len(String)):
        str += '{0:08b}'.format(ord(String[i]))
    bit8_rep = str + "1"
    n = len(bit8_rep)
    while len(bit8_rep) % 512 != 448:
        bit8_rep += "0" 
    bit8_rep += '{0:064b}'.format(n - 1)
    return bit8_rep


def sha1_operation(String):
    padding_bits = padding(String)

    def size_limitconst(array, max_size):
        return [array[i: i + max_size]
            for i in range(0, len(array), max_size)
        ]
    def left_shift(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
    H0, H1, H2, H3, H4 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0
    for element in size_limitconst(padding_bits, 512):
        word = size_limitconst(element, 32)
        w = [0] * 80
    for n in range(0, 16):
        w[n] = int(word[n], 2)
    for i in range(16, 80):
        w[i] = left_shift((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
    a, b, c, d, e = H0, H1, H2, H3, H4
    k1, k2, k3, k4 = 0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6


    for i in range(0, 80):
        if 0 <= i <= 19:
            func = (b & c) | ((~b) & d)
            key = k1
        elif 20 <= i <= 39:
            func = b ^ c ^ d
            key = k2
        elif 40 <= i <= 59:
            func = (b & c) | (b & d) | (c & d)
            key = k3
        elif 60 <= i <= 79:
            func = b ^ c ^ d
            key = k4

        res = (left_shift(a, 5) + func + e + key + w[i] & 0xffffffff)
        e, d, c, b, a = d, c, left_shift(b, 30), a, res

    H0 = (H0 + a) & 0xffffffff
    H1 = (H1 + b) & 0xffffffff
    H2 = (H2 + c) & 0xffffffff
    H3 = (H3 + d) & 0xffffffff
    H4 = (H4 + e) & 0xffffffff
    return '%08x%08x%08x%08x%08x' % (H0, H1, H2, H3, H4)

print("\nWELCOME TO THE STAR WARS MERCHANDISE STORE\n")
print("Enter details for verification\n")
key = RSA.generate(2048)
private_key = key.exportKey(passphrase = "1234")
filename = input("Enter filename to store private key: ")
file_out = open(filename, "wb")
file_out.write(private_key)
file_out.close()
public_key = key.publickey().exportKey()
filename2 = input("Enter filename to store public key: ")
file_out = open(filename2, "wb")
file_out.write(public_key)
file_out.close()


class OrderInformation():
    def init(self):
        self.item_List = []
    self.priceList = []
    self.totalPrice = 0
def calcPrice(self):
    totalPrice = 0
for price in self.priceList:
    totalPrice += price
self.totalPrice = totalPrice
def searchItem(self, item):
    for i in range(len(self.item_List)):
    if (self.item_List[i] == item):
        return i
return -1

def addItem(self, item, price):
    self.item_List.append(item)
print("One item added to the cart")
self.priceList.append(price)
self.calcPrice()
def removeItem(self, item):
    index = self.searchItem(item)
if (index != -1):
    del self.item_List[index]
print("Removed item:", item)
del self.priceList[index]
self.calcPrice()
else :
    print("Item not found")
def getTotal(self):
    return self.totalPrice
def display(self):
    print("\nCart Summary:")
print("Item\tPrice")
for i in range(len(self.item_List)):
    print(self.item_List[i] + "\t" + str(self.priceList[i]))
print("\nTotal amount:", self.totalPrice)
def generateOrderText(self):
    msg = "Order Summary\nItems: "
for item in self.item_List:
    msg += item + ", "
return msg[: len(msg) - 2]
class PaymentInformation():
    def init(self):
    self.cardNumber = ""
self.cvv = ""
self.expiry = ""
self.pay = 0
def setPay(self, amount):
    self.pay = amount
def card_details(self, cardNumber, expiry, cvv):
    self.cardNumber = cardNumber
self.expiry = expiry
self.cvv = cvv
def display(self):
    print("\nYour card details are as follows:")
print("Card-Number:", self.cardNumber)
19 BCE2347 Rajvi Jasani
6
print("Expiry date:", self.expiry)
print("CVV:", self.cvv)
print("\nTotal Amount:", self.pay)
def generatePayText(self):
    msg = "----Payment Information-------" + "Card Number:" + self.cardNumber + "-----Expiry 
Date: -- -- --" + \ 
self.expiry + "------CVV Number:-------" + self.cvv + \
    "-------Payment Amount:----" + str(self.pay)
return msg# ''
'Helper Functions'
''
def bin2hex(binStr):
    return binascii.hexlify(binStr)
def hex2bin(hexStr):
    return binascii.unhexlify(hexStr)
class Request_Message(): #''
'Initialize everything'
''
def init(self, PI, OI): #''
'Calculating hash of payment information'
''
self.PI = PI
self.PIMD = sha1_operation(self.PI)#
''
'Calculating hash of order information'
''
self.OI = OI
self.OIMD = sha1_operation(self.OI)#
''
'Calculate POMD and hashed POMD'
''
POMD = ""
POMD += self.PIMD + self.OIMD
self.POMD = POMD.encode()
self.HPOMD = sha1_operation(self.POMD)#
''
'Function to encrypt POMD using user'
s private key and generate DS ''
' 
def encrypt_the_POMD(self): #passphrase = "passphrase-used-by-user"
f = open('private_key', 'r')
keyPair = RSA.generate(bits = 1024)
user_Key = keyPair.publickey()
cipher_rsa = PKCS1_OAEP.new(user_Key)
data = self.POMD
self.ds = cipher_rsa.encrypt(data)
print("Computed Dual Signature:")
self.ds = bin2hex(self.ds).decode()
print(self.ds)#
''
'Function to create the digital envelope'
''
19 BCE2347 Rajvi Jasani
7
def digital_Envelope(self):
    file_out = open("public_key", "wb")#
''
'Generate random session key'
''
session_key = get_random_bytes(16)
cipher_aes = AES.new(session_key, AES.MODE_EAX)
data = self.PI + "\n"
data += "----Dual-Signature----\n" + self.ds + "\n"
data += "----OIMD----\n" + self.OIMD
data = data.encode()
print(data)
keyPair = RSA.generate(bits = 1024)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
f1 = open('public_key', 'r')
bankKey = keyPair.publickey()
cipher_rsa = PKCS1_OAEP.new(bankKey)
print("\n\nCiphertext in Digital Envelope:\n",
    bin2hex(ciphertext).decode())#
''
'Encrypt session key using bank'
s public key ''
' 
encrypted_session_key = cipher_rsa.encrypt(session_key)[file_out.write(x) for x in (encrypted_session_key,
    cipher_aes.nonce, tag, ciphertext)]
print("Digital envelope has been created and will be sent to the Merchant")#

def completeRequest(self):
    file_out = open("requestmessage.txt", "w")#

data = self.OI + "\n"
data += "-------Dual Signature------\n" + self.ds + "\n"
data += "----PIMD----\n" + self.PIMD[file_out.write(x) for x in (data)]
def verify_by_Bank():
    file_in = open("digitalenvelope.txt", "r")
keyPair = RSA.generate(bits = 1024)
private_key = keyPair.publickey()
enc_session_key, nonce, tag, ciphertext = [file_in.read(
    x) for x in (private_key.size_in_bytes(), 16, 16, -1)]#

cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)#

cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print("\n\nData recieved by bank:")
print(data.decode("utf-8"))
def verify_by_Merchant():
    print("\nCard details verified, waiting for merchant's confirmation\n")
file_in = open("requestmessage.txt", "r")
data = file_in.read()
print("Data recieved by merchant:")
print(data, "\n")
def main():
    items = ["Yoda", "Anakin", "Ahsoka", "Kenobi", "Ezra"]
prices = [210, 200, 170, 190, 90]
choice = -1
order = OrderInformation()
order.init()
payment = PaymentInformation()
while (choice != 4):
    choice = int(input(
            "\n1.Add item to the cart\n2.Remove item from the cart\n3.Display cart\n4.Proceed to 
            pay\ nChoose an operation: ")) 
            if (choice == 1):
                print("\nAvailable Items:")
            print("Id\tItem\t\tPrice") for i in range(len(items)):
            print(str(i + 1) + "\t" + items[i] + "\t\t" + str(prices[i])) ch2 = input("\nEnter item name to add: ") found = False
            for i in range(len(items)):
            if ch2 == items[i]:
            order.addItem(items[i], prices[i]) found = True
            if not found:
            print("No item with that name available") elif(choice == 2):
            order.display() ch2 = input("Enter item name to remove: ") order.removeItem(ch2) elif(choice == 3):
            order.display() elif(choice != 4):
            print("Invalid option! Try again") order.display() ch3 = "no"
            while (ch3 != "yes"):
                print("\nEnter your details")
            t = int(input(
                "1.American Express\n2.VISA\n3.MasterCard\n4.Rupay\nChoose payment gateway: ")) cardNo = input("Enter card number: ") expiry = input(
                "Enter expiry date in MM/YY format: ") cvv = input("Enter CVV: ") payment.card_details(cardNo, expiry, cvv) payment.setPay(order.getTotal()) payment
            .display() ch3 = input("Are your details correct?(yes/no): ")# print(ch3) 19 BCE2347 Rajvi Jasani 9 print(
                "\nGenerating dual signature for verification of the customer") order_message = order.generateOrderText() payment_message = payment.generatePayText() obj_req =
            Request_Message() obj_req.init(payment_message, order_message) obj_req.encrypt_the_POMD() obj_req.digital_Envelope() obj_req.completeRequest() print(
                "\nVerifying the data received by merchant") verify_by_Merchant() print(
                "\nVerification successful\nYour order has been placed\nThank you for shopping with 
                us!") 
                main()