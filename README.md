
# Todo

Django Task Management (TODO) with Authentication is a web application developed on the Django framework that allows users to manage their tasks using CRUD (create, read, update, delete) functions and provides an authentication system for secure access to functionality applications.


## Authors

- [@robiya07](https://www.github.com/robiya07)


## Features

- Authentication: The application includes an authentication system that allows users to register, log into their accounts, and secure access to task management functionality

- Creating Tasks: Users can create new tasks by specifying their title, description, and other details. Creating a task is available only to registered users after logging in

- Task Reading: Registered users can view a list of their tasks, displaying information about the title, description, progress status, and other details. This allows users to be aware of their current tasks and their details

- Updating tasks: Users can make changes to their existing tasks, including changing the title, description, due dates, and status. Updating tasks is available only to authorized users

- Deleting tasks: Registered users have the ability to delete their tasks that are no longer required or have been completed. This helps keep your task list clean and manages only the most relevant and important tasks

## Screenshots
Home Page:

![Home Page](https://github.com/robiya07/todo/blob/master/apps/medias/Screenshot%20from%202023-06-28%2017-56-18.png)



Create|Update Page:

![Create|Update Page](https://github.com/robiya07/todo/blob/master/apps/medias/Screenshot%20from%202023-06-28%2017-56-34.png)



Delete Page:

![Delete Page](https://github.com/robiya07/todo/blob/master/apps/medias/Screenshot%20from%202023-06-28%2017-57-14.png)



Change Task Status:

![Change Task Status](https://github.com/robiya07/todo/blob/master/apps/medias/todo.png)


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Create a virtual environment

```bash
  python3 -m venv .venv
```

Activate virtual environment

```bash
  . .venv/bin/activate
```

Migrate

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python3 manage.py runserver
```
