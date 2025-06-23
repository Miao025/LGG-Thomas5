# SQL Constraints in SQLite

In this notebook you will learn how **constraints** protect data quality and establish relationships between tables.

**Create your own example database** for these exercises to play with constraints freely.

---

## 1. Why Constraints Matter

- **`PRIMARY KEY`** → guarantees a unique identifier for each row  
- **`FOREIGN KEY`** → enforces referential integrity between tables  
- **`UNIQUE`** → prevents duplicate values in a column or set of columns  
- **`NOT NULL`** → disallows missing values  
- **`CHECK`** → limits values with custom expressions  
- **`DEFAULT`** → supplies a fallback value when none is given

SQLite supports them all, but remember to enable foreign‑key checks:

```sql
PRAGMA foreign_keys = ON;
```

---

## 2. Creating Tables with Constraints

```sql
CREATE TABLE IF NOT EXISTS Categories (
    category_id INTEGER PRIMARY KEY,
    name        TEXT    NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS Products (
    product_id   INTEGER PRIMARY KEY,
    name         TEXT    NOT NULL,
    category_id  INTEGER     REFERENCES Categories(category_id)
                               ON DELETE SET NULL
                               ON UPDATE CASCADE,
    price        REAL    NOT NULL CHECK(price > 0),
    stock_qty    INTEGER DEFAULT 0
);
```

### Exercise 2 — Build Your Own

> **Task 2.1**  
> Create a **`Customers`** table with the following rules:  
> - `customer_id` → PK  
> - `email` → text, **unique** and **not null**  
> - `join_date` → text, default today’s date  
> - `credit_limit` → real, must be **greater than 0**
---

## 3. Testing Constraint Enforcement

Try the following inserts and see what happens:

```sql
-- (A) Duplicate UNIQUE value
INSERT INTO Categories (name) VALUES ('Toys');
INSERT INTO Categories (name) VALUES ('Toys');   -- should fail

-- (B) FOREIGN KEY violation
INSERT INTO Products (name, category_id, price)
VALUES ('Widget‑X', 999, 19.99);                  -- should fail

-- (C) CHECK violation
INSERT INTO Products (name, price)
VALUES ('Freebie', -5);                           -- should fail
```

> **Task 3.1**  
> Write one `INSERT` per scenario above and observe the error messages. Make a note *which* constraint fired.

---

## 3. Testing Deeper the Foreign Key Constraint

First we populate the tables:

```sql
-- Insert three categories
INSERT INTO Categories (category_id, name, description) VALUES
    (1, 'Electronics', 'Gadgets and devices'),
    (2, 'Clothing',    'Apparel and accessories'),
    (3, 'Books',       'Printed and digital books');

-- Insert four products that reference those categories
INSERT INTO Products (product_id, name, category_id, price, stock_qty) VALUES
    (1, 'Smartphone',  1, 699.99,  50),
    (2, 'T-Shirt',     2,  19.99, 100),
    (3, 'Novel',       3,   9.99, 200),
    (4, 'Headphones',  1, 199.99,  30);
```

> **Task 4.1**  
> Look at how the foreign key constraint was defined on `category_id` in `Products`. What does `ON DELETE`/`ON UPDATE` and `SET NULL`/`CASCADE` mean? If you also think `CASCADE` sounds cool send me the message "I agree, Cascade sounds cool" on discord just so I know you're actually doing my content. If you don't think it sounds cool you can also message me your bad opinion. Thank you :)

> **Task 4.2**
> Test it out!
> Update the category_id of 'Books' to 4 in the `Categories` table. What happend to the products associated to it in the `Products` table? Now delete this category altogether. What happend in the `Products` table?

---

## 5. Composite Keys & Multi‑Column UNIQUE

```sql
CREATE TABLE IF NOT EXISTS Enrolments (
    student_id  INTEGER,
    course_id   INTEGER,
    enrolled_at TEXT DEFAULT (DATE('now')),
    PRIMARY KEY (student_id, course_id)
);
```

### Exercise 5

> **Task 5.1**  
> Insert two identical rows into `Enrolments`. Explain why the second insert fails.

## Further Reading

- [SQLite Constraints](https://www.sqlite.org/lang_createtable.html#constraints)
- [SQLite Foreign Keys](https://www.sqlite.org/foreignkeys.html)

---

### Pedagogical Objectives

* Describe the purpose of each major SQL constraint.  
* Apply constraints when creating tables in SQLite.  
* Detect and interpret constraint‑violation errors.  
* Understand cascading actions for foreign keys.
