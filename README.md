# Project Description
- Connect FastAPI to Postgres Database

### DBCONNECT | REST API - Python, FastAPI
- Python - 3.12.7
- Postgres Database - pgAdmin - 17.0
- Video URL - https://www.youtube.com/watch?v=398DuQbQJq0


### Command that use in this Projects

- setup initial project

**Create a Virtual Envioronment**

- create virtual envioronment (Do this if require)
```bash
python -m venv myenv
```
- activate the envioronment (Do this if require)
```bash
.\myenv\Scripts\activate
```

- create database in pgAdmin

// uncomment this below line
- user_schema.Base.metadata.create_all(bind=engine)

// for starting api
```bash
uvicorn main:app --reload
```