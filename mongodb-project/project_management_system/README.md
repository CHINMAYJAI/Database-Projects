# Project Management System

The **Project Management System** is a Python application that helps manage projects using MongoDB as the backend database. It leverages the power of **pymongo** for database operations and **prettytable** for displaying data in a readable table format.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup Virtual Environment](#setup-virtual-environment)
- [Usage](#usage)
- [Tools & Resources](#tools--resources)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **Project Management System** is designed to help users manage and keep track of various projects efficiently. It provides functionalities such as adding, updating, deleting, and listing projects using MongoDB as its database.

---

## Features

- **Add Projects:** Create new projects with details.
- **Update Projects:** Modify existing project details.
- **Delete Projects:** Remove projects from the database.
- **List Projects:** Display a summary of projects in a formatted table.

---

## Tech Stack

- **Programming Language:** Python
- **Database:** MongoDB
- **Modules:** 
  - [pymongo](https://pypi.org/project/pymongo/)
  - [prettytable](https://pypi.org/project/prettytable/)

---

## Project Structure

The repository is organized as follows:

Database-Projects/ └── mongodb-project/ └── project_management_system/ └── main.py


- **Database-Projects:** Parent folder containing various database-related projects.
- **mongodb-project:** Subrepository for MongoDB-based projects.
- **project_management_system:** Subrepository for the project management system.
- **main.py:** The main Python script to run the application.

---

## Installation

### Prerequisites

- **Python 3.x:** Ensure Python 3 is installed on your system.
- **MongoDB:** Install MongoDB on your system or use a cloud-hosted MongoDB service.
- **MongoDB Compass:** (Optional) Use [MongoDB Compass](https://www.mongodb.com/products/compass) for a GUI to interact with your MongoDB database.

### Setup Virtual Environment

It is recommended to use a virtual environment to manage dependencies. You can set one up using `virtualenv`:

1. **Install virtualenv (if not already installed):**
   ```bash
   pip install virtualenv
   ```
2. **Create a virtual environment:**
```bash
virtualenv venv
```

3. **Activate the virtual environment:**
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```
4. **Install the required modules:**
```bash
pip install pymongo prettytable
```

## Usage
1. **Ensure MongoDB is running:**
Start your MongoDB server locally or connect to your remote MongoDB instance.

2. **Run the application:** Navigate to the `project_management_system` directory and run:

```bash
python main.py
```

3. **Follow the on-screen instructions:**
The application will guide you through managing projects.

---

## Tools & Resources
- **MongoDB Compass:** A GUI tool to help you visualize and manage your MongoDB databases easily.

- **Virtual Environment:** Using `virtualenv` ensures that your project's dependencies are isolated.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request. For any major changes, please open an issue first to discuss what you would like to change.

Repository: [CHINMAYJAI/mongodb-project](https://github.com/CHINMAYJAI/Database-Projects/)


## License: 
This project is licensed under the MIT License. See the LICENSE file for details.

---
## Author
[CHINMAY JAIN](https://github.com/CHINMAYJAI/)