def draw_door_mat(size):
    height = int(size[0])
    length = int(size[1])
    starter = int((length - 1)/2) #5
    greeting = "WELCOME"
    print(starter)
    detail = ".|."
    for _ in range(int(height/2)):
        draw =  "-".rjust((starter - 1),"-") + detail + "-".ljust((starter -1), "-")
        starter -= 3
        detail += ".|..|."

        print(draw)
    print(greeting.center(((height * 2) + len("WELCOME")),"-"))
    starter = int(length-1)
    detail = ".|."
    for _ in range(int(height/2)):
        draw =  "-".rjust((starter - 1),"-") + detail + "-".ljust((starter - 1), "-")
        starter -= 3
        detail += ".|..|."
        print(draw)





if __name__ == '__main__':
    size = ['7', '21']
    draw_door_mat(size)

#     >>> width = 20
# >>> print 'HackerRank'.ljust(width,'-')
# HackerRank---------- 

    # ---------.|.---------
    # ------.|..|..|.------
    # ---.|..|..|..|..|.---
    # -------WELCOME-------
    # ---.|..|..|..|..|.---
    # ------.|..|..|.------
    # ---------.|.---------