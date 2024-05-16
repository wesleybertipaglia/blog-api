# 🚀 Project Structure

Inside this project, you'll see the following folders and files:

```text
├── alembic/
├── app/
│   ├── controllers.py
│   ├── database.py
│   ├── models.py
│   └── schemes.py
├── docs/
├── mockup/
├── venv/
├── .gitignore
├── alembic.ini
├── docker-compose.yaml
├── main.py
├── Makefile
├── README.md
└── requirements.txt
```

There are several key components in this project:

- The `alembic` folder contains the database migration scripts. 
- The `app` folder contains the main application code.
    - The `controllers.py` file contains the API endpoints.
    - The `database.py` file contains the database connection setup.
    - The `models.py` file contains the database models.
    - The `schemes.py` file contains the Pydantic models for request and response payloads.
- The `docs` folder contains the project documentation.
- The `mockup` folder contains the mockup data for the database.
- The `venv` folder contains the Python virtual environment.
- The `.gitignore` file specifies which files and directories to ignore in version control.
- The `alembic.ini` file is the configuration file for Alembic.
- The `docker-compose.yaml` file is the configuration file for Docker Compose.
- The `main.py` file is the entry point for the FastAPI application.
- The `Makefile` contains shortcuts for common development tasks.
- The `README.md` file contains the project overview and setup instructions.
- The `requirements.txt` file lists the Python dependencies for the project.