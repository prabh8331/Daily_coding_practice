if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    
        
    student_score = [names,scores]
    
    #second_lowest using functions 
    #min_score = min(student_score[1])
    #second_lowest = min([x for x in student_score[1] if x!=min_score])
    
    ###second_lowest using loop
    max_value = student_score[1][0]
    for value in student_score[1]:
        if value > max_value:
            max_value=value

    min_value = student_score[1][0]
    for value in student_score[1]:
        if value < min_value:
            min_value=value

    second_lowest= max_value
    
    for value in student_score[1]:
        if value < second_lowest and value > min_value:
            second_lowest = value

    second_lowest_names = []
    
    for i in range(0,len(student_score[0])):
        if student_score[1][i] == second_lowest:
            second_lowest_names.append(student_score[0][i])
        
    second_lowest_names = sorted(second_lowest_names) 
    
    for i in range(0,len(second_lowest_names)):
        print(second_lowest_names[i])
