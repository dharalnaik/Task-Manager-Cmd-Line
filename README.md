# Task-Manager-Cmd-Line
A task management command line software created with python.
**Description:**

A Python program for a command-line task management system. Users will be able to perform various operations on tasks, including adding new tasks, displaying them, marking them as completed, deleting tasks, saving tasks to a file, and loading tasks from a file.

**Requirements:**

1. Users will have to enter task's title, and description.
2. A menu-driven command-line interface has been used that allows users to:
    - Add a new task.
    - Display all tasks.
    - Mark a task as completed.
    - Delete a task.
    - Save tasks to a file.
    - Load tasks from a file.
    - Quit the program.
    - (The menu is in the same order in the program)
3. Error handling has been taken care to handle invalid input and missing tasks gracefully.
4. The data structures for task storage is lists.

**Things to note:**
1. "program.py" is the main file for the source code of the program.
2. "task_manager.py" and "task.py" is the supporting file with all user-defined functions for different tasks to perform.
3. "task_data.txt" is the main text file on which different operations are performed.
4. "file1.txt" is the supporting file from which the tasks will be loaded to the main text file- task_data.txt .
