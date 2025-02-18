import project_management_tool as pmt  # importing the project management tool module


def main(self):
    """The main function of the project management tool is used to call the functions that are present into the class ProjectManagementTool"""
    while True:
        print(
            "1. Add Project\n2. Update Project\n3. Delete Project\n4. View Projects\n5. Exit"
        )
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.addProject()
        elif choice == 2:
            self.updateProject()
        elif choice == 3:
            self.deleteProject()
        elif choice == 4:
            self.viewProjects()
        elif choice == 5:
            print("Exiting...")
            exit(0)
        else:
            print("Invalid choice! Try again.")


# calling project management tool
if __name__ == "__main__":
    project_management_tool = (
        pmt.ProjectManagementTool()
    )  # creating an object of the class
    main(
        project_management_tool
    )  # calling the main function of the project management tool
