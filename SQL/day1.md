## SQL practice 

### City

| Field | Type |
| --- | --- |
| id | number |
| Name | varchar(17) |
| contrycode | varchar(3) |
| district | varchar(20) |
| population | Number |

#### 1. Query all columns for all american cites in the city table with populations larger than 100000. the countrycode for america is usa 

``` sql
select * from city a where countrycode = "USA" and population > 100000
```

#### 2. Query all the columns for every row in the city table 

``` sql
select * from city a 
```


#### 3. Query all the columns in the city table with ID 1661 

``` sql
select * from city a where id = 1661
```

#### 4. query all attributes if every japanese city in the city table. the countrycode for japan is JPA

``` sql
select * from city a where countrycode = "JPN" 
```

#### 5. query the names of all the japanese cities in the city table. 

``` sql 
select distinct name from city where countrycode = "JPN"
```

