def contains_duplicate(numbers):
    if len(numbers) > len(set(numbers)):
        return True
    return False


if __name__ == "__main__":
    numbers = [1]
    print(contains_duplicate(numbers))
