# Contact Book

A Python-based contact management system that allows users to store, retrieve, and manage their contacts efficiently.

---

## Overview

This project, maintained by **CHINMAYJAI**, is part of the **Database-Projects** collection. It serves as a practical implementation of contact management using Python, showcasing different versions of the script for better understanding and evolution of the code.

---

## Project Directory Structure

```plaintext
contact_book/
|── contact_book_version_1.0.py   # Version 1
│── contact_book_version_2.0.py   # Version 2
│── contact_book_version_3.0.py   # Version 3: Latest version of the contact
└── README.md                     # Project documentation
```

---

## Features

- **Contact Management**: Add, update, delete, and retrieve contacts.
- **Versioned Scripts**: Easy comparison between different versions of the contact management script.
  - **contact_book_version_1.0.py**: Basic version where users cannot search existing contacts.
  - **contact_book_version_2.0.py**: Introduces the ability to search for existing contacts by providing a hardcoded name.
  - **contact_book_version_3.0.py**: Enhances search functionality to allow users to search by first or last name without hardcoding. This version is case-insensitive, providing greater flexibility. The entire codebase has been refactored into an object-oriented programming (OOP) format.
- **User-Friendly Interface**: Simple command-line interface for interaction.

---

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/CHINMAYJAI/Database-Projects.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd Database-Projects/mongodb-project/contact_book
   ```

3. **Install MongoDB**:
   - Follow the instructions on the [MongoDB installation page](https://docs.mongodb.com/manual/installation/) to install MongoDB on your system.
   - Ensure that the MongoDB service is running. You can start it using the following command (for Windows):
     ```bash
     net start MongoDB
     ```

4. **Install Pymongo**:
   - Use pip to install the `pymongo` library, which allows Python to interact with MongoDB:
   ```bash
   pip install pymongo
   ```

5. **Run the Script:**
   Execute the main script using Python:
   ```bash
   python contact_book/contact_book_version_1.0.py
   ```

6. **Explore the Code:**
   Open the `scripts` folder in your preferred code editor to review and modify the Python scripts as needed.

## Technologies Used

- **Python**: For implementing the contact management logic.
- **MongoDB**: Database where the contacts are saved

## License
This project is licensed under the MIT License.

## Contact
For questions, feedback, or contributions, please reach out to **CHINMAYJAI** via GitHub.

## Author
[CHINMAY JAIN](https://github.com/CHINMAYJAI/)