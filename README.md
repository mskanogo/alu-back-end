# API Project – Employee TODO Data Export

## Project Overview

This project demonstrates how to interact with a REST API using Python instead of Bash scripting.  

The goal is to retrieve employee TODO list data from an external API and export it into different formats such as standard output, CSV, and JSON.

The API used for this project is:

https://jsonplaceholder.typicode.com

This API provides fake employee and task data that we use for practice.

---

## Learning Objectives

By completing this project, I can explain:

- Why Bash scripting is not suitable for complex data processing
- What an API is
- What a REST API is
- What microservices are
- What the CSV format is
- What the JSON format is
- Pythonic naming conventions
- The importance of PEP8 style
- Why clean and maintainable code matters

---

## Technologies Used

- Python 3.4.3
- Ubuntu 14.04 LTS
- requests module
- csv module
- json module

---

## Requirements

- All files start with:

- All files are executable.
- Imports are organized in alphabetical order.
- Code follows PEP8 style.
- Dictionary values are accessed using `.get()`.
- Code does not execute when imported (uses `if __name__ == "__main__":`).
- Each file ends with a new line.
- All modules contain documentation.

---

## Project Files

### 0-gather_data_from_an_API.py

Retrieves an employee’s TODO list progress and prints:

- Employee name
- Number of completed tasks
- Total number of tasks
- Titles of completed tasks

Usage:

