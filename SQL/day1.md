

### query all columns for all american cites in the city table with populations larger than 100000. the countrycode for america is usa 

### City

| Field | Type |
| --- | --- |
| id | number |
| Name | varchar(17) |
| contrycode | varchar(3) |
| district | varchar(20) |
| population | Number |


``` sql
select * from city a where countrycode = "USA" and population > 100000
```

