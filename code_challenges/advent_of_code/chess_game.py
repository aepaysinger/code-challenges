import hashlib


def find_pass_code(code):
    used_hashes = []
    number = 0
    while len(used_hashes) < 8:
        test_hash = hashlib.md5(code + str(number).encode('utf-8')).hexdigest()
        if test_hash.startswith("00000"):
            print("{}: {}".format(code + str(number).encode('utf-8'), test_hash))
            used_hashes.append(number)
        number += 1
    return used_hashes
    





if __name__ == "__main__":
    code = "abc".encode('utf-8')
    print(find_pass_code(code))