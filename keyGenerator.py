
from bit import PrivateKey

def generate_address_fromInt(keyInt):
    try:
        key = PrivateKey.from_int(keyInt)
        print("\n Private Key: " + key.to_wif())
        print("\n Public Address: " + key.address)
        print("\n Your wallet is ready!")
    except:
        print("\n not working")
    
def generate_address_fromString(keyString):
    try:
        keyBytes  = keyString.encode('utf-8')
        key = PrivateKey.from_bytes(keyBytes)
        print("\n Private Key: " + key.to_wif())
        print("\n Public Address: " + key.address)
        print("\n Your wallet is ready!")
    except:
        print("\n Invalid string")  
        
if __name__ =="__main__":
    user_input = input("\n Options: \n \n   [1]: generate key pair from integer \n   [2]: generate key pair from string \n   [0]: exit \n \n Type something>")
    if user_input == "0":
        exit()
    elif user_input == "1":
        keyNumber = int(input("\n Enter Private Key integer>"))
        try:
            generate_address_fromInt(keyNumber)          
        except:
            print("\n incorrect key format")
            input("Press Enter to exit")
    elif user_input == "2":
        keyString = input("\n Enter Private Key string>")
        try:
            generate_address_fromString(keyString)           
        except:
            print("\n incorrect key format")
            input("Press Enter to exit")   
        