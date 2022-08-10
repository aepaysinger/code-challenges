def set_mutations(instructions, number_of_instructions):
    instruction_list = []
    sets = []

    for i, items in enumerate(instructions):
        if i % 2 == 0:
            instruction_list.append(''.join([i for i in items if not i.isdigit()]))
        else:
            sets.append(items)

    


    print(instruction_list, sets)


             
  




if __name__ == "__main__":
    number_of_instructions = 4
    starting_point = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '24', '52']
    instructions = ['intersection_update 10', '2 3 5 6 8 9 1 4 7 11', 'update 2', '55 66', 'symmetric_difference_update 5', '22 7 35 62 58', 'difference_update 7', '11 22 35 55 58 62 66']
    set_mutations(instructions, number_of_instructions, starting_point)
    