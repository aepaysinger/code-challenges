def get_triangle_sides():
    with open("code_challenges/advent_of_code/triangle_input") as triangle_input:
        triangel_sides = triangle_input.read().split("\n")
    return triangel_sides


def clean_up_triangle_sides():
    triangle_sides = get_triangle_sides()
    triangle_sides = [sides.strip() for sides in triangle_sides]
    triangle_sides = [sides.split() for sides in triangle_sides]
    
    for sides in triangle_sides:
        sides[0] = int(sides[0])
        sides[1] = int(sides[1])
        sides[2] = int(sides[2])

    return triangle_sides

def find_triangle():
    triangle_sides = clean_up_triangle_sides()
    number_of_triangles = 0
    
    for sides in triangle_sides:
        if (sides[0] + sides[1]) > sides[2] and (sides[0] + sides[2]) > sides[1] and (sides[1] + sides[2]) > sides[0]:
            number_of_triangles += 1
    return number_of_triangles 
        


# print(get_triangle_sides())
# print(clean_up_triangle_sides())
print(find_triangle())
#986 too high