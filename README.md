# 📓 Blog Sphere
A Full-Stack Blog Application built with FastAPI and React.

### Features:

- ✅ Sign-up & Sign-in
- ✅ Customizeable User Profile
- ✅ Create and manage posts
- ✅ Read, share and interact with posts
- ✅ API Documentation
- ✅ PostgreSQL Database
- ✅ Alembic Migrations and seed data
- ✅ Docker and Docker Compose
- ✅ CI/CD with GitHub Actions (coming soon)
- ✅ Monitoring and Logging (coming soon)
- ✅ Automated Tests (coming soon)

## 📚 Table of Contents
- [Getting Started](#-getting-started)
- [Commands](#-commands)
- [Endpoints](#-endpoints)
- [Tech Stack](#-tech-stack)
- [License](#-license)
- [Checklist](#-checklist)

To know more about the project structure, check the [structure.md](/docs/structure.md) file.

## 🤖 Getting Started
1. Clone the repository
```bash
git clone https://github.com/wesleybertipaglia/blog-sphere.git
```

2. Initialize and Activate the virtual environment
```bash
Make init
source venv/bin/activate
```

3. Install the dependencies and init the alembic
```bash
Make setup
```

4. Run the application
```bash
Make run
```

> 🚀 Open your browser and go to [http://localhost:8000](http://localhost:8000) to see the api in action.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                    | Action                                    |
| :------------------------  | :---------------------------------------- |
| `Make init`                | Initialize the virtual enviroment         |
| `source venv/bin/activate` | Activate the virtual enviroment           |
| `Make setup`               | Install dependencies and init the alembic |
| `Make freeze`              | Update the dependencies                   |
| `Make run`                 | Starts the application                    |
| `Make alembic-revision`    | Make an alembic revision                  |
| `Make alembic-upgrade`     | Make an alembic upgrade                   |

To know more about the commands, check the [commands.md](/docs/commands.md) file.

## 🪧 Endpoints
The API has the following endpoints:
- `/auth`: Sign-up and Sign-in
- `/profile`: Read, Update, Delete
- `/users`: Read
- `/posts`: Create, Read, Update, Delete

To know more about the endpoints, check the [endpoints.md](/docs/endpoints.md) file, or access the API documentation in the following URL:
[localhost:8000/docs](http://localhost:8000/docs)

## 🧩 Tech Stack
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/) and [Adminer](https://www.adminer.org/)

To know more about the tech stack, check the [stack.md](/docs/stack.md) file.

## ☑️ Cheklist

The following checklist can be used to track the project progress:

- [x] Authentication
- [x] Authorization
- [x] Documentation
- [ ] Tests
- [ ] Docker
- [ ] CI/CD
- [ ] Deploy
- [ ] Monitoring

## 📜 License

This repository is licensed under the [MIT]. See the [LICENSE](LICENSE) file for details.

[Back to top](#store-api)