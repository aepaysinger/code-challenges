from typing import List, Tuple

def locate_entrance(office: List[str]) -> Tuple[int, int]:
    #top
    for i, character in enumerate(office[0]):
        if character == ".":
            return (i, 0)
        
    #left
    
    for i in range(len(office)):
        x = 0
        while office[i][x] == " ":
            x += 1

        if office[i][x] == ".":
            return (i, x)
    #right
    for i in range(len(office)):
        
    #bottom
    return 0, 0




if __name__ == "__main__":
    office = ['###.###',
          '#.....#',
          '#.....#',
          '#.....#',
          '#######']
    print(locate_entrance(office))
' #####',
' #...#',
' ....#',
' #...#',
'##...#',
'#....#',
'######']