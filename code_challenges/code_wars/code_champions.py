def render_champions(submissions, minimum_submission_count):
    champions = ""
    count = 0
    champion_name = [submissions[-1][0]]
    champion_score = [submissions[-1][1]]
    # if len(submissions) < minimum_submission_count:
    #     return ""
    for i in range(len(submissions)-1, -1, -1):
        count += 1
        if count >= minimum_submission_count:
            if submissions[i][0] == champion_name[0]:
                champion_score.append(submissions[i][1])
            else:
                if submissions[i][1] <= champion_score[0]:
                    champion_name.append[submissions[i][0]]
                    champion_score.append[submissions[i][1]]



    return champion_name, champion_score
  



if __name__ == "__main__":
    submissions = [('Jane',118), ('John',117), ('John',117), ('Jane',115), ('John',117), ('John',114)]
    minimum_submission_count = 2
    print(render_champions(submissions, minimum_submission_count))
'John - 114, 117 (2); Jane - 115'
