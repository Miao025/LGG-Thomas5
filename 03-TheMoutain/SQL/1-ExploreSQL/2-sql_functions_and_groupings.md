
# SQL Functions and Groupings

SQL functions are prewritten actions that can be called on a cell, record, or database to flexibly manipulate and extract information for further analysis.  

We will focus on two main types:

- **SQL scalar functions**: Take one or more parameters and return a single value.
- **SQL aggregate functions**: Summarize a set of values and return a single value.

---

## Part 1: Exploring Scalar Functions

| Scalar Function | Description                          | Syntax                                              |
|-----------------|--------------------------------------|-----------------------------------------------------|
| `UPPER()` / `LOWER()` | Converts a string to uppercase/lowercase | `SELECT UPPER(column_name) FROM table_name;`        |
| `SUBSTR()`      | Extracts a substring from a string   | `SELECT SUBSTR(column_name, start, length) FROM table_name;` |
| `LENGTH()`      | Returns the length of a string       | `SELECT LENGTH(column_name) FROM table_name;`       |
| `ROUND()`       | Rounds a number to given decimals    | `SELECT ROUND(column_name, decimals) FROM table_name;` |

### Exercises:
1. Find Longest Artist Names  
2. Retrieve 10 customer emails in uppercase format.  
3. Replace “USA” with “usa” in customer countries.  
4. Show track names and durations, rounded to nearest minute.  
5. **Challenge**: Find customers with Gmail using pattern matching and functions.  
6. **Challenge**: Create a report with uppercase album titles, their length, and first 5 characters.

---

## Part 2: Exploring Aggregate Functions

| Aggregate Function | Description                       | Syntax                                         |
|--------------------|-----------------------------------|------------------------------------------------|
| `AVG()`            | Calculates the average value      | `SELECT AVG(column_name) FROM table_name;`     |
| `COUNT()`          | Counts the number of rows         | `SELECT COUNT(column_name) FROM table_name;`   |
| `MAX()`            | Retrieves the maximum value       | `SELECT MAX(column_name) FROM table_name;`     |
| `MIN()`            | Retrieves the minimum value       | `SELECT MIN(column_name) FROM table_name;`     |
| `SUM()`            | Total sum of values in a column   | `SELECT SUM(column_name) FROM table_name;`     |

### Exercises:
1. Total number of tracks  
2. Number of unique composers  
3. Average price per track  
4. Longest and shortest track duration  
5. Date of the latest invoice

---

## Part 3: Applying Aggregate Functions using `GROUP BY`

The `GROUP BY` clause groups rows that have the same values in specified columns, often used with aggregate functions to summarize data.

```sql
SELECT Country, COUNT(*) 
FROM Customers 
GROUP BY Country;
```

### Exercises:
1. Count customers per country  
2. Total spent by each customer (top 10 spenders)  
3. Average track duration per genre  
4. Composers with more than 10 tracks  
5. Total sales per billing country, sorted descending

---

## Part 4: Leveraging Window Functions with `PARTITION BY`

Window functions allow calculations across rows related to the current one—without grouping or collapsing them.

```sql
<function>() OVER (
    PARTITION BY <column>
    ORDER BY <column>
) AS alias
```

- Keeps original rows visible
- Use aggregate or ranking functions like `SUM`, `AVG`, `ROW_NUMBER`, `RANK`

### Exercises:
1. Show each track with the average track length of its genre  
2. Show invoice line totals and their percentage contribution to the invoice

---

## Resources

- [Summarizing Data in SQL - Dataquest](https://www.dataquest.io/tutorial/summarizing-data-in-sql-tutorial/)
- [How SQL Aggregations Work - Data School](https://dataschool.com/how-to-teach-people-sql/how-sql-aggregations-work/)

---

## Pedagogical Objectives

- Explore built-in scalar and aggregate functions  
- Apply the `GROUP BY` clause  
- Understand `WHERE` vs `HAVING`  
- Build complex queries  
- Use aliases and best formatting practices
