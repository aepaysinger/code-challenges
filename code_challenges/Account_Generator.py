import random


def account_generator():
    student_names = []
    student_id_numbers = []
    student_email_addresses = []
    email_name = []

    for i in range(int(input("enter how many students you have: "))):
        student_names.append(input("Enter student name: "))

    for name in student_names:
        student_id_number = random.randint(111111, 999999)
        student_id_numbers.append(student_id_number)
        while student_id_number in student_id_numbers:
            student_id_number = random.randint(111111, 999999)
        student_name = name.split(" ")
        if len(student_name) > 2:
            email_name.append(student_name[0][0] + student_name[1][0] + student_name[2])
        else:
            email_name.append(student_name[0][0] + student_name[1])

    for i in range(len(student_names)):
        new_id = student_id_numbers[i]
        new_id = str(new_id)[3:]
        student_email_addresses.append(f"{email_name[i]}{new_id}@example.com")

    for i in range(len(student_names)):
        return f"name: {student_names[i]}\nid: {student_id_numbers[i]}\nemail: {student_email_addresses[i]}\n"


print(account_generator())

# def account_generator():
#     student_names = ["Charlotte Selva", "Mary Jane Drobka", "Ely Paysinger", "Brian Baranski", "Andrew Calvo"]
#     student_id_numbers = []
#     student_email_addresses = []
#     email_name = []

#     for name in student_names:
#         student_id_numbers.append(random.randint(111111, 999999))
#         student_name = name.split(" ")
#         if len(student_name) > 2:
#             email_name.append(student_name[0][0]+student_name[1][0]+student_name[2])
#         else:
#             email_name.append(student_name[0][0]+student_name[1])


#     for i in range(len(student_names)):
#         new_id = student_id_numbers[i]
#         new_id = str(new_id)[3:]
#         student_email_addresses.append(f"{email_name[i]}{new_id}@example.com")

#     for i in range(len(student_names)):
#         print(f"name: {student_names[i]}\nid: {student_id_numbers[i]}\nemail: {student_email_addresses[i]}")


# account_generator()
# Write a loop for requirement 2 that prompts the user for 5 names rather than hard coding the data.
