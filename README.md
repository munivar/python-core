# Project Description
- Connect FastAPI to Postgres Database

### DBCONNECT | REST API - Python, FastAPI
- Python - 3.12.7
- Postgres Database - pgAdmin - 17.0
- Video URL - https://www.youtube.com/watch?v=398DuQbQJq0


### Usage (Command and Steps)

1. setup initial project

**Create a Virtual Envioronment**

2. create virtual envioronment (Do this if require)
```bash
python -m venv myenv
```
3. activate the envioronment (Do this if require)
```bash
.\myenv\Scripts\activate
```

4. create database in pgAdmin

5. uncomment this below line
```bash
user_schema.Base.metadata.create_all(bind=engine)
```

5. for starting api
```bash
uvicorn main:app --reload
```