import hashlib

def mining_adventcoins():
    secret_key = "abcdef"
    # final_code = ""

    number = up_the_number()
    code = secret_key + str(number)
    code_bytes = bytes(code, 'utf-8')
    m = hashlib.md5()
    m.update(code_bytes)
    m.digest()
    final_code = m.hexdigest()

    print(number)    
    print(final_code)
def up_the_number():
    number = 609041

print(mining_adventcoins())
# arr = bytes(string, 'utf-8')
# arr2 = bytes(string, 'ascii')

# print(arr,'\n')