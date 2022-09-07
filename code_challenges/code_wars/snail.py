def snail(trail):
    # path_a = #trail[the list you want]
    # path_b = #last item in all lists
    # #for path in trail:
    #     #path[-1]
    # path_c = #from right to left bottom list
    # #trail[the list you want][::-1]
    # path_d = #from bottom to top first item in lists
    #     #for path in trail:
    #         #trail[-1][0]
    final_path = []
    # while trail:
    final_path.append(trail[0])
    trail.remove(trail[0])
        # for path in trail:
        #     final_path.append(path[-1])    
        #     del path[-1]
        # final_path.append(trail[-1][::-1])
        # trail.remove(trail[-1])
        # for path in reversed(trail):
        #     final_path.append(path[0])
        #     del path[0]

        

    return  final_path, trail
    
       
       
       


    
    



if __name__ == "__main__":
    trail = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    print(snail(trail))