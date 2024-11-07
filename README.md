# Project Description
- Example of Project Stucture of APIs and Connect the Database and Create table using Base.metadata.create_all(bind=engine)

### APIDEV | REST API - Python, FastAPI
- Python - 3.12.7
- Postgres Database - pgAdmin - 17.0


### Usage (Command and Steps)

1. setup initial project structure
- This command will display a list of all installed Python packages along with their versions
```bash
pip freeze
```
- Run the following command to generate a list of installed packages
```bash
pip freeze > requirements.txt
```
- To install Python libraries listed in a requirements.txt file, you can use the following command
```bash
pip install -r requirements.txt
```
- uninstall all the packages
```bash
pip uninstall -r requirements.txt
```

2. create virtual envioronment (Do this if require)
```bash
python -m venv myenv
```
3. activate the envioronment (Do this if require)
```bash
.\myenv\Scripts\activate
```

4. create database in pgAdmin (check .env file for database name and other config)
```bash
pgAdmin 4 -> PostgresSQL 17 -> Databases -> Create -> Database -> (Your Database Name)
```

5. uncomment this below line
```bash
user_schema.Base.metadata.create_all(bind=engine)
```

6. for starting api
```bash
uvicorn app.main:app --reload
```