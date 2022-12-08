class Phone:
    def __init__(self, numbers):
        self.numbers = numbers
        self.translator = {
            "2": "a",
            "22": "b",
            "222": "c",
            "3": "d",
            "33": "e",
            "333": "f",
            "4": "g",
            "44": "h",
            "444": "i",
            "5": "j",
            "55": "k",
            "555": "l",
            "6": "m",
            "66": "n",
            "666": "o",
            "7": "p",
            "77": "q",
            "777": "r",
            "7777": "s",
            "8": "t",
            "88": "u",
            "888": "v",
            "9": "w",
            "99": "x",
            "999": "y",
            "9999": "z",
        }

    def translate_numbers(self):
        spot_holder = ""
        translation = ""
        for i, number in enumerate(self.numbers):
            if self.numbers[i] == "0":
                translation += " "
                continue
            if self.numbers[i] == "1":
                continue
            spot_holder += self.numbers[i]
            if i == len(self.numbers) - 1:
                translation += self.translator[spot_holder]
                break
            elif self.numbers[i] != self.numbers[i + 1]:
                translation += self.translator[spot_holder]
                spot_holder = ""
                continue
            elif self.numbers[i + 1] == self.numbers[i]:
                if len(spot_holder) == 3:
                    if spot_holder == "777" or spot_holder == "999":
                        continue
                    else:
                        translation += self.translator[spot_holder]
                        spot_holder = ""
                elif len(spot_holder) == 4:
                    translation += self.translator[spot_holder]
                    spot_holder = ""
                continue

        return translation


def phone_code(numbers):
    secret_code = Phone(numbers)

    return secret_code.translate_numbers()


if __name__ == "__main__":
    numbers = "339997772"
    print(phone_code(numbers))
