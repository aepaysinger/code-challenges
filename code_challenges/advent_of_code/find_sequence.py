def get_ip_addresses():
    with open("./code_challenges/advent_of_code/ip_addresses_input") as input:
        ip_addresses = input.read().split("\n")

    return ip_addresses


def abba_in_middle():
    ip_adresses = get_ip_addresses()
    abba_in_middle = set()
    go = False
    for address in ip_adresses:
        for i, character in enumerate(address):
            if character == "[":
                go = True
            if character == "]":
                go = False
            if go:
                if (
                    address[i] == address[i + 3]
                    and address[i + 1] == address[i + 2]
                    and address[i] != address[i + 1]
                ):
                    abba_in_middle.add(address)
    for address in abba_in_middle:
        if address in ip_adresses:
            ip_adresses.remove(address)

    return ip_adresses


def abba_on_outside():
    ip_adresses = abba_in_middle()
    correct_ip_address = set()
    go = True
    for address in ip_adresses:
        for i in range(len(address) - 3):
            if address[i] == "[":
                go = False
            if address[i] == "]":
                go = True
            if go:
                if (
                    address[i] == address[i + 3]
                    and address[i + 1] == address[i + 2]
                    and address[i] != address[i + 1]
                ):
                    correct_ip_address.add(address)
    return len(correct_ip_address)


def find_aba():
    ip_addresses = get_ip_addresses()
    good_ip = set()
    go = True
    for address in ip_addresses:
        aba_out = set()
        aba_in = set()
        for i in range(len(address) - 2):
            if address[i] == "[":
                go = False
            if address[i] == "]":
                go = True

            if (
                address[i] == address[i + 2]
                and address[i + 1] != "["
                and address[i + 1] != "]"
            ):
                if go:
                    aba_out.add(address[i : i + 3])
                else:
                    aba_in.add(address[i : i + 3])
        if aba_out and aba_in:
            for section in aba_out:
                for i in range(1):
                    if (section[i + 1] + section[i] + section[i + 1]) in aba_in:
                        good_ip.add(address)
    return len(good_ip)
