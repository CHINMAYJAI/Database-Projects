
# ToDo List Notifier

This Python project is a **ToDo List Notifier** that helps you manage and notify tasks based on time. It uses **MongoDB** for task storage and **Plyer** for system notifications. Tasks are stored in a MongoDB collection and sorted by time to ensure timely notifications.

## Features

- Add tasks to the database with a specified time.
- Automatically sorts tasks by time for efficient reminders.
- Notifies users of upcoming tasks.
- Deletes completed tasks from the database after notifying.

## Prerequisites

- Python 3.x
- MongoDB database
- Environment variable `MongoDBLink` set to your MongoDB connection link.
- Required Python libraries:
  - `pymongo`
  - `plyer`


## Installation

1. Clone the repository:

```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

```
2. Install the required libraries:
```bash
   pip install pymongo plyer
```
3. Set up your environment variable MongoDBLink with your MongoDB connection string.

## Usage

Run the Script
```python
task_remainder.py
```
2. Follow the prompts to:

- Enter a task description.
- Provide the time for the task in HH:MM (24-hour format).
3. Notifications will appear when the specified task time is reached.

## Code Highlights
### Functions
1. openingDatabase():

- Establishes a connection with MongoDB and creates/opens a database and collection.
2. enteringTask(task, list_time, collection):

- Adds a task to the MongoDB database, ensuring tasks are stored in time-sorted order.
3. notifyingTask(collection):

- Checks for upcoming tasks, sends notifications, and removes completed tasks from the database.

## Example
### Adding a Task
``` bash
Task: Complete Python assignment
NOTE: time must be in **HH:MM 24 hour** format
Enter time: 15:30
```
### Notification Example
- At 15:30, you will receive:
- Title: Complete Python assignment
- Message: Here is your reminder, please accomplish it.

## Contribution

Feel free to fork the repository and submit a pull request if you'd like to improve this project. Suggestions and feedback are welcome!

## Author

[Chinmay Jain](https://github.com/CHINMAYJAI)