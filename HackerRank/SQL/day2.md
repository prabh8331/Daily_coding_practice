## SQL practice day2

### Station

| Field | Type |
| --- | --- |
| id | number |
| City | varchar(21) |
| State | varchar(2) |
| LAT_N | Number |
| LONG_W | Number |

#### 1. Query a list of CITY and STATE from the STATION table

```sql
select city , state from station
```

#### 2. Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.

```sql
select distinct city from station where id%2=0
```


#### 3. Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

```sql
select (select count(*) from station )-(select count(distinct city) from station )
from dual 
```

#### 4. Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

```sql
select city, length(city) from station 
order by 2 desc,1 limit 1;

select city, length(city) from station 
order by 2,1 limit 1 ;

```

#### 5. Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

```sql
select distinct city from station where lower(left(city,1)) in ("a","e","i","o","u")
```

#### 6. Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

```sql
select distinct city from station where lower(right(city,1)) in ("a","e","i","o","u")
```

#### 7.Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

```sql
select distinct city from station where lower(right(city,1)) in ("a","e","i","o","u") and lower(left(city,1)) in ("a","e","i","o","u")

```