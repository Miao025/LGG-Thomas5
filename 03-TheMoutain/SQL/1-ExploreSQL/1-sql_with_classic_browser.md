# SQL with the Classic SQL Browser for SQLite

## Getting Started: Installing the Classic SQL Browser for SQLite

Before you begin, make sure you have the classic SQL browser for SQLite installed.

You can download it from the official website: [https://sqlitebrowser.org/](https://sqlitebrowser.org/)

- For Windows, macOS, and Linux: Choose the appropriate installer and follow the installation instructions on the site.
- Once installed, open the application to begin working with your SQLite database.

Read more:
- [SQL Editor (SQLite browser)](https://www.sqlitetutorial.net/sqlite-sample-database/)

---

## Relational databases: Review

A **relational database** is a way of structuring information in tables, rows, and columns. You could compare it to an excel file (database) with several sheets (tables) that contain tabular data (rows and columns). The particularity of this database is its ability to create relationships between those tables by joining them.

What is a `join`? Let's take an example by looking at the schema of a database of a music producer. You can see here that certain fields are common between several tables.

For example: `ArtistID` exists in `artists` and in `albums`. Consequently the information from an artist can be included (_joined_) to the information of his/her albums.

<img src="https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg" />

SQL (Structured Query Language) is one of the most common languages for interacting with a relational database. It allows you to perform efficient and precise queries on the database, including queries among different tables.

SQL mainly allows you to `select`, `insert`, `update` or `delete` data from the DB.

---

## Part 1: Exploring CRUD Commands

SQL can be used to perform CRUD (Create, Retrieve, Update, Delete) operations on a database.

- **Download the sample database file**  
- **Connect to the database**:  
  - Open the classic SQL browser for SQLite  
  - Navigate to `File → Open Database`  
  - The sample database file `music.db` can be found in the `data` subdirectory.

---

### `SELECT … FROM …`

This command allows you to retrieve data from a specific or multiple tables.

```sql
SELECT * FROM Customers;
```

Analyze the syntax.  
- What is the purpose of the `*` symbol?  
- What happens if you don’t include the semicolon?  
- What are the results displayed?

---

### `WHERE`

Add conditions to your results. For example:

```sql
SELECT * FROM customers
WHERE country = "Belgium";
```

---

### `LIMIT`

Limit the number of results:

```sql
SELECT * FROM customers
LIMIT 5;
```

---

### `DISTINCT`

Display only unique values:

```sql
SELECT DISTINCT Country FROM customers;
```

How many countries are represented in the data?

---

### `ORDER BY`

Sort the results:

```sql
SELECT * FROM customers
ORDER BY Country;
```

---

### Try It Yourself

Pick one table and explore it using the commands above. Document your commands and share them with a colleague.

1. Show the first 10 entries of the table `artists`  
2. Find the ID of `Aerosmith`  
3. Find the IDs of the albums of `Aerosmith`

---

## Creating and Modifying Tables

### `CREATE`

Create a new table called `MyFavoriteTracks`:

```sql
CREATE TABLE MyFavoriteTracks (
  TrackName TEXT,
  Artist TEXT,
  Mood TEXT
);
```

What happens when you run this command?  
Tip: Refresh the schema view to see your new table.

---

### `INSERT`

Add records:

```sql
INSERT INTO MyFavoriteTracks
  (TrackName, Artist, Mood)
VALUES
  ('Silver Springs', 'Fleetwood Mac', 'Dramatic'),
  ('What a feeling', 'Irene Cara', 'Energetic'),
  ('Stairway to Heaven', 'Heart', 'Inspiring');
```

---

### `UPDATE`

Update a record:

```sql
UPDATE TempCustomer
SET Email = "daan_peeters@gmail.com"
WHERE CustomerId = 8;
```

Why is it important to use the `WHERE` clause correctly?

---

### `DELETE`

Delete a record:

```sql
DELETE FROM MyFavoriteTracks WHERE TrackName = 'What a feeling';
```

**⚠ Be careful!** If you omit the `WHERE` clause, all records will be deleted.

---

### Check Your Table

```sql
SELECT * FROM MyFavoriteTracks;
```

---

## Bonus Challenges

- Insert 3 more songs and categorize them by genre.
- Update one song’s mood.
- Delete one track you don’t like anymore.

---

## Additional Resources

- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/default.asp)
- [SQLite Sample Database](https://www.sqlitetutorial.net/sqlite-sample-database/)
- [Introduction to SQL - DataQuest](https://www.dataquest.io/tutorial/introduction-to-sql-and-databases-tutorial/)
- [SQL Order of Execution - DataCamp](https://www.datacamp.com/tutorial/sql-order-of-execution)

---

## Pedagogical Objectives

- Open and navigate the classic SQL browser for SQLite
- Execute basic SQL queries: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- Use `WHERE` clauses to filter data
- Understand the logical execution order of SQL commands
- Apply `ORDER BY` and `LIMIT`
- (Optional) Use `LIKE`, `BETWEEN`, and conditionals for complex filtering
