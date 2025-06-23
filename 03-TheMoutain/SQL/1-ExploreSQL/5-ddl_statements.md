# SQL: Data Definition Language (DDL) with SQLite

Welcome to your notebook on **Data Definition Language (DDL)** commands in SQLite.  
DDL statements let you define, modify and remove objects in the database schema.
We'll focus on exploring the DDL statements on tables today, but know that these may also apply to various other database objects such as views or procedures.

---

## 1. Inspecting the Existing Schema

SQLite keeps a record of every object in `sqlite_master`.

```sql
-- List every table
SELECT name, type
FROM sqlite_master
WHERE type = 'table';
```

> **Task 1.1**  
> Use `PRAGMA table_info(<table_name>)` to list the columns of the `albums` table.

---

## 2. `CREATE TABLE`

Every table starts life with a `CREATE TABLE` statement.

### Exercise 2 — Create your own table

> Create a table called **`MusicPublishers`** with these columns:  
> - `publisher_id` → integer primary key  
> - `name` → text, **must not be null** 
> - `country` → text  
> - `founded_year` → integer

Check your work:

```sql
PRAGMA table_info(MusicPublishers);
```

*What data types did SQLite assign? Why?*

---

## 3. `ALTER TABLE`

SQLite’s `ALTER TABLE` supports **adding** a column or **renaming** objects.

### Exercise 3

> **Task 3.1**  
> Add a `rating` column (integer, default 0) to the `MusicPublishers` table.  
>   
> **Task 3.2**  
> Rename `MusicPublishers` back to `Publishers`.

---

## 4. `DROP TABLE`

This is how you may delete the Publishers table:

```sql
DROP TABLE IF EXISTS Publishers;
```

## 5. Knowledge Check (Self‑Test)

Copy‑paste these statements into a fresh database. They should execute **without errors**.

```sql
CREATE TABLE IF NOT EXISTS TestDDL (
    id      INTEGER PRIMARY KEY,
    note    TEXT
);

ALTER TABLE TestDDL
ADD COLUMN created_at TEXT DEFAULT (datetime('now'));

DROP TABLE IF EXISTS TestDDL;
```

If everything runs, your environment handles `CREATE`, `ALTER`, and `DROP` correctly.

---

## Further Reading

- [SQLite DDL documentation](https://www.sqlite.org/lang.html)
- [SQLite PRAGMA statements](https://www.sqlite.org/pragma.html)

---

### Pedagogical Objectives

* Identify the purpose of DDL commands (`CREATE`, `ALTER`, `DROP`).  
* Practice creating and altering tables with common column constraints.  
* Understand database schema inspection with `PRAGMA` and `sqlite_master`.  
* Recognise the effect of destructive operations such as `DROP TABLE`.
