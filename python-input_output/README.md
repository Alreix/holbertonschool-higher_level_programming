# Python Input / Output

## Description

This project focuses on understanding and practicing Python input/output operations, JSON serialization and deserialization, file handling, and basic object persistence. Through a series of progressive exercises, you learn how to read and write files, work with JSON, convert objects to serializable formats, and rebuild objects from saved data.

The project also includes a classic technical interview exercise: generating Pascal's Triangle.

---

## Learning Objectives

At the end of this project, you should be able to:

* Read from and write to text files in Python
* Understand and use JSON serialization and deserialization
* Convert Python objects to JSON-compatible dictionaries
* Rebuild Python objects from stored data
* Handle command-line arguments in scripts
* Understand basic persistence mechanisms
* Apply clean code and Python style guidelines

---

## Requirements

### Python Scripts

* Allowed editors: **vi**, **vim**, **emacs**
* All files will be interpreted/compiled on **Ubuntu 20.04 LTS**
* Python version: **Python 3.8.5**
* All files must end with a new line
* The first line of all files must be exactly:

  ```bash
  #!/usr/bin/python3
  ```
* A **README.md** file at the root of the project directory is mandatory
* Code must follow **pycodestyle** (version **2.7.*** )
* All files must be executable
* The length of files will be tested using `wc`

---

## Project Structure

```
python-input_output/
│
├── 0-read_file.py
├── 1-write_file.py
├── 2-append_write.py
├── 3-to_json_string.py
├── 4-from_json_string.py
├── 5-save_to_json_file.py
├── 6-load_from_json_file.py
├── 7-add_item.py
├── 8-class_to_json.py
├── 9-student.py
├── 10-student.py
├── 11-student.py
├── 12-pascal_triangle.py
└── README.md
```

---

## Exercises

### 0. Read file

Write a function that reads a text file (UTF-8) and prints its content to stdout.

---

### 1. Write to a file

Write a function that writes a string to a text file (UTF-8) and returns the number of characters written.

---

### 2. Append to a file

Write a function that appends a string at the end of a text file (UTF-8) and returns the number of characters added.

---

### 3. To JSON string

Write a function that returns the JSON representation (string) of an object.

---

### 4. From JSON string

Write a function that returns a Python object represented by a JSON string.

---

### 5. Save Object to a file

Write a function that writes an object to a text file using JSON representation.

---

### 6. Create object from a JSON file

Write a function that creates a Python object from a JSON file.

---

### 7. Load, add, save

Write a script that adds all command-line arguments to a Python list and saves them to a file using JSON.

---

### 8. Class to JSON

Write a function that returns the dictionary description of a simple data structure for JSON serialization of an object.

---

### 9. Student to JSON

Write a `Student` class with a method that returns a dictionary representation of the instance.

---

### 10. Student to JSON with filter

Extend the `Student` class to filter attributes returned in the JSON representation.

---

### 11. Student to disk and reload

Extend the `Student` class with a method that replaces all attributes using a dictionary (deserialization).

---

### 12. Pascal's Triangle

Write a function that returns a list of lists of integers representing Pascal's Triangle of `n`.

---

## Author
Alerix - Morgane Abbattista
Project completed as part of the **Holberton School** curriculum.

