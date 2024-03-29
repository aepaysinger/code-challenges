def delete_extra(alist, amount):
    updated = []
    count = {}
    for item in alist:
        count[item] = count.get(item, 0) + 1
        if count[item] <= amount:
            updated.append(item)

    return updated


if __name__ == "__main__":
    alist = [1, 2, 3, 1, 2, 1, 2, 3]
    amount = 2
    print(delete_extra(alist, amount))
