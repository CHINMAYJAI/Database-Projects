from pymongo import MongoClient
import datetime
from os import environ
from plyer import notification
import time


# NOTE: function is successfully completed
def openingDatabase():
    """setting connection and creating/opening database/collection in mongodb"""
    mongodb_connection = environ.get("MongoDBLink")
    connectionEstablish = MongoClient(mongodb_connection)
    database = connectionEstablish["ToDo-List"]
    current_date = datetime.date.today()
    collection = database[f"{current_date} tasks"]
    return collection


# NOTE: function is successfully completed
def enteringTask(task, list_time, collection):
    """This function is used to enter the data into database"""
    hour = str(list_time[0])
    minute = str(list_time[1])
    data = {"Task": task, "Time": hour + " " + minute}

    hour_int = int(hour)
    minute_int = int(minute)

    tasks = list(collection.find())

    if not tasks:
        collection.insert_one(data)
    else:
        tasks.append(data)  # Add the new task
        # Sorting tasks based on time (insertion sort logic)
        tasks.sort(key=lambda x: (int(x["Time"].split()[0]), int(x["Time"].split()[1])))
        # Re-insert sorted tasks back into the collection
        collection.delete_many({})  # Remove all previous documents
        collection.insert_many(tasks)  # Insert all tasks in the correct order

    print("Task entered successfully")


# NOTE: function is successfully completed
def notifyingTask(collection):
    """This is used to notify the Task that is coming next (based on the time)"""
    while collection.count_documents({}) != 0:  # if the number_of_documents != 0
        for document in collection.find():
            task = document["Task"]
            _time = document["Time"]
            hour = str(_time[0]) + str(_time[1])
            minute = str(_time[3]) + str(_time[4])
            break
        # fetching the current time from the system
        current_time = datetime.datetime.now().strftime("%M")
        # if time current_time and the minute are same then notify the user to accomplished the task
        if int(current_time) == int(minute):
            notification.notify(
                title=task,
                message="Here is your remainder, please accomplished it",
                timeout=10,
            )
        # if the time isn't reached
        else:
            time_left = abs(int(minute) - int(current_time))
            time.sleep(time_left * 60)
            notification.notify(
                title=task,
                message="Here is your remainder, please accomplished it",
                timeout=10,
            )
        # now deleting that task from the database
        collection.delete_one({"Task": task})
        print("Task removed from the database")


if __name__ == "__main__":
    # opening the database
    collection = openingDatabase()
    # asking the task from the user
    task = str(input("Task: "))
    # asking the time from the user
    print("NOTE: time must be in **HH:MM 24 hour** format")
    raw_time = str(input("Enter time: "))
    list_time = raw_time.split(":")
    enteringTask(task, list_time, collection)
    notifyingTask(collection)