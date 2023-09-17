if __name__ == '__main__':
    n = int(input())  #this input is given by code checker to input the answer value   5
    arr = map(int, input().split())  # this input is to enter test   2 3 6 6 5
    
    arr = list(arr)

    #Method 1
    #max_value = max(arr)
    #filtered_list = [x for x in arr if x != max_value]
    #print(max(filtered_list))

    max_value = 0
    for value in arr:
        if value > max_value:
            max_value=value
    
    second_max=0            
    for value in arr:
        if value > second_max and value!=max_value:
            second_max=value         
            
    print(second_max)