from pymongo import MongoClient
from bson.objectid import ObjectId
from os import environ
from datetime import datetime
import random
from prettytable import PrettyTable

# Connecting to mongodb database
client = MongoClient(environ["MongoDBLink"])
db = client["ProjectsManagementTool"]


# Creating a class for the project management tool
class ProjectManagementTool:
    """This is the class for the project management tool"""

    def __init__(self):
        """This is the constructor of the class"""
        self.serial_number = 0
        self.project_name = ""
        self.task = ""
        self.occupied_date = ""
        self.deadline = ""
        self.days_to_complete = 0
        self.task_completed_date = ""
        self.task_completed = False
        self.days_required = 0
        self.uploaded_area = ""
        self.projects = []

    def addProject(self):
        """This function is used to add the project in the database"""
        # NOTE: initially the project will add into the not completed projects database
        collection = db["Projects_Not_Completed"]
        self.serial_number = random.random()
        self.project_name = input("Enter the project name: ")
        self.task = input("Enter the task that is occupied: ")
        print("Date Format: YYYY-MM-DD")
        self.occupied_date = input("Enter the occupied date: ")
        self.deadline = input("Enter the deadline: ")
        self.days_to_complete = (
            datetime.strptime(self.deadline, "%Y-%m-%d")
            - datetime.strptime(self.occupied_date, "%Y-%m-%d")
        ).days
        self.task_completed = "no"
        self.days_required = 0
        self.uploaded_area = input("Enter the uploaded area: ")

        project = {
            "serial_number": self.serial_number,
            "project_name": self.project_name,
            "task": self.task,
            "occupied_date": self.occupied_date,
            "deadline": self.deadline,
            "days_to_complete": self.days_to_complete,
            "task_completed": self.task_completed,
            "days_required": self.days_required,
            "uploaded_area": self.uploaded_area,
        }

        while collection.find_one({"serial_number": self.serial_number}):
            print("Project with this serial number already exists!")
            self.serial_number = random.random()
            project["serial_number"] = self.serial_number

        collection.insert_one(project)
        print("Project added successfully!")

    def updateProject(self):
        """This function is used to update the project details"""
        user_choice = input(
            "Do you want to update the project in Projects_Completed or Projects_Not_Completed? (completed/not completed): "
        )
        collection = (
            db["Projects_Completed"]
            if user_choice.lower()[0] == "c"
            else db["Projects_Not_Completed"]
        )
        self.serial_number = float(
            input("Enter the serial number of the project you want to update: ")
        )
        project = collection.find_one({"serial_number": self.serial_number})

        if project:
            updation_area = input(
                "Enter the area you want to update: \n 1. project_name \n 2. task \n 3. occupied_date \n 4. deadline \n 5. days_to_complete \n 6. task_completed \n 7. days_required \n 8. uploaded_area \n"
            ).lower()
            if updation_area in self.__dict__:
                print(
                    f"Previous {updation_area.replace('_', ' ').title()}: {self.__dict__[updation_area]}"
                )
                self.__dict__[updation_area] = input(
                    f"Enter the new {updation_area.replace('_', ' ').title()}: "
                )
                if (
                    updation_area == "task_completed"
                    and self.__dict__[updation_area].lower()[0] == "y"
                ):
                    project["task_completed"] = self.__dict__[updation_area]
                    self.days_required = int(
                        input("Enter how many days are required to complete the task: ")
                    )
                    project["days_required"] = self.days_required
                    project["task_completed_date"] = datetime.now().strftime("%Y-%m-%d")
                    db["Projects_Completed"].insert_one(project)
                    db["Projects_Not_Completed"].delete_one(
                        {"serial_number": self.serial_number}
                    )
                    print(
                        "Project added to the completed projects database and removed from the not done projects database!"
                    )
                    return
                collection.update_one(
                    {"serial_number": self.serial_number},
                    {"$set": {updation_area: self.__dict__[updation_area]}},
                )
                print("Project updated successfully!")
            else:
                print("Invalid updation area! Try again.")
        else:
            print("Project not found!")

    def deleteProject(self):
        """This function is used to delete the project from the database"""
        print(
            "This will delete the project from the task which is not completed, not from the task which is completed|!"
        )
        local_serial_number = float(
            input("Enter the serial number of the project you want to delete: ")
        )
        project = db["Projects_Not_Completed"].find_one(
            {"serial_number": local_serial_number}
        )
        if project:
            db["Projects_Not_Completed"].delete_one(
                {"serial_number": local_serial_number}
            )
            print("Project deleted successfully!")
        else:
            print("Project not found!")

    def viewProjects(self):
        """Use to view the projects on the basis of user choice"""
        view_projects = input(
            "Do you want to view the projects on the basis of task completed or not? (yes/no): "
        )
        if view_projects.lower()[0] == "y":
            projects = db["Projects_Completed"].find({"task_completed": "yes"})
        else:
            projects = db["Projects_Not_Completed"].find()

        filter_choice = input(
            "Do you want to filter the projects by serial number or project name? (serial/project/both/none): "
        ).lower()
        if filter_choice[0] == "s":
            serial_number = float(input("Enter the serial number: "))
            projects = [
                project
                for project in projects
                if project["serial_number"] == serial_number
            ]
        elif filter_choice[0] == "p":
            project_name = input("Enter the project name: ")
            projects = [
                project
                for project in projects
                if project["project_name"].lower() == project_name.lower()
            ]
        elif filter_choice[0] == "b":
            serial_number = float(input("Enter the serial number: "))
            project_name = input("Enter the project name: ")
            projects = [
                project
                for project in projects
                if project["serial_number"] == serial_number
                and project["project_name"].lower() == project_name.lower()
            ]
        elif filter_choice[0] == "n":
            pass
        else:
            print("Invalid Input")
            return None

        projects = list(projects)
        if not projects:
            print("No such project exists")
            return None

        table = PrettyTable()
        table.field_names = [
            "Serial Number",
            "Project Name",
            "Task",
            "Occupied Date",
            "Deadline",
            "Days to Complete",
            "Task Completed",
            "Days Required",
            "Uploaded Area",
        ]

        for project in projects:
            table.add_row(
                [
                    project["serial_number"],
                    project["project_name"],
                    project["task"],
                    project["occupied_date"],
                    project["deadline"],
                    project["days_to_complete"],
                    project["task_completed"],
                    project["days_required"],
                    project["uploaded_area"],
                ]
            )

        print(table)
