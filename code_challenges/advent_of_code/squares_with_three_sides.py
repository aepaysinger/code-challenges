def get_triangle_sides():
    with open("code_challenges/advent_of_code/triangle_input") as triangle_input:
        triangel_sides = triangle_input.read().split("\n")
    return triangel_sides


def clean_up_triangle_sides():
    triangle_sides = get_triangle_sides()
    triangle_sides = [angles.strip() for angles in triangle_sides]
    triangle_sides = [angles.split() for angles in triangle_sides]
    
    for angles in triangle_sides:
        angles[0] = int(angles[0])
        angles[1] = int(angles[1])
        angles[2] = int(angles[2])

    return triangle_sides

def find_triangle():
    triangle_sides = clean_up_triangle_sides()
    number_of_trianles = 0
    
    for angles in triangle_sides:
        if (angles[0] + angles[1]) > angles[2] and (angles[0] + angles[2]) > angles[1] and (angles[1] + angles[2]) > angles[0]:
            number_of_trianles += 1
    return number_of_trianles 
        


# print(get_triangle_sides())
# print(clean_up_triangle_sides())
print(find_triangle())
#986 too high