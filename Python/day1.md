## Python practice

### Say "Hello, World!" with python 
#### 1. print Hello world
``` py
if __name__ == '__main__':
    print("Hello, World!")
```

```
if __name__ == '__main__': construct allows you to write code that will only run when the script is executed directly 
and will not run when the script is imported as a module into another script. It's commonly used 
to include test code or script-specific logic that should only be executed when the script is the main entry point.
```


### Python if-else 
#### qn- Given an integer, , perform the following conditional actions:
#### If  is odd, print Weird
#### If  is even and in the inclusive range of  to , print Not Weird
#### If  is even and in the inclusive range of  to , print Weird
#### If  is even and greater than , print Not Weird

``` py
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    elif n%2 == 0:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")
```            

### Arithmatic Operators 
#### qn- The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
#### The first line contains the sum of the two numbers.
#### The second line contains the difference of the two numbers (first - second).
#### The third line contains the product of the two numbers.

``` py
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
```

### Python: Division 
#### qn- The provided code stub reads two integers,  and , from STDIN.
#### Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

``` py
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
```


### Loops
#### qn- The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

``` py
if __name__ == '__main__':
    n = int(input())
    for x in range(n):
        print(x**2)
```


### Write a function 
#### qn- three conditions are used to identify leap years:
#### The year can be evenly divided by 4, is a leap year, unless:
#### The year can be evenly divided by 100, it is NOT a leap year, unless:
#### The year is also evenly divisible by 400. Then it is a leap year.
```py
def is_leap(year):
    leap = False
    
    if year%4 == 0:
        if year%100 ==0:
            if year % 400 ==0:
                leap = True
        else:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))
```

#### other solution 
```py
def is_leap(year):
    leap = False
    
    if year%4 == 0:
        if year%100 ==0:
            if year % 400 ==0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))
```

### Print Funtion 
#### The included code stub will read an integer, , from STDIN. Without using any string methods, try to print the following: 123..n

```py
if __name__ == '__main__':
    n = int(input())
    srt=''
    for x in range(n):
        srt += str(x+1)
    print(srt)
```


