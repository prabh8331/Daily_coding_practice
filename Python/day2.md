## Python practice day2 

### 1.  Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

#### Print Hello world
``` py
if __name__ == '__main__':
    n = int(input())  #this input is given by code checker to input the answer value   5
    arr = map(int, input().split())  # this input is to enter test   2 3 6 6 5
    
    arr = list(arr)

    max_value = max(arr)
    
    filtered_list = [x for x in arr if x != max_value]
    
    print(max(filtered_list))
```

### Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
    Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

<details>
  <summary>starting code:</summary>

  ```py
  if __name__ == '__main__':
      for _ in range(int(input())):
          name = input()
          score = float(input())
  ```

</details>

<details>
  <summary>input:</summary>
  
  ```
  5
  Harry
  37.21
  Berry
  37.21
  Tina
  37.2
  Akriti
  41
  Harsh
  39
  ```
  
</details>


```py
if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    
        
    student_score = [names,scores]
    
    min_score = min(student_score[1])
    
    second_lowest = min([x for x in student_score[1] if x!=min_score])
    
    second_lowest_names = []
    
    for i in range(0,len(student_score[0])):
        if student_score[1][i] == second_lowest:
            second_lowest_names.append(student_score[0][i])
        
    second_lowest_names = sorted(second_lowest_names) 
    
    for i in range(0,len(second_lowest_names)):
        print(second_lowest_names[i])

```