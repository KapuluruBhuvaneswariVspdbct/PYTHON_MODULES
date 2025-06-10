# 📦 Python Modules

This repository contains notes and examples related to **Python Modules** — a key concept to structure your programs and promote code reuse.

---

## 📘 What are Modules?

A module is a file containing Python definitions and statements. Grouping related code into modules makes your code more organized and maintainable.

---

## 🔍 Topics Covered

- Creating your own module
- Importing modules (`import`, `from ... import`, `as`)
- Built-in modules (e.g., `math`, `random`, `datetime`)
- The `__name__ == "__main__"` usage
- Module search path (`sys.path`)
- Organizing code using packages (`__init__.py`)

---

## 🧪 Example

### 1. mymodule.py

def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

2. main.py
import mymodule
print(mymodule.add(3, 5))
print(mymodule.greet("Alice"))

🧪 Built-in Module Examples
1. math Module
import math
print(math.factorial(5))  # Output: 120

3. random Module
import random
print(random.choice(['apple', 'banana', 'cherry']))

5. datetime Module
from datetime import datetime
print(datetime.now())  # Output: current date and time

📂 Folder Structure
/python-modules
    ├── mymodule.py
    ├── main.py
    └── README.md
    
🚀 Run the Code
python main.py
🧑‍💻 Created By
Bhuvaneswari Kapuluru
