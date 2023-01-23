import hashlib


class MiningAdventCoins:
    def __init__(self, code):
        self.code = code
        self.number = 0
        self.final_code = ""

    def mining_adventcoins(self):

        while self.final_code[:6] != "00000":
            code_number = self.up_the_number()
            code_to_check = self.code + str(code_number)
            code_bytes = bytes(code_to_check, 'utf-8')
            m = hashlib.md5()
            m.update(code_bytes)
            m.digest()
            self.final_code = m.hexdigest()
        
        return self.final_code, self.number
            

    def up_the_number(self):
        self.number += 1
        return self.number 

mine_coins = MiningAdventCoins("abcdef")
print(mine_coins.mining_adventcoins())
# arr = bytes(string, 'utf-8')
# arr2 = bytes(string, 'ascii')

# print(arr,'\n')