# Python - Classes and Objects

## Description

This project introduces the basics of Object-Oriented Programming (OOP) in Python.  
It focuses on defining classes, creating instances, handling private attributes, validating data using getters and setters, and implementing public methods.

The exercises progressively build a `Square` class and add new behaviors step by step.

---

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version **3.8.5**)
- All files should end with a new line
- The first line of all files must be:
- A `README.md` file at the root of the project directory is mandatory
- Code must follow **pycodestyle** (version `2.7.*`)
- All files must be executable
- File length will be tested with `wc`
- All modules must have documentation  
(`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes must have documentation  
(`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside classes) must have documentation  
(`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation must consist of full sentences explaining the purpose of the module, class, or method

---

## Project Tasks

### **0. My first square**
Create an empty class `Square`.

---

### **1. Square with size**
Add a private instance attribute `size`.  
Instantiation with `size`.

---

### **2. Size validation**
Validate `size`:
- Must be an integer (`TypeError`)
- Must be >= 0 (`ValueError`)

---

### **3. Area of a square**
Add the public method `area()` that returns the square area.

---

### **4. Access and update private attribute**
Use properties:
- Getter `size`
- Setter `size` (with validation)

---

### **5. Printing a square**
Add public method `my_print()`:
- Print square using `#`
- If `size == 0`: print an empty line

---

### **6. Coordinates of a square**
Add a new private attribute `position`:
- Use getter and setter
- Validate that `position` is a tuple of 2 non-negative integers

Update `my_print()` to take `position` into account:
- `position[0]` → horizontal offset (spaces)
- `position[1]` → vertical offset (new lines)

---

## Example

```python
>>> square = Square(3, (1, 1))
>>> square.area()
9
>>> square.my_print()

###
###
###

