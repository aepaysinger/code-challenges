def one_two_three(n):
    if n == 0:
        return [0,0]
    n = str(n)
    first_number = ""
    second_number = ""
   
    if int(n) <= 9:
        first_number = n
    elif int(n) < 99:
        part1 = int(n[0])
        first_number = "9" * part1
        part2 = int(n)[0]+int(n)[1]
        first_number += "9" 
        print(first_number)
        # for i, number in enumerate(n):
        #     first_number += number*(i+1)
    for _ in range(int(n)):
        second_number += "1"

    
    # both_numbers = [int(first_number), int(second_number)]
    # return both_numbers


if __name__ == "__main__":
    n = 19
    print(one_two_three(n))

    # 19 = 199