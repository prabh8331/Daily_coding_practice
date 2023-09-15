#qn- write a bash script that prints "Hello"
echo "Hello"


#qn- Write a Bash script which accepts name as input and displays the greeting "Welcome (name)"

read name
echo "Welcome $name"

#qn- use a loop to display the natural numbers from 1 to 50

for i in {1..50}; do
    echo $i
done


count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    count=$((count + 1))
done

#qn- given two integers , X & Y, find their usm, difference, product and quotient. 
read X
read Y
echo $((X+Y))
echo $((X-Y))
echo $((X*Y))
echo $((X/Y))



# given two integers , X and Y, identify wheter X< Y or X>Y or X = Y
# Exactly one of the following lines:
# - X is less than Y
# - X is greater than Y
# - X is equal to Y

#   -eq: Equal to
#   -ne: Not equal to
#   -lt: Less than
#   -le: Less than or equal to
#   -gt: Greater than
#   -ge: Greater than or equal to


read X
read Y

if [ $X -eq $Y ]; then
    echo "X is equal to Y"
elif [ $X -lt $Y ]; then 
    echo "X is less than Y"
else
    echo "X is greater than Y"
fi


