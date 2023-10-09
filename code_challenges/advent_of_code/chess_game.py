import hashlib


def find_pass_code(code):
    used_hashes = []
    number = 0
    password = ""
    while len(used_hashes) < 8:
        test_hash = hashlib.md5(code + str(number).encode("utf-8")).hexdigest()
        if test_hash.startswith("00000"):
            used_hashes.append(test_hash)
            password += test_hash[5]
        number += 1

    return password


def find_second_pass_code(code):
    password = ["-" for _ in range(8)]
    number = 0
    while "-" in password:
        test_hash = hashlib.md5(code + str(number).encode("utf-8")).hexdigest()
        if test_hash.startswith("00000") and test_hash[5].isdigit():
            spot = int(test_hash[5])
            if spot <= 7 and password[spot] == "-":
                password[spot] = test_hash[6]
        number += 1

    return "".join(password)
