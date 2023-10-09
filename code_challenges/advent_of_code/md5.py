import hashlib


def crack_the_code_lowest(secret_key, amount_of_zeroes):
    count = 1
    result = ""
    while True:
        result = hashlib.md5((secret_key + str(count)).encode())
        if result.hexdigest()[0:amount_of_zeroes] == "0" * amount_of_zeroes:
            return count
        count += 1
