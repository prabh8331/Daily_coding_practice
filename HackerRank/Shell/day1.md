## Linus shell practice 

#### 1. Write a bash script that prints "Hello"

``` bash
echo "Hello"
```


#### 2. Write a Bash script which accepts name as input and displays the greeting "Welcome (name)"

``` bash
read name
echo "Welcome $name"
```

#### 3. use a loop to display the natural numbers from 1 to 50

``` bash
for i in {1..50}; do
    echo $i
done
```

``` bash
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    count=$((count + 1))
done
```

#### 4. given two integers , X & Y, find their sum, difference, product and quotient. 

``` bash
read X
read Y
echo $((X+Y))
echo $((X-Y))
echo $((X*Y))
echo $((X/Y))
```

#### 5. given two integers , X and Y, identify wheter X< Y or X>Y or X = Y, Exactly one of the following lines:
`X is less than Y`
`X is greater than Y`
`X is equal to Y`

`-eq:` Equal to
`-ne:` Not equal to
`-lt:` Less than
`-le:` Less than or equal to
`-gt:` Greater than
`-ge:` Greater than or equal to

```  bash
read X
read Y

if [ $X -eq $Y ]; then
    echo "X is equal to Y"
elif [ $X -lt $Y ]; then 
    echo "X is less than Y"
else
    echo "X is greater than Y"
fi
```

