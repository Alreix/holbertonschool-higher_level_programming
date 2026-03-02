# SQL Introduction

## Description

This project is an introduction to **SQL** and **relational databases** using **MySQL 8.0**.  
It covers the basic concepts of database creation, table management, and data manipulation.

All scripts are written to be executed on **Ubuntu 22.04 LTS** using the MySQL command-line interface.

---

## Learning Objectives

By completing this project, I learned how to:

- Explain what a database is
- Explain what a relational database is
- Understand what SQL stands for (Structured Query Language)
- Use MySQL to manage databases
- Create and delete databases
- Create tables and understand table structure
- Insert, update, delete, and query data
- Use SQL functions such as `COUNT`, `AVG`
- Use filtering, ordering, and grouping (`WHERE`, `ORDER BY`, `GROUP BY`)
- Work with NULL values
- Write clean and readable SQL scripts

---

## Requirements

- Ubuntu 22.04 LTS
- MySQL 8.0
- All SQL keywords are written in **UPPERCASE**
- Each SQL file starts with a comment describing its purpose
- Each SQL query is preceded by a comment
- All files end with a new line
- No forbidden SQL statements are used when restricted by the task

---

## Project Structure

Each file corresponds to a specific task:

| File | Description |
|-----|-------------|
| `0-list_databases.sql` | Lists all databases |
| `1-create_database_if_missing.sql` | Creates a database if it does not exist |
| `2-remove_database.sql` | Deletes a database if it exists |
| `3-list_tables.sql` | Lists all tables in a database |
| `4-first_table.sql` | Creates the `first_table` table |
| `5-full_table.sql` | Displays the full table creation SQL |
| `6-list_values.sql` | Lists all rows from `first_table` |
| `7-insert_value.sql` | Inserts a row into `first_table` |
| `8-count_89.sql` | Counts records with `id = 89` |
| `9-full_creation.sql` | Creates `second_table` and inserts data |
| `10-top_score.sql` | Lists records ordered by score |
| `11-best_score.sql` | Lists records with score ≥ 10 |
| `12-no_cheating.sql` | Updates Bob’s score |
| `13-change_class.sql` | Deletes records with low scores |
| `14-average.sql` | Computes the average score |
| `15-groups.sql` | Counts records grouped by score |
| `16-no_link.sql` | Lists records with a valid name |

---

## Usage

Scripts are executed using standard input redirection:

```bash
cat filename.sql | mysql -hlocalhost -uroot -p database_name
```
Example:
```bash
cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

## Authors
Morgane Abbattista
Holberton School
