# Task Manager Web Application

A simple task management application allowing users to add, view, mark as done, and delete tasks. The application supports filtering tasks and viewing tasks for today.

## Features

- **View Tasks**: Display tasks based on their completion status.
- **Add Tasks**: Add new tasks with title, description, and due date.
- **Mark Tasks as Done/Incompleted**: Toggle the status of tasks.
- **Delete Tasks**: Remove tasks from the list.
- **Filter Tasks**: Search and filter tasks by title.
- **Today's Tasks**: View tasks specifically for the current date.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **API**: Fetch API (for communication between frontend and backend)

## File Structure

```
to-do-app/
├── static/
│ ├── css/
│ │ └── styles.css
│ └── js/
│ └── scripts.js
├── templates/
│ └── index.html
├── app.py
└── tasks.json
```

- **`static/css/styles.css`**: CSS file for styling the application.
- **`static/js/scripts.js`**: JavaScript file for handling application logic.
- **`templates/index.html`**: The main HTML file for the application.
- **`app.py`**: Flask application code.
- **`tasks.json`**: JSON file for storing tasks.

## Installation and Usage

### Backend Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
   ```

2. **Set up a virtual environment and install dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install Flask
   ```

3. **Run the Flask server:**

   ```bash
   python app.py
   ```
   The server will start and listen on http://127.0.0.1:5000/.

### Frontend Setup

1. **Open the index.html file in a web browser:**

   You can directly open `templates/index.html` in a browser or serve it using a web server.

## API Endpoints

- **`GET /tasks`**: Returns a list of all tasks.
- **`GET /task/<int:task_id>`**: Returns details of a specific task.
- **`POST /task`**: Creates a new task. Requires a JSON body with title, description date, and done properties.
- **`DELETE /task/<int:task_id>`**: Deletes a task by ID.
- **`PUT /task/<int:task_id>`**: Updates a task by ID. Requires a JSON body with updated task properties.

## Example Data

The **`tasks.json`** file includes tasks with the following structure:

```json
[
    {
        "id": 1,
        "title": "Buy milk",
        "description": "Buy milk at the store",
        "date": "2024-08-04",
        "done": true
    },
    {
        "id": 2,
        "title": "Meeting with John",
        "description": "Project meeting",
        "date": "2024-08-04",
        "done": false
    },
    {
        "id": 3,
        "title": "Visit the library",
        "description": "Return books to the library",
        "date": "2024-08-05"
    }
]
```

## Usage

- **Add Task**: Enter the task title, description, and due date in the form and click "Add".
- **View Tasks**: Tasks are displayed in the sidebar under "Tasks not completed" and "Tasks completed" sections.
- **Toggle Completed Tasks**: Click on the link to show or hide completed tasks.
- **Search Tasks**: Type in the search box to filter tasks by title.
- **View Today's Tasks**: View tasks scheduled for the current date in the main section.
- **Task Details**: Click on any task to view its details and options to delete or mark it as done.

## Contributing

Contributions are welcome! Please submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
