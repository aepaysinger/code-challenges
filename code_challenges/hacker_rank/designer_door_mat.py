def draw_door_mat(size):
    height = int(size[0])
    length = int(size[1])
    starter = int((length - 1)/2) #5
    greeting = "WELCOME"

    detail_a = ".|."
    detail_b = "-"
    result = []

    for n in range((int(height/2))):
        result.append(detail * n)















    # print(starter)
    # detail = ".|."
    # for _ in range(int(height/2)):
    #     draw =  "-".rjust((starter - 1),"-") + detail + "-".ljust((starter -1), "-")
    #     starter -= 3
    #     detail += ".|..|."

    #     print(draw)
    # print(greeting.center(((height * 2) + len("WELCOME")),"-"))
    # starter = int(length/7)
    # print(starter)
    # detail = ".|." * int((length//2)/2)
    # count = 2
    # for _ in range(int(height/2)):
    #     draw =  "-".rjust((starter - 1),"-") + detail + "-".ljust((starter), "-")
    #     starter += 3
    #     detail = ".|." * (int((length/2)/2) - count)
    #     count += 2
            
            
    #     print(draw)







if __name__ == '__main__':
    size = ['7', '21']
    draw_door_mat(size)
# 7 21
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