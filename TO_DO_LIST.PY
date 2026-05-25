# Store tasks in a list
tasks = []
while True:

    # Heading
    print("\n TO DO LIST ")

    # Menu Options
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit")

    # Take user input
    choice = input("Enter your choice: ")

    # If user selects the option 1 → Add a Task to the list
    if choice == '1':
            print("\nAdd the task selected: ")
            # Take task from user
            task = input("Enter your task: ")
            # Add task in the list
            tasks.append(task)
            # Confirm the task has been added
            print("Task Added Successfully!")
    # If user selects the option 2 → View the Tasks in the list
    elif choice == '2':
        print("\n Your Tasks ")

        # Check if list is empty
        if len(tasks) == 0:
            print("No tasks available.")

        else:
            # see the tasks using loop
            for index, task in enumerate(tasks, start=1):
                print(index, ".", task)

    # If user selects the option 3 → Remove the Task from the list
    elif choice == '3':

        print("\n Remove Task Selected ")

        # Check if list is empty
        if len(tasks) == 0:
            print("No tasks to remove.")

        else:

            # Show all the tasks
            for index, task in enumerate(tasks, start=1):
                print(index, ".", task)

            # Ask which task to remove
            remove_task = int(input("Enter task number to remove: "))

            # Check if task number is valid
            if remove_task >= 1 and remove_task <= len(tasks):

                # Delete  the task from the list
                removed_task = tasks.pop(remove_task - 1)

                print(removed_task, " removed successfully! ")

            else:
                print(" Invalid task number. ")

    # If user selects the option 4 → Exit
    elif choice == '4':

        print(" Thank you for using the To Do List App. Goodbye! ")

        # Stop the loop
        break

    # Your choice is invalid
    else:
        print(" Invalid Choice! Please try again. ")