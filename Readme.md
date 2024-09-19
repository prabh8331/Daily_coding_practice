

Create git repository with vscode

create a folder in some location 
open vs code and open this new folder
click on terminal 
type 
> git init

create readme.md

and do the first commit 

click on Publish Branch 




few qns to solve: 

1. pyspark

you have follwoing table

| EMP_ID | FIRST_NAME | LAST_NAME | SALARY  | JOINING_DATE         | DEPARTMENT |
|--------|------------|-----------|---------|----------------------|------------|
| 1      | Monika     | Arora     | 100000  | 20-02-2014 9:00      | HR         |
| 2      | Niharika   | Verma     | 80000   | 11-06-2014 9:00      | Admin      |
| 3      | Vishal     | Singhal   | 300000  | 20-02-2014 9:00      | HR         |
| 4      | Amitabh    | Singh     | 500000  | 20-02-2014 9:00      | Admin      |
| 5      | Vivek      | Bhati     | 500000  | 11-06-2014 9:00      | Admin      |
| 6      | Vipul      | Diwan     | 200000  | 11-06-2014 9:00      | Account    |
| 7      | Satish     | Kumar     | 75000   | 20-01-2014 9:00      | Account    |
| 8      | Geetika    | Chauhan   | 90000   | 11-04-2014 9:00      | Admin      |

write a code to find such employs who have less salary than the average salary of their dep 

```py
Df= read


Df_avg = df.select(department,salary).aggregate(avg(salary).alias("avg_salary")

Df_filter=df.alias("a").join(af_avg.alias("b"),"a.department=b.department","left").filter(a.salary<b.avg_salary))

```

2. python

you have above same table , how you will know if there is any special character in salary in dataframe in python 

3. 



2. Create an incremental refresh datapipeline
write a code where data from oracle goes to intermidate table and to the destination table



how to will do optimazation of data in aws athena and How will you do partationby and indexing in aws aetna, and how do you optimize the query in aethna





#### 1. PySpark: Find Employees with Salary Less Than Average Salary of Their Department

To solve this problem, you can use PySpark's DataFrame API to first compute the average salary for each department and then filter the employees who earn less than the average salary of their department. Here’s how you can do it:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

# Initialize Spark session
spark = SparkSession.builder.appName("EmployeeSalary").getOrCreate()

# Sample data
data = [
    (1, "Monika", "Arora", 100000, "20-02-2014 9:00", "HR"),
    (2, "Niharika", "Verma", 80000, "11-06-2014 9:00", "Admin"),
    (3, "Vishal", "Singhal", 300000, "20-02-2014 9:00", "HR"),
    (4, "Amitabh", "Singh", 500000, "20-02-2014 9:00", "Admin"),
    (5, "Vivek", "Bhati", 500000, "11-06-2014 9:00", "Admin"),
    (6, "Vipul", "Diwan", 200000, "11-06-2014 9:00", "Account"),
    (7, "Satish", "Kumar", 75000, "20-01-2014 9:00", "Account"),
    (8, "Geetika", "Chauhan", 90000, "11-04-2014 9:00", "Admin")
]

# Create DataFrame
df = spark.createDataFrame(data, ["EMP_ID", "FIRST_NAME", "LAST_NAME", "SALARY", "JOINING_DATE", "DEPARTMENT"])

# Compute average salary per department
df_avg = df.groupBy("DEPARTMENT").agg(avg("SALARY").alias("avg_salary"))

# Join original DataFrame with average salary DataFrame and filter
df_filtered = df.alias("a").join(df_avg.alias("b"), col("a.DEPARTMENT") == col("b.DEPARTMENT"), "left") \
    .filter(col("a.SALARY") < col("b.avg_salary"))

df_filtered.show()
```

#### 2. Python: Detect Special Characters in Salary

To find if there are any special characters in the salary column in a pandas DataFrame, you can use regular expressions.

```python
import pandas as pd
import re

# Sample data
data = {
    'EMP_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'FIRST_NAME': ["Monika", "Niharika", "Vishal", "Amitabh", "Vivek", "Vipul", "Satish", "Geetika"],
    'LAST_NAME': ["Arora", "Verma", "Singhal", "Singh", "Bhati", "Diwan", "Kumar", "Chauhan"],
    'SALARY': ["100000", "80000", "300000", "500000", "500000", "200000", "75000", "90000"],
    'JOINING_DATE': ["20-02-2014 9:00", "11-06-2014 9:00", "20-02-2014 9:00", "20-02-2014 9:00", "11-06-2014 9:00", "11-06-2014 9:00", "20-01-2014 9:00", "11-04-2014 9:00"],
    'DEPARTMENT': ["HR", "Admin", "HR", "Admin", "Admin", "Account", "Account", "Admin"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to check for special characters in salary
def contains_special_chars(value):
    return bool(re.search(r'[^0-9.]', value))

# Apply function to 'SALARY' column
df['contains_special_chars'] = df['SALARY'].apply(contains_special_chars)

# Display rows with special characters
print(df[df['contains_special_chars']])
```

#### 3. Create an Incremental Refresh Data Pipeline

For a data pipeline from Oracle to an intermediate table and then to a destination table, you can use a combination of Python and SQL. Here’s a high-level approach:

**Python Example Using `pandas` and `sqlalchemy`**

```python
from sqlalchemy import create_engine

# Create connection to Oracle and destination database
oracle_engine = create_engine('oracle://username:password@oracle_host:port/dbname')
destination_engine = create_engine('mysql://username:password@destination_host:port/dbname')

# Read data from Oracle
query = "SELECT * FROM source_table WHERE last_modified > (SELECT last_refresh_time FROM refresh_metadata)"
df = pd.read_sql(query, oracle_engine)

# Write data to intermediate table
df.to_sql('intermediate_table', destination_engine, if_exists='replace', index=False)

# Further processing and moving data to destination table
df.to_sql('destination_table', destination_engine, if_exists='append', index=False)
```

**Note**: You'll need to replace placeholders with actual values and adjust connection strings according to your databases.

#### 4. AWS Athena Optimization

**Partitioning and Indexing in AWS Athena:**

1. **Partitioning**:
   - **How to Partition**: When creating tables in Athena, use the `PARTITIONED BY` clause to partition data by one or more columns.
   - **Example**:
     ```sql
     CREATE TABLE my_table (
       col1 STRING,
       col2 INT
     )
     PARTITIONED BY (year STRING, month STRING);
     ```

2. **Indexing**:
   - Athena doesn’t support traditional indexing. Instead, optimize queries by partitioning tables and using columnar formats like Parquet or ORC.

3. **Query Optimization**:
   - **Use Columnar Formats**: Store data in formats like Parquet or ORC for better performance.
   - **Filter Data Early**: Use partition columns in your `WHERE` clauses to minimize the amount of data scanned.
   - **Optimize Queries**: Use `EXPLAIN` to understand query performance and adjust as needed.

**Example of Optimized Query**:
```sql
SELECT col1, col2
FROM my_table
WHERE year = '2024' AND month = '09'