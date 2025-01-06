# Command-Line Interface Documentation

This document provides a detailed guide on using the Command-Line Interface (CLI) for the priority-based task manager. Each command is explained with its description, syntax, arguments, examples, and potential errors.

## Commands Overview
- **`--add`**: Adds a new task.
- **`--list`**: Lists all tasks.
- **`--complete`**: Marks a task as completed.
- **`--delete`**: Deletes a task.

---

### Command: `--add`
- **Description**  
  Adds a new task to the task manager.

- **Syntax**  
  ```bash
  python main.py --add <title> <description> <priority> <due_date>
  ```

- **Arguments**  
  - `<title>`: The title of the task (string).  
  - `<description>`: A brief description of the task (string).  
  - `<priority>`: The priority level of the task (integer, e.g., 1 for high priority).  
  - `<due_date>`: The due date for the task (YYYY-MM-DD format, optional).  

- **Examples**  
  Add a new high-priority task with a due date:  
  ```bash
  python main.py --add "Learn Python" "Study Clean Architecture" 1 "2025-01-01"
  ```

  Add a low-priority task without a due date:  
  ```bash
  python main.py --add "Buy Groceries" "Weekly shopping" 3
  ```

- **Potential Errors**  
  1. **`ValueError: invalid literal for int() with base 10`**  
     - **Cause**: The `<priority>` value is not an integer.  
     - **Solution**: Ensure the `<priority>` argument is a valid integer (e.g., 1, 2, 3).  

  2. **`ValueError: time data 'XXXX' does not match format '%Y-%m-%d'`**  
     - **Cause**: The `<due_date>` is not in the correct `YYYY-MM-DD` format.  
     - **Solution**: Provide a properly formatted date, e.g., "2025-01-01".  

  3. **`sqlite3.IntegrityError: UNIQUE constraint failed`**  
     - **Cause**: A task with the same ID already exists.  
     - **Solution**: Check if the task already exists before adding it.

---

### Command: `--list`
- **Description**  
  Displays all tasks stored in the task manager.

- **Syntax**  
  ```bash
  python main.py --list
  ```

- **Arguments**  
  No arguments required.

- **Examples**  
  List all tasks:  
  ```bash
  python main.py --list
  ```

- **Potential Errors**  
  1. **`sqlite3.OperationalError: no such table: tasks`**  
     - **Cause**: The database has not been initialized or is corrupted.  
     - **Solution**: Ensure the database schema is created by running the setup process.

  2. **`IndexError: list index out of range`**  
     - **Cause**: No tasks are available.  
     - **Solution**: Add at least one task before running this command.

---

### Command: `--complete`
- **Description**  
  Marks a specific task as completed.

- **Syntax**  
  ```bash
  python main.py --complete <task_id>
  ```

- **Arguments**  
  - `<task_id>`: The unique ID of the task to be marked as completed (integer).  

- **Examples**  
  Mark task with ID `1` as completed:  
  ```bash
  python main.py --complete 1
  ```

- **Potential Errors**  
  1. **`ValueError: invalid literal for int() with base 10`**  
     - **Cause**: The `<task_id>` is not a valid integer.  
     - **Solution**: Provide a valid numeric ID (e.g., `1`).  

  2. **`TaskNotFoundError` (custom exception)**  
     - **Cause**: The task ID does not exist in the database.  
     - **Solution**: Verify the task ID by listing all tasks (`--list`) before using this command.

---

### Command: `--delete`
- **Description**  
  Deletes a specific task from the task manager.

- **Syntax**  
  ```bash
  python main.py --delete <task_id>
  ```

- **Arguments**  
  - `<task_id>`: The unique ID of the task to delete (integer).  

- **Examples**  
  Delete task with ID `1`:  
  ```bash
  python main.py --delete 1
  ```

- **Potential Errors**  
  1. **`TaskNotFoundError`**  
     - **Cause**: The task ID does not exist in the database.  
     - **Solution**: Verify the task ID before attempting to delete.  

  2. **`sqlite3.OperationalError: database is locked`**  
     - **Cause**: Another process is accessing the database.  
     - **Solution**: Ensure no other process is using the database and retry.

---

## General Recommendations
- Ensure Python and required packages are properly installed.
- Use valid arguments to avoid errors.
- Review logs for debugging when encountering issues.
- Refer to examples for proper usage.

For more information, consult the project README or contact the developer.

